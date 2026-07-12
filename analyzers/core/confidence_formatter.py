def explain_confidence(details):
    reasons = []

    factors = details["Factors"]

    if factors["Perfect Fit"]:
        reasons.append(
            "✓ Exact fit to all provided terms"
        )

    if factors["Has Competition"]:
        reasons.append(
            "• Another family provides an equally accurate fit"
        )

    if factors["Evidence Length"] < 10:
        reasons.append(
            "• Confidence is limited by a short sequence"
        )

    return reasons