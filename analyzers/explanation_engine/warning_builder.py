def explanation_warnings(analysis):

    warnings = []

    # Confidence may not exist yet
    confidence = getattr(
        analysis,
        "confidence",
        None
    )

    # Competition comes from recognition,
    # not confidence
    if hasattr(analysis, "runner_up"):

        runner = analysis.runner_up

        if runner is not None:

            warnings.append(
                f"{runner['Family'].NAME} also provides a comparable explanation."
            )


    # Evidence warning
    if hasattr(analysis, "sequence"):

        if len(analysis.sequence) < 8:

            warnings.append(
                "Additional terms would further confirm this classification."
            )


    # If confidence exists (future compatibility)
    if confidence is not None:

        if confidence.get("Tied"):

            warnings.append(
                "Multiple families provide an equally accurate explanation."
            )


    return warnings