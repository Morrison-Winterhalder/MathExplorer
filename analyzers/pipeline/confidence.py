import math

def calculate_confidence(
    winner_error,
    runner_up_error,
    sequence_length,
    complexity
):

    confidence = 85

    # -------------------------
    # 1. Fit Penalty
    # -------------------------
    fit_penalty = 100 * (1 - math.exp(-5 * winner_error))

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

    competition_penalty = 40 * (1 - separation)

    # -------------------------
    # 3. Evidence Penalty
    # -------------------------
    evidence_bonus = 20 * (1 - math.exp(-sequence_length / 20))       

    # -------------------------
    # 4. Complexity Penalty
    # -------------------------
    complexity_penalty = max(0, complexity - 2) * 0.5

    confidence -= fit_penalty
    confidence -= competition_penalty
    confidence += evidence_bonus
    confidence -= complexity_penalty

    confidence = max(0, min(100, confidence))

    return {
        "Fit Penalty": fit_penalty,
        "Competition Penalty": competition_penalty,
        "Evidence Bonus": evidence_bonus,
        "Complexity Penalty": complexity_penalty,
        "Separation": separation,
        "Confidence": confidence
    }

def update_confidence(sequence, report):

    best_fit = report["Recognition Scores"]["Best Fit"]

    if best_fit is None:
        report["Sequence Classification"]["Confidence"] = None
        return
    
    winner = best_fit["Winner Score"]

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

    report["Sequence Classification"]["Confidence"] = calculate_confidence(
        winner_error,
        runner_error,
        len(sequence),
        family_complexity
    )