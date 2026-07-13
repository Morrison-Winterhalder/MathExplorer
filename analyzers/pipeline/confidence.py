import math

def confidence_label(score):
    if score >= 90:
        return "Very High"
    elif score >= 75:
        return "High"
    elif score >= 60:
        return "Moderate"
    elif score >= 40:
        return "Low"
    else:
        return "Very Low"

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

    return {
        "Fit Penalty": fit_penalty,
        "Competition Penalty": competition_penalty,
        "Sample Size Bonus": sample_size_bonus,
        "Complexity Penalty": complexity_penalty,
        "Separation": separation,
        "Score": confidence,
        "Label": confidence_label(confidence),
        "Factors": {
            "Perfect Fit": winner_error == 0,
            "Has Competition": not math.isinf(runner_up_error),
            "Evidence Length": sequence_length   
        }
    }

def update_confidence(sequence, analysis):

    best_fit = analysis.best_fit

    if best_fit is None:
        analysis.confidence = None
        return
    
    winner = best_fit["Winners"][0]

    analysis.analysis_trace.append({
        "stage": "confidence",
        "event": "confidence_started",
        "family": winner["Family"].NAME,
    })

    tied = len(best_fit["Winners"]) > 1

    runner = best_fit["Runner Up Score"]

    winner_error = winner["RRN"]

    analysis.analysis_trace.append({
        "stage": "confidence",
        "event": "winner_assessed",
        "family": winner["Family"].NAME,
        "rrn": winner_error,
    })

    if runner is None:
        runner_error = float("inf")
    else:
        runner_error = runner["RRN"]

    analysis.analysis_trace.append({
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

    analysis.analysis_trace.append({
        "stage": "confidence",
        "event": "complexity_assessed",
        "complexity": family_complexity,
    })

    analysis.analysis_trace.append({
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

    analysis.analysis_trace.append({
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

        analysis.analysis_trace.append({
            "stage": "confidence",
            "event": "tie_adjustment",
            "adjustment": -15,
        })

    confidence["Tied"] = tied

    analysis.analysis_trace.append({
        "stage": "confidence",
        "event": "confidence_finalized",
        "score": confidence["Score"],
        "label": confidence_label(confidence["Score"]),
        "tied": tied,
    })

    analysis.confidence = confidence