def recognition_evidence(analysis):

    evidence = []

    ranking = analysis.ranking

    if ranking:
        winner = ranking[0]

        evidence.append(
            f"Residual error (RRN): {winner['RRN']:.6f}"
        )

        evidence.append(
            f"R² = {winner['R2']:.6f}"
        )

    metadata = analysis.classification.get(
        "Metadata",
        {}
    )
    recognition = metadata.get("RECOGNITION_METHOD")

    if recognition:
        evidence.append(
            f"Recognition method: {recognition}."
        )

    if analysis.verification:
        if analysis.verification["Verified"]:
            evidence.append(
                "The recovered formula exactly generates the known sequence terms."
            )

    return evidence