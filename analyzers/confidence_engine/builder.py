"""
Confidence Explanation Builder

Converts confidence factors into a structured explanation.
"""


from analyzers.core.reasoning import (
    build_reasoning
)


def build_confidence(confidence):

    reasoning = build_reasoning(
        confidence
    )


    score = confidence["Score"]


    if score >= 90:
        label = "Very High"

    elif score >= 70:
        label = "High"

    elif score >= 40:
        label = "Moderate"

    else:
        label = "Low"



    confidence["Label"] = label

    confidence.update(
        reasoning
    )


    return confidence


def build_summary(
    confidence,
    strengths,
    limitations,
):

    label = confidence["Label"].lower()

    if strengths:

        major = strengths[0]["Reason"]

    else:

        major = (
            "limited supporting evidence "
            "is currently available."
        )

    if limitations:

        weakness = limitations[0]["Reason"]

        return (
            f"Confidence is {label} because {major} "
            f"However, {weakness.lower()}"
        )

    return (
        f"Confidence is {label} because {major}"
    )