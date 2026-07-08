import math

def confidence_engine(
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
    margin = runner_up_error / max(winner_error, 1e-12)

    competition_penalty = 40 / margin

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
        "Confidence": confidence
    }

def update_confidence(sequence, report):

    best_fit = report["Recognition Scores"]["Best Fit"]

    if best_fit is None:
        report["Confidence"] = None
        return

    winner = best_fit["Winner Score"]

    runner = best_fit["Runner Up Score"]

    winner_error = winner["RRN"]

    if runner is None:
        runner_error = winner_error * 100
    else:
        runner_error = runner["RRN"]

    # complexity = (
    #     winner["Family"].complexity(
    #         winner["Parameters"]
    #     )
    # )

    complexity = 2

    report["Sequence Classification"]["Confidence"] = confidence_engine(
        winner_error,
        runner_error,
        len(sequence),
        complexity
    )