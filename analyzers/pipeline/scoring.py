from analyzers.core.statistics import (
    r_squared,
    relative_residual_norm,
    normalized_rmse,
)
from families.registry import FAMILIES
from analyzers.core.best_fit import best_fit

COMPLEXITY_WEIGHT = 1e-3
TIE_TOLERANCE = 1e-6


def score_family(sequence, family):

    fit = best_fit(sequence, family)

    if fit is None:
        return None

    predicted = fit["Predicted"]

    return {
        "Family": family,
        "Parameters": fit["Parameters"],
        "Predicted": predicted,
        "Residuals": fit["Residuals"],
        "NRMSE": normalized_rmse(sequence, predicted),
        "RRN": relative_residual_norm(sequence, predicted),
        "R2": r_squared(sequence, predicted),
    }



def update_scores(sequence, report):

    scores = []

    for family in FAMILIES:

        result = score_family(sequence, family)

        if result is None:
            report["Analysis Trace"].append({
                "stage": "scoring",
                "event": "family_tested",
                "family": family.NAME,
                "recognized": False,
            })
        else:
            report["Analysis Trace"].append({
                "stage": "scoring",
                "event": "family_tested",
                "family": family.NAME,
                "recognized": True,
                "rrn": result["RRN"],
                "nrmse": result["NRMSE"],
            })


            scores.append(result)

    selection = choose_best_fit(scores, report)

    if selection is None:
        report["Recognition Scores"] = {
            "Scores": scores,
            "Ranking": [],
            "Best Fit": None,
        }
        return

    report["Recognition Scores"] = {
        "Scores": scores,
        "Ranking": selection["Ranking"],
        "Best Fit": selection["Best Fit"],
    }


def choose_best_fit(scores, report):

    for score in scores:
        complexity = score["Family"].complexity(score["Parameters"])
        score["Complexity"] = complexity
        score["Ranking Score"] = (
            score["RRN"] + COMPLEXITY_WEIGHT * complexity
        )

        report["Analysis Trace"].append({
            "stage": "ranking",
            "event": "ranking_calculated",
            "family": score["Family"].NAME,
            "ranking_score": score["Ranking Score"],
            "complexity": complexity,
            "specificity": score["Family"].SPECIFICITY
        })

    ordered = sorted(
        scores,
        key=lambda score: score["Ranking Score"],
    )

    for rank, score in enumerate(ordered, start=1):
        score["Rank"] = rank

        report["Analysis Trace"].append({
            "stage": "ranking",
            "event": "family_ranked",
            "family": score["Family"].NAME,
            "rank": rank,
            "ranking_score": score["Ranking Score"],
        })

    if not ordered:
        return None

    best_score = ordered[0]["Ranking Score"]

    winners = []

    for score in ordered:
        if abs(score["Ranking Score"] - best_score) <= TIE_TOLERANCE:
            winners.append(score)
        else:
            break

    initial_winner_count = len(winners)

    if initial_winner_count > 1:
        report["Analysis Trace"].append({
            "stage": "ranking",
            "event": "tie_detected",
            "families": [
                winner["Family"].NAME
                for winner in winners
            ],
        })

    max_specificity = max(
        winner["Family"].SPECIFICITY
        for winner in winners
    )

    winners = [
        winner
        for winner in winners
        if winner["Family"].SPECIFICITY == max_specificity
    ]

    if initial_winner_count != len(winners):
        report["Analysis Trace"].append({
            "stage": "ranking",
            "event": "tie_resolved",
            "method": "specificity",
            "winners": [winner["Family"].NAME for winner in winners],
        })

    if initial_winner_count == len(ordered):
        report["Analysis Trace"].append({
            "stage": "classification",
            "event": "winner_selected",
            "winners": [winner["Family"].NAME for winner in winners],
        })

        return {
            "Ranking": ordered,
            "Best Fit": {
                "Winners": winners,
                "Runner Up": None,
                "Runner Up Score": None,
                "Separation": 1.0,
            },
        }

    runner_index = initial_winner_count

    if runner_index >= len(ordered):
        runner = None
        separation = 0.0
    else:
        runner = ordered[runner_index]

        report["Analysis Trace"].append({
            "stage": "classification",
            "event": "runner_up",
            "family": runner["Family"].NAME,
        })

        separation = (
            runner["Ranking Score"] - ordered[0]["Ranking Score"]
        ) / (
            runner["Ranking Score"] + ordered[0]["Ranking Score"] + 1e-12
        )

    report["Analysis Trace"].append({
        "stage": "classification",
        "event": "winner_selected",
        "winners": [winner["Family"].NAME for winner in winners],
    })

    return {
        "Ranking": ordered,
        "Best Fit": {
            "Winners": winners,
            "Runner Up": None if runner is None else runner["Family"],
            "Runner Up Score": runner,
            "Separation": separation,
        },
    }