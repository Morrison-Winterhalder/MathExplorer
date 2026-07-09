import math

def calculate_confidence(
    winner_error,
    runner_up_error,
    sequence_length,
    complexity
):

    BASE_CONFIDENCE = 60

    FIT_WEIGHT = 80
    FIT_CURVE = 8

    COMPETITION_WEIGHT = 20
    SAMPLE_SIZE_WEIGHT = 35

    COMPLEXITY_WEIGHT = 0.5

    confidence = BASE_CONFIDENCE

    # -------------------------
    # 1. Fit Penalty
    # -------------------------

    fit_penalty = FIT_WEIGHT * (
        1 - math.exp(-FIT_CURVE * winner_error)
    )

    # -------------------------
    # 2. Competition Penalty
    # -------------------------

    if math.isinf(runner_up_error):
        separation = 1.0
    elif runner_up_error == 0:
        separation = 0.0
    else:
        separation = max(
            0.0,
            min(1.0, 1 - winner_error / runner_up_error)
    )

    competition_penalty = COMPETITION_WEIGHT * (1 - separation)

    # -------------------------
    # 3. Sample Size Bonus
    # -------------------------
    sample_size_bonus = SAMPLE_SIZE_WEIGHT * (
        1 - math.exp(-sequence_length / 10)
    )       

    # -------------------------
    # 4. Complexity Penalty
    # -------------------------
    complexity_penalty = (
        max(0, complexity - 2)
        * COMPLEXITY_WEIGHT
    )

    confidence -= fit_penalty
    confidence -= competition_penalty
    confidence += sample_size_bonus
    confidence -= complexity_penalty

    confidence = max(0, min(100, confidence))

    if confidence >= 90:
        label = "Very High"
    elif confidence >= 75:
        label = "High"
    elif confidence >= 60:
        label = "Moderate"
    elif confidence >= 40:
        label = "Low"
    else:
        label = "Very Low"

    return {
        "Fit Penalty": fit_penalty,
        "Competition Penalty": competition_penalty,
        "Sample Size Bonus": sample_size_bonus,
        "Complexity Penalty": complexity_penalty,
        "Separation": separation,
        "Score": confidence,
        "Label": label
    }

def update_confidence(sequence, report):

    best_fit = report["Recognition Scores"]["Best Fit"]

    if best_fit is None:
        report["Sequence Classification"]["Confidence"] = None
        return
    
    winner = best_fit["Winners"][0]

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "confidence_started",
        "family": winner["Family"].NAME,
    })

    tied = len(best_fit["Winners"]) > 1

    runner = best_fit["Runner Up Score"]

    winner_error = winner["RRN"]

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "winner_assessed",
        "family": winner["Family"].NAME,
        "rrn": winner_error,
    })

    if runner is None:
        runner_error = float("inf")
    else:
        runner_error = runner["RRN"]

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "competition_assessed",
        "runner_up": (
            None if runner is None
            else runner["Family"].NAME
        ),
        "winner_rrn": winner_error,
        "runner_up_rrn": runner_error,
        "separation": best_fit["Separation"],
    })

    family_complexity = winner["Family"].complexity(
        winner["Parameters"]
    )

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "complexity_assessed",
        "complexity": family_complexity,
    })

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "sample_size_assessed",
        "sample_size": len(sequence),
    })

    confidence = calculate_confidence(
        winner_error,
        runner_error,
        len(sequence),
        family_complexity
    )

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "confidence_calculated",
        "score": confidence["Score"],
        "label": confidence["Label"],
        "fit_penalty": confidence["Fit Penalty"],
        "competition_penalty": confidence["Competition Penalty"],
        "sample_size_bonus": confidence["Sample Size Bonus"],
        "complexity_penalty": confidence["Complexity Penalty"],
        "separation": confidence["Separation"],
    })

    if tied:
        confidence["Score"] = max(0, confidence["Score"] - 15)

        report["Analysis Trace"].append({
            "stage": "confidence",
            "event": "tie_adjustment",
            "adjustment": -15,
        })

    score = confidence["Score"]

    if score >= 90:
        confidence["Label"] = "Very High"
    elif score >= 75:
        confidence["Label"] = "High"
    elif score >= 60:
        confidence["Label"] = "Moderate"
    elif score >= 40:
        confidence["Label"] = "Low"
    else:
        confidence["Label"] = "Very Low"

    confidence["Tied"] = tied

    report["Analysis Trace"].append({
        "stage": "confidence",
        "event": "confidence_finalized",
        "score": confidence["Score"],
        "label": confidence["Label"],
        "tied": tied,
    })

    report["Sequence Classification"]["Confidence"] = confidence