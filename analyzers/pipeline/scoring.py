from analyzers.core.statistics import (
    r_squared,
    relative_residual_norm,
    normalized_rmse,
)
from families.registry import FAMILIES, get_metadata
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
        "Metadata": get_metadata(family),
    }



def update_scores(sequence, analysis):

    scores = []

    for family in FAMILIES:

        result = score_family(sequence, family)

        if result is None:
            analysis.analysis_trace.append({
                "stage": "recognition",
                "event": "family_tested",
                "family": family.NAME,
                "recognized": False,
            })
        else:
            analysis.analysis_trace.append({
                "stage": "recognition",
                "event": "family_tested",
                "family": family.NAME,
                "recognized": True,
                "rrn": result["RRN"],
                "nrmse": result["NRMSE"],
            })

            scores.append(result)

    selection = choose_best_fit(scores, analysis)

    if selection is None:
        analysis.recognition_scores = {
            "Scores": scores,
            "Ranking": [],
            "Best Fit": None,
        }
        return

    analysis.recognition_scores = {
        "Scores": scores,
        "Ranking": selection["Ranking"],
        "Best Fit": selection["Best Fit"],
    }


def choose_best_fit(scores, analysis):

    for score in scores:
        complexity = score["Family"].complexity(score["Parameters"])
        score["Complexity"] = complexity
        score["Ranking Score"] = (
            score["RRN"] + COMPLEXITY_WEIGHT * complexity
        )

        analysis.analysis_trace.append({
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

        analysis.analysis_trace.append({
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
        analysis.analysis_trace.append({
            "stage": "ranking",
            "event": "tie_detected",
            "families": [
                winner["Family"].NAME
                for winner in winners
            ],
        })

    tie_candidates = winners.copy()


    max_specificity = max(
        winner["Family"].SPECIFICITY
        for winner in tie_candidates
    )


    winners = [
        winner
        for winner in tie_candidates
        if winner["Family"].SPECIFICITY == max_specificity
    ]

    if initial_winner_count != len(winners):
        analysis.analysis_trace.append({
            "stage": "ranking",
            "event": "tie_resolved",
            "method": "specificity",
            "winners": [winner["Family"].NAME for winner in winners],
        })

    if initial_winner_count == len(ordered):
        analysis.analysis_trace.append({
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

    runner_index = len(winners)

    if runner_index >= len(ordered):
        runner = None
        separation = 0.0
    else:
        runner = ordered[runner_index]

        analysis.analysis_trace.append({
            "stage": "classification",
            "event": "runner_up",
            "family": runner["Family"].NAME,
        })

        separation = (
            runner["Ranking Score"] - ordered[0]["Ranking Score"]
        ) / (
            runner["Ranking Score"] + ordered[0]["Ranking Score"] + 1e-12
        )


    if runner is not None:

        winner_family = winners[0]["Family"]

        runner_family = runner["Family"]


        analysis.analysis_trace.append({

            "stage": "recognition",

            "event": "candidate_comparison",

            "winner": winner_family.NAME,

            "alternative": runner_family.NAME,

            "comparison": [

                "Both candidates reproduce the observed sequence",

                (
                    f"{winner_family.NAME} provides a more "
                    "specific mathematical explanation"
                ),

                (
                    f"{runner_family.NAME} is a more "
                    "general model"
                ),

            ]

        })

    analysis.analysis_trace.append({
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