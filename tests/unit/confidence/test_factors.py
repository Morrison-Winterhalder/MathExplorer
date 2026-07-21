from types import SimpleNamespace

from analyzers.confidence_engine.factors import (
    fit_factor,
    competition_factor,
    hierarchy_factor,
    observation_factor,
    sample_size_factor,
    complexity_factor,
    generalization_factor,
    naturalness_factor,
    prediction_verification_factor,
)


# ==========================================================
# Fit Factor
# ==========================================================

def test_fit_factor_exact_match():

    result = fit_factor(0)

    assert result["name"] == "Exact Formula Match"
    assert result["impact"] == 25


def test_fit_factor_approximate_match():

    result = fit_factor(0.5)

    assert result["name"] == "Formula Accuracy"
    assert result["impact"] == 20


def test_fit_factor_never_negative():

    result = fit_factor(100)

    assert result["impact"] == 0



# ==========================================================
# Competition Factor
# ==========================================================

def test_competition_no_runner_up():

    result = competition_factor(
        winner=None,
        runner_up=None,
        winner_error=0,
        runner_up_error=None,
    )

    assert result["name"] == "No Competition"
    assert result["impact"] == 5



def test_competition_polynomial_alternative():

    polynomial = SimpleNamespace(
        NAME="Polynomial"
    )

    result = competition_factor(
        winner=None,
        runner_up={
            "Family": polynomial
        },
        winner_error=0,
        runner_up_error=0,
    )

    assert result["name"] == "Generic Model Alternative"
    assert result["impact"] == -5



def test_competing_equal_explanations():

    family = SimpleNamespace(
        NAME="Arithmetic"
    )

    result = competition_factor(
        winner=None,
        runner_up={
            "Family": family
        },
        winner_error=1,
        runner_up_error=1,
    )

    assert result["name"] == "Competing Explanation"
    assert result["impact"] == -15



def test_family_separation():

    family = SimpleNamespace(
        NAME="Squares"
    )

    result = competition_factor(
        winner=None,
        runner_up={
            "Family": family
        },
        winner_error=0,
        runner_up_error=5,
    )

    assert result["name"] == "Family Separation"
    assert result["impact"] == 5



# ==========================================================
# Hierarchy Factor
# ==========================================================

def test_hierarchy_no_family():

    result = hierarchy_factor(None)

    assert result["impact"] == 0



def test_hierarchy_root_family():

    family = SimpleNamespace(
        NAME="Recursive",
        PARENT=None
    )

    result = hierarchy_factor(family)

    assert result["name"] == "Root Family"



def test_hierarchy_child_family():

    family = SimpleNamespace(
        NAME="Fibonacci Numbers",
        PARENT="Linear Recurrence"
    )

    result = hierarchy_factor(family)

    assert result["impact"] == 8



# ==========================================================
# Observation Factor
# ==========================================================

def test_observation_factor():

    analysis = SimpleNamespace(
        explanation={
            "Reasons": [
                "reason1",
                "reason2",
                "reason3",
            ]
        }
    )

    result = observation_factor(analysis)

    assert result["impact"] == 3



def test_observation_factor_caps():

    analysis = SimpleNamespace(
        explanation={
            "Reasons": list(range(20))
        }
    )

    result = observation_factor(analysis)

    assert result["impact"] == 8



# ==========================================================
# Sample Size Factor
# ==========================================================

def test_large_sample():

    result = sample_size_factor(10)

    assert result["name"] == "Large Evidence Sample"
    assert result["impact"] == 10



def test_adequate_sample():

    result = sample_size_factor(7)

    assert result["name"] == "Adequate Evidence Sample"



def test_limited_sample():

    result = sample_size_factor(3)

    assert result["name"] == "Limited Evidence Sample"



# ==========================================================
# Complexity Factor
# ==========================================================

def test_simple_complexity():

    result = complexity_factor(1)

    assert result["name"] == "Simple Explanation"
    assert result["impact"] == 5



def test_complexity_penalty():

    result = complexity_factor(5)

    assert result["name"] == "Complex Explanation"
    assert result["impact"] == -6



def test_complexity_penalty_caps():

    result = complexity_factor(100)

    assert result["impact"] == -10



# ==========================================================
# Generalization Factor
# ==========================================================

def make_analysis(family):

    return SimpleNamespace(
        best_fit={
            "Winners": [
                {
                    "Family": family,
                    "Parameters": {},
                }
            ]
        }
    )


def test_generalization_polynomial_penalty():

    family = SimpleNamespace(
        NAME="Polynomial",
        complexity=lambda _: 1
    )

    result = generalization_factor(
        make_analysis(family)
    )

    assert result["name"] == "Weak Generalization"



def test_generalization_simple_family():

    family = SimpleNamespace(
        NAME="Squares",
        complexity=lambda _: 1
    )

    result = generalization_factor(
        make_analysis(family)
    )

    assert result["impact"] == 8



# ==========================================================
# Naturalness Factor
# ==========================================================

def test_natural_family():

    family = SimpleNamespace(
        NATURAL_FAMILY=True
    )

    result = naturalness_factor(family)

    assert result["impact"] == 10



def test_non_natural_family():

    family = SimpleNamespace(
        NATURAL_FAMILY=False
    )

    result = naturalness_factor(family)

    assert result["impact"] == -5



def test_unknown_naturalness():

    family = SimpleNamespace()

    result = naturalness_factor(family)

    assert result["impact"] == 0



# ==========================================================
# Prediction Verification
# ==========================================================

def test_prediction_verified():

    report = {
        "Verification": {
            "Predicted Terms": [1,2,3],
            "Verified": True,
        }
    }

    result = prediction_verification_factor(report)

    assert result["impact"] == 15



def test_prediction_generated_only():

    report = {
        "Verification": {
            "Predicted Terms": [1,2,3],
            "Verified": False,
        }
    }

    result = prediction_verification_factor(report)

    assert result["impact"] == 5



def test_no_prediction():

    report = {
        "Verification": {}
    }

    result = prediction_verification_factor(report)

    assert result["impact"] == 0