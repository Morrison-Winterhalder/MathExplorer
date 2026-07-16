"""
Confidence Evidence Factors

Each factor evaluates one source of evidence.
"""


# --------------------------------------------------
# Mathematical Fit Evidence
# --------------------------------------------------

def fit_factor(winner_error):

    if winner_error == 0:

        return {
            "name": "Exact Formula Match",
            "impact": 25,
            "reason":
                "The recovered formula exactly reproduces all observed terms.",
        }


    return {
        "name": "Formula Accuracy",
        "impact": max(
            0,
            25 - winner_error * 10
        ),
        "reason":
            "The recovered formula closely matches the observed sequence.",
    }



# --------------------------------------------------
# Competition Evidence
# --------------------------------------------------

def competition_factor(
    winner,
    runner_up,
    winner_error,
    runner_up_error
):

    if runner_up is None:

        return {
            "name": "No Competition",
            "impact": 5,
            "reason":
                "No competing family produced a comparable explanation.",
        }


    runner_family = runner_up.get(
        "Family"
    )

    runner_name = getattr(
        runner_family,
        "NAME",
        ""
    )


    if runner_name == "Polynomial":

        return {
            "name": "Generic Model Alternative",
            "impact": -5,
            "reason":
                "Polynomial interpolation matches the terms but is a generic explanation rather than a specific mathematical family.",
        }


    if winner_error == runner_up_error:

        return {
            "name": "Competing Explanation",
            "impact": -15,
            "reason":
                "Another mathematical family explains the observed terms equally well.",
        }


    return {
        "name": "Family Separation",
        "impact": 5,
        "reason":
            "The selected family explains the sequence better than alternatives.",
    }



# --------------------------------------------------
# Hierarchy Evidence
# --------------------------------------------------

def hierarchy_factor(family):

    if family is None:
        return {
            "name": "No Hierarchy Evidence",
            "impact": 0,
            "reason":
                "No family hierarchy information was available.",
        }


    if family.PARENT is None:

        return {
            "name": "Root Family",
            "impact": 3,
            "reason":
                "The selected family is a valid root classification.",
        }


    return {
        "name": "Hierarchy Consistency",
        "impact": 8,
        "reason":
            f"{family.NAME} correctly belongs to {family.PARENT}.",
    }



# --------------------------------------------------
# Observation Evidence
# --------------------------------------------------

def observation_factor(analysis):

    reasons = analysis.explanation.get(
        "Reasons",
        []
    )

    count = len(reasons)


    return {
        "name": "Observed Evidence",
        "impact": min(
            8,
            count
        ),
        "reason":
            f"{count} mathematical observations support the classification.",
    }



# --------------------------------------------------
# Sample Size Evidence
# --------------------------------------------------

def sample_size_factor(sequence_length):

    if sequence_length >= 10:

        return {
            "name": "Large Evidence Sample",
            "impact": 10,
            "reason":
                "The sequence contains many terms for structural analysis.",
        }


    if sequence_length >= 5:

        return {
            "name": "Adequate Evidence Sample",
            "impact": 5,
            "reason":
                "The sequence contains enough terms for pattern analysis.",
        }


    return {
        "name": "Limited Evidence Sample",
        "impact": 0,
        "reason":
            "The sequence has enough terms for recognition but limited confirmation.",
    }



# --------------------------------------------------
# Complexity Evidence
# --------------------------------------------------

def complexity_factor(complexity):

    if complexity <= 2:

        return {
            "name": "Simple Explanation",
            "impact": 5,
            "reason":
                "The family provides a simple mathematical explanation.",
        }


    penalty = min(
        10,
        (complexity - 2) * 2
    )


    return {
        "name": "Complex Explanation",
        "impact": -penalty,
        "reason":
            "The explanation requires a more complex model.",
    }



# --------------------------------------------------
# Prediction Evidence
# --------------------------------------------------

def prediction_factor(analysis):

    verification = analysis.verification

    predicted = verification.get(
        "Predicted Terms",
        []
    )

    verified = verification.get(
        "Verified Terms",
        []
    )


    if not predicted:

        return {
            "name": "No Prediction Evidence",
            "impact": -5,
            "reason":
                "No unseen prediction test was performed.",
        }


    accuracy = len(verified) / len(predicted)


    if accuracy == 1:

        return {
            "name": "Prediction Verification",
            "impact": 10,
            "reason":
                "The family correctly predicted additional terms.",
        }


    return {
        "name": "Prediction Failure",
        "impact": -15,
        "reason":
            "Predicted terms failed verification.",
    }



# --------------------------------------------------
# Generalization Strength
# --------------------------------------------------

def generalization_factor(analysis):

    winner = analysis.best_fit["Winners"][0]

    family = winner["Family"]

    complexity = family.complexity(
        winner["Parameters"]
    )


    if family.NAME == "Polynomial":

        return {
            "name": "Weak Generalization",
            "impact": -10,
            "reason":
                "Polynomial models can fit finite data without representing the true structure.",
        }


    if complexity <= 2:

        return {
            "name": "Strong Generalization",
            "impact": 8,
            "reason":
                "The rule represents a simple reusable mathematical structure.",
        }


    return {
        "name": "Moderate Generalization",
        "impact": 3,
        "reason":
            "The rule explains the sequence with moderate complexity.",
    }



# --------------------------------------------------
# Naturalness Evidence
# --------------------------------------------------

def naturalness_factor(family):

    natural = getattr(
        family,
        "NATURAL_FAMILY",
        None
    )


    if natural is True:

        return {
            "name": "Natural Family",
            "impact": 10,
            "reason":
                "The classification corresponds to a recognized mathematical sequence family.",
        }


    if natural is False:

        return {
            "name": "Non-Natural Model",
            "impact": -5,
            "reason":
                "The classification is a general model rather than a natural sequence family.",
        }


    return {
        "name": "Unknown Naturalness",
        "impact": 0,
        "reason":
            "No naturalness information was available.",
    }



# --------------------------------------------------
# Prediction Verification
# --------------------------------------------------

def prediction_verification_factor(report):

    verification = report.get(
        "Verification",
        {}
    )


    if verification.get("Verified"):

        return {
            "name": "Prediction Verification",
            "impact": 15,
            "reason":
                "The family successfully predicted unseen terms.",
        }


    return {
        "name": "No Prediction Evidence",
        "impact": 0,
        "reason":
            "The classification has not yet been verified using unseen sequence terms.",
    }