"""
Confidence Evidence Categories

Groups confidence factors into broader reasoning categories.
"""


EVIDENCE_CATEGORIES = {

    "Mathematical": [
        "Exact Formula Match",
        "Formula Accuracy",
        "Observed Evidence",
        "Prediction Verification",
    ],


    "Structural": [
        "Hierarchy Consistency",
        "Root Family",
        "Related Family Support",
        "Natural Family"
    ],


    "Competitive": [
        "No Competition",
        "Family Separation",
        "Competing Explanation",
    ],


    "Reliability": [
        "Large Evidence Sample",
        "Adequate Evidence Sample",
        "Limited Evidence Sample",
        "Simple Explanation",
        "Complex Explanation",
    ],

}