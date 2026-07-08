from analyzers.core.statistics import r_squared, relative_residual_norm, normalized_rmse
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
        "R2": r_squared(sequence, predicted)
    }

def update_scores(sequence, report):

    scores = {}

    for family in FAMILIES:
        result = score_family(sequence, family)

        if result is None:
            continue

        scores[family.NAME] = result

    best_fit = choose_best_fit(scores)

    if best_fit is None:
        report["Recognition Scores"] = {
            "Scores": scores,
            "Ranking": [],
            "Best Fit": None
        }
        return

    report["Recognition Scores"] = {
        "Scores": scores,
        "Ranking": best_fit["Ranking"],
        "Best Fit": best_fit["Best Fit"]
    }

def choose_best_fit(scores):

    for score in scores.values():
        complexity = score["Family"].complexity(score["Parameters"])
        score["Complexity"] = complexity
        score["Ranking Score"] = (
            score["RRN"] + COMPLEXITY_WEIGHT * complexity
        )

    ordered = sorted(
        scores.items(),
        key=lambda item: item[1]["Ranking Score"]
    )

    if len(ordered) == 0:
        return None

    winner_family, winner = ordered[0]

    if len(ordered) == 1:
        return {
            "Ranking": ordered,
            "Best Fit": {
                "Winner": winner_family,
                "Winner Score": winner,
                "Runner Up": None,
                "Runner Up Score": None,
                "Separation": 1.0
            }
        }

    runner_family, runner = ordered[1]

    winner_rrn = winner["RRN"]
    runner_rrn = runner["RRN"]

    separation = (
        runner_rrn - winner_rrn
    ) / (
        runner_rrn + winner_rrn + 1e-12
    )

    return {
        "Ranking": ordered,
        "Best Fit": {
            "Winner": winner_family,
            "Winner Score": winner,
            "Runner Up": runner_family,
            "Runner Up Score": runner,
            "Separation": separation
        }
    }