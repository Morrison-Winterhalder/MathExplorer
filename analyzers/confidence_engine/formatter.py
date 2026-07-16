"""
Confidence formatting utilities.
"""


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