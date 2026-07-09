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

    tied = len(best_fit["Winners"]) > 1

    if winner is None:
        report["Sequence Classification"]["Confidence"] = None
        return

    runner = best_fit["Runner Up Score"]

    winner_error = winner["RRN"]

    if runner is None:
        runner_error = float("inf")
    else:
        runner_error = runner["RRN"]

    family_complexity = winner["Family"].complexity(
        winner["Parameters"]
    )

    confidence = calculate_confidence(
        winner_error,
        runner_error,
        len(sequence),
        family_complexity
    )

    if tied:
        confidence["Score"] = max(0, confidence["Score"] - 15)

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

    report["Sequence Classification"]["Confidence"] = confidence