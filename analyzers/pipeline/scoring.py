from analyzers.core.statistics import (
    r_squared,
    relative_residual_norm,
    normalized_rmse,
)
from families.registry import FAMILIES
from analyzers.core.best_fit import best_fit

COMPLEXITY_WEIGHT = 1e-3


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

        if result is not None:
            scores.append(result)

    selection = choose_best_fit(scores)

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


def choose_best_fit(scores):

    TIE_TOLERANCE = 1e-6

    for score in scores:
        complexity = score["Family"].complexity(score["Parameters"])
        score["Complexity"] = complexity
        score["Ranking Score"] = (
            score["RRN"] + COMPLEXITY_WEIGHT * complexity
        )

    ordered = sorted(
        scores,
        key=lambda score: score["Ranking Score"],
    )

    if not ordered:
        return None

    best_rrn = ordered[0]["RRN"]

    winners = []

    for score in ordered:
        if abs(score["RRN"] - best_rrn) <= TIE_TOLERANCE:
            winners.append(score)
        else:
            break

    if len(ordered) == 1:
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

        separation = (
            runner["RRN"] - ordered[0]["RRN"]
        ) / (
            runner["RRN"] + ordered[0]["RRN"] + 1e-12
        )

    return {
        "Ranking": ordered,
        "Best Fit": {
            "Winners": winners,
            "Runner Up": None if runner is None else runner["Family"],
            "Runner Up Score": runner,
            "Separation": separation,
        },
    }