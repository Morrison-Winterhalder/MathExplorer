"""
Confidence Scoring Engine

Combines evidence factors into a confidence score.
"""

from analyzers.confidence_engine.formatter import (
    confidence_label,
)


CATEGORY_WEIGHTS = {

    "Mathematical": 0.35,

    "Structural": 0.30,

    "Competitive": 0.20,

    "Reliability": 0.15,

}


CATEGORY_BASELINES = {

    "Mathematical": 50,

    "Structural": 50,

    "Competitive": 70,

    "Reliability": 65,

}



def calculate_confidence(factors):

    weighted = calculate_weighted_score(
        factors
    )

    return {
        "Score": weighted["Score"],

        "Label": confidence_label(
            weighted["Score"]
        ),

        "Category Breakdown":
            weighted["Category Breakdown"],

        "Factors": factors,
    }



def categorize_factor(factor):

    name = factor["name"]


    if name in {

        "Exact Formula Match",

        "Formula Accuracy",

        "Observed Evidence",

        "Prediction Verification",

        "Adequate Evidence Sample",

    }:

        return "Mathematical"



    if name in {

        "Hierarchy Consistency",

        "Established Family",

        "Root Family",

        "Natural Family",

        "Strong Generalization",

        "Simple Explanation",

    }:

        return "Structural"



    if name in {

        "No Competition",

        "Family Separation",

        "Competing Explanation",

    }:

        return "Competitive"



    return "Reliability"




def calculate_weighted_score(factors):


    categories = {

        category: []

        for category in CATEGORY_WEIGHTS

    }



    for factor in factors:

        category = categorize_factor(
            factor
        )

        categories[category].append(
            factor
        )



    breakdown = {}

    score = 0



    for category, weight in CATEGORY_WEIGHTS.items():


        evidence = categories[category]


        if not evidence:

            category_score = CATEGORY_BASELINES[category]


        else:


            total = sum(
                item["impact"]
                for item in evidence
            )


            category_score = (
                CATEGORY_BASELINES[category]
                +
                total
            )


            category_score = max(
                0,
                min(
                    100,
                    category_score
                )
            )


        breakdown[category] = category_score


        score += (
            category_score
            *
            weight
        )



    return {

        "Score": round(score),

        "Category Breakdown": breakdown,

    }