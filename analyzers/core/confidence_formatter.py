def explain_confidence(confidence):

    if confidence is None:
        return []

    explanation = []

    strengths = confidence.get(
        "Strengths",
        []
    )

    limitations = confidence.get(
        "Limitations",
        []
    )


    if strengths:

        explanation.append(
            "Supporting evidence:"
        )

        for factor in strengths:

            explanation.append(
                f"• {factor['Reason']}"
            )


    if limitations:

        explanation.append(
            "Confidence limitations:"
        )

        for factor in limitations:

            explanation.append(
                f"• {factor['Reason']}"
            )


    return explanation