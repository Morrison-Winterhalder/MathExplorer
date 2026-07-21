import pytest

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

from analyzers.confidence_engine.scorer import (
    calculate_confidence,
    calculate_weighted_score,
    categorize_factor,
)


# ============================================================
# Helper Objects
# ============================================================


class MockFamily:

    def __init__(
        self,
        name="Test Family",
        parent=None,
        natural=True,
    ):

        self.NAME = name

        self.PARENT = parent

        self.NATURAL_FAMILY = natural


class MockAnalysis:

    def __init__(
        self,
        reasons=None,
    ):

        self.explanation = {

            "Reasons":
                reasons
                if reasons is not None
                else []

        }


class MockBestFitAnalysis:

    def __init__(
        self,
        family,
        parameters=None,
    ):

        self.best_fit = {

            "Winners": [

                {

                    "Family": family,

                    "Parameters":
                        parameters
                        if parameters is not None
                        else {},

                }

            ]

        }


class MockReport:

    def __init__(
        self,
        predicted_terms=None,
        verified=False,
    ):

        self.data = {

            "Verification": {

                "Predicted Terms":
                    predicted_terms
                    if predicted_terms is not None
                    else [],

                "Verified":
                    verified,

            }

        }

    def get(
        self,
        key,
        default=None,
    ):

        return self.data.get(
            key,
            default,
        )


# ============================================================
# Fit Evidence
# ============================================================


def test_exact_fit_produces_exact_formula_match():

    factor = fit_factor(

        winner_error=0

    )

    assert factor["name"] == (
        "Exact Formula Match"
    )

    assert factor["impact"] == 25


def test_imperfect_fit_produces_formula_accuracy():

    factor = fit_factor(

        winner_error=0.5

    )

    assert factor["name"] == (
        "Formula Accuracy"
    )

    assert factor["impact"] < 25


def test_worse_fit_reduces_fit_impact():

    excellent = fit_factor(

        winner_error=0.1

    )

    poor = fit_factor(

        winner_error=1.0

    )

    assert excellent["impact"] > (
        poor["impact"]
    )


def test_fit_impact_never_becomes_negative():

    factor = fit_factor(

        winner_error=1000

    )

    assert factor["impact"] >= 0


# ============================================================
# Competition Evidence
# ============================================================


def test_no_competition_produces_no_competition_factor():

    factor = competition_factor(

        winner=None,

        runner_up=None,

        winner_error=0,

        runner_up_error=None,

    )

    assert factor["name"] == (
        "No Competition"
    )

    assert factor["impact"] == 5


def test_polynomial_competitor_is_penalized_as_generic_model():

    polynomial = MockFamily(

        name="Polynomial"

    )

    runner_up = {

        "Family": polynomial

    }

    factor = competition_factor(

        winner=None,

        runner_up=runner_up,

        winner_error=0,

        runner_up_error=0,

    )

    assert factor["name"] == (
        "Generic Model Alternative"
    )

    assert factor["impact"] == -5


def test_equal_errors_produce_competing_explanation():

    runner_up = {

        "Family": MockFamily(

            name="Other Family"

        )

    }

    factor = competition_factor(

        winner=None,

        runner_up=runner_up,

        winner_error=1.0,

        runner_up_error=1.0,

    )

    assert factor["name"] == (
        "Competing Explanation"
    )

    assert factor["impact"] == -15


def test_better_winner_produces_family_separation():

    runner_up = {

        "Family": MockFamily(

            name="Other Family"

        )

    }

    factor = competition_factor(

        winner=None,

        runner_up=runner_up,

        winner_error=0.0,

        runner_up_error=1.0,

    )

    assert factor["name"] == (
        "Family Separation"
    )

    assert factor["impact"] == 5


# ============================================================
# Hierarchy Evidence
# ============================================================


def test_missing_family_produces_no_hierarchy_evidence():

    factor = hierarchy_factor(

        family=None

    )

    assert factor["name"] == (
        "No Hierarchy Evidence"
    )

    assert factor["impact"] == 0


def test_root_family_receives_root_classification():

    family = MockFamily(

        name="Explicit",

        parent=None,

    )

    factor = hierarchy_factor(

        family

    )

    assert factor["name"] == (
        "Root Family"
    )

    assert factor["impact"] == 3


def test_child_family_receives_hierarchy_consistency():

    family = MockFamily(

        name="Factorials",

        parent="Special",

    )

    factor = hierarchy_factor(

        family

    )

    assert factor["name"] == (
        "Hierarchy Consistency"
    )

    assert factor["impact"] == 8


# ============================================================
# Observation Evidence
# ============================================================


def test_observation_factor_counts_explanation_reasons():

    analysis = MockAnalysis(

        reasons=[

            "Reason one",

            "Reason two",

            "Reason three",

        ]

    )

    factor = observation_factor(

        analysis

    )

    assert factor["name"] == (
        "Observed Evidence"
    )

    assert factor["impact"] == 3


def test_observation_factor_is_capped():

    analysis = MockAnalysis(

        reasons=[

            "Reason"

        ] * 100

    )

    factor = observation_factor(

        analysis

    )

    assert factor["impact"] == 8


# ============================================================
# Sample Size Evidence
# ============================================================


def test_short_sequence_has_limited_sample_evidence():

    factor = sample_size_factor(

        sequence_length=4

    )

    assert factor["name"] == (
        "Limited Evidence Sample"
    )

    assert factor["impact"] == 0


def test_medium_sequence_has_adequate_sample_evidence():

    factor = sample_size_factor(

        sequence_length=5

    )

    assert factor["name"] == (
        "Adequate Evidence Sample"
    )

    assert factor["impact"] == 5


def test_long_sequence_has_large_sample_evidence():

    factor = sample_size_factor(

        sequence_length=10

    )

    assert factor["name"] == (
        "Large Evidence Sample"
    )

    assert factor["impact"] == 10


def test_longer_sequences_do_not_reduce_sample_evidence():

    short = sample_size_factor(

        sequence_length=5

    )

    long = sample_size_factor(

        sequence_length=20

    )

    assert long["impact"] >= (
        short["impact"]
    )


# ============================================================
# Complexity Evidence
# ============================================================


def test_simple_model_receives_simple_explanation_bonus():

    factor = complexity_factor(

        complexity=1

    )

    assert factor["name"] == (
        "Simple Explanation"
    )

    assert factor["impact"] == 5


def test_complex_model_receives_penalty():

    factor = complexity_factor(

        complexity=10

    )

    assert factor["name"] == (
        "Complex Explanation"
    )

    assert factor["impact"] < 0


def test_complexity_penalty_is_capped():

    factor = complexity_factor(

        complexity=1000

    )

    assert factor["impact"] >= -10


# ============================================================
# Naturalness Evidence
# ============================================================


def test_natural_family_receives_naturalness_bonus():

    family = MockFamily(

        natural=True

    )

    factor = naturalness_factor(

        family

    )

    assert factor["name"] == (
        "Natural Family"
    )

    assert factor["impact"] == 10


def test_non_natural_family_receives_penalty():

    family = MockFamily(

        natural=False

    )

    factor = naturalness_factor(

        family

    )

    assert factor["name"] == (
        "Non-Natural Model"
    )

    assert factor["impact"] == -5


def test_unknown_naturalness_receives_neutral_score():

    family = MockFamily(

        natural=None

    )

    factor = naturalness_factor(

        family

    )

    assert factor["name"] == (
        "Unknown Naturalness"
    )

    assert factor["impact"] == 0


# ============================================================
# Confidence Categorization
# ============================================================


@pytest.mark.parametrize(

    "factor_name, expected_category",

    [

        (

            "Exact Formula Match",

            "Mathematical",

        ),

        (

            "Formula Accuracy",

            "Mathematical",

        ),

        (

            "Observed Evidence",

            "Mathematical",

        ),

        (

            "Prediction Verification",

            "Mathematical",

        ),

        (

            "Hierarchy Consistency",

            "Structural",

        ),

        (

            "Root Family",

            "Structural",

        ),

        (

            "Natural Family",

            "Structural",

        ),

        (

            "Strong Generalization",

            "Structural",

        ),

        (

            "Simple Explanation",

            "Structural",

        ),

        (

            "No Competition",

            "Competitive",

        ),

        (

            "Family Separation",

            "Competitive",

        ),

        (

            "Competing Explanation",

            "Competitive",

        ),

    ],

)


def test_factor_is_categorized_correctly(

    factor_name,

    expected_category,

):

    factor = {

        "name":
            factor_name,

        "impact":
            5,

    }

    assert categorize_factor(

        factor

    ) == expected_category


def test_unknown_factor_defaults_to_reliability():

    factor = {

        "name":
            "Unknown Factor",

        "impact":
            5,

    }

    assert categorize_factor(

        factor

    ) == "Reliability"


# ============================================================
# Weighted Confidence Scoring
# ============================================================


def test_empty_factors_use_category_baselines():

    result = calculate_weighted_score(

        []

    )

    assert result["Score"] is not None

    assert result["Category Breakdown"] == {

        "Mathematical": 50,

        "Structural": 50,

        "Competitive": 70,

        "Reliability": 65,

    }


def test_positive_factor_increases_category_score():

    factors = [

        {

            "name":
                "Exact Formula Match",

            "impact":
                25,

        }

    ]

    result = calculate_weighted_score(

        factors

    )

    assert result["Category Breakdown"][

        "Mathematical"

    ] > 50


def test_negative_factor_decreases_category_score():

    factors = [

        {

            "name":
                "Competing Explanation",

            "impact":
                -15,

        }

    ]

    result = calculate_weighted_score(

        factors

    )

    assert result["Category Breakdown"][

        "Competitive"

    ] < 70


def test_category_scores_are_bounded():

    factors = [

        {

            "name":
                "Exact Formula Match",

            "impact":
                1000,

        },

        {

            "name":
                "Competing Explanation",

            "impact":
                -1000,

        },

    ]

    result = calculate_weighted_score(

        factors

    )

    for score in result["Category Breakdown"].values():

        assert 0 <= score <= 100


# ============================================================
# Complete Confidence Report
# ============================================================


def test_calculate_confidence_returns_complete_report():

    factors = [

        {

            "name":
                "Exact Formula Match",

            "impact":
                25,

            "reason":
                "Exact match.",

        },

        {

            "name":
                "Natural Family",

            "impact":
                10,

            "reason":
                "Natural family.",

        },

    ]

    result = calculate_confidence(

        factors

    )

    assert isinstance(

        result,

        dict

    )

    assert "Score" in result

    assert "Label" in result

    assert "Category Breakdown" in result

    assert "Factors" in result


def test_confidence_score_is_numeric():

    factors = [

        {

            "name":
                "Exact Formula Match",

            "impact":
                25,

            "reason":
                "Exact match.",

        }

    ]

    result = calculate_confidence(

        factors

    )

    assert isinstance(

        result["Score"],

        (

            int,

            float,

        ),

    )


def test_confidence_score_is_bounded():

    factors = [

        {

            "name":
                "Exact Formula Match",

            "impact":
                1000,

            "reason":
                "Very strong evidence.",

        }

    ]

    result = calculate_confidence(

        factors

    )

    assert 0 <= result["Score"] <= 100


# ============================================================
# Prediction Verification Evidence
# ============================================================


def test_verified_prediction_receives_full_bonus():

    report = MockReport(

        predicted_terms=[

            10,

            20,

        ],

        verified=True,

    )

    factor = prediction_verification_factor(

        report

    )

    assert factor["name"] == (

        "Prediction Verification"
    )

    assert factor["impact"] == 15


def test_unverified_prediction_receives_partial_bonus():

    report = MockReport(

        predicted_terms=[

            10,

            20,

        ],

        verified=False,

    )

    factor = prediction_verification_factor(

        report

    )

    assert factor["name"] == (

        "Prediction Generated"
    )

    assert factor["impact"] == 5


def test_no_predictions_receive_no_bonus():

    report = MockReport(

        predicted_terms=[],

        verified=False,

    )

    factor = prediction_verification_factor(

        report

    )

    assert factor["name"] == (

        "No Prediction Verification"
    )

    assert factor["impact"] == 0


# ============================================================
# Final Confidence Sanity Check
# ============================================================


def test_confidence_engine_is_usable():

    factors = [

        fit_factor(

            winner_error=0

        ),

        sample_size_factor(

            sequence_length=10

        ),

        complexity_factor(

            complexity=2

        ),

    ]

    result = calculate_confidence(

        factors

    )

    assert result is not None

    assert isinstance(

        result,

        dict

    )

    assert isinstance(

        result["Score"],

        int

    )

    assert 0 <= result["Score"] <= 100