from analyzers.confidence_engine.scorer import (
    calculate_confidence,
    categorize_factor,
    calculate_weighted_score,
)


# ==========================================================
# categorize_factor()
# ==========================================================

def test_categorize_mathematical_factor():

    factor = {
        "name": "Exact Formula Match",
        "impact": 25,
    }

    assert categorize_factor(factor) == "Mathematical"



def test_categorize_structural_factor():

    factor = {
        "name": "Hierarchy Consistency",
        "impact": 8,
    }

    assert categorize_factor(factor) == "Structural"



def test_categorize_competitive_factor():

    factor = {
        "name": "Family Separation",
        "impact": 5,
    }

    assert categorize_factor(factor) == "Competitive"



def test_categorize_unknown_defaults_reliability():

    factor = {
        "name": "Unknown Evidence",
        "impact": 1,
    }

    assert categorize_factor(factor) == "Reliability"



# ==========================================================
# calculate_weighted_score()
# ==========================================================

def test_weighted_score_with_no_factors():

    result = calculate_weighted_score([])

    # Weighted baselines:
    # Mathematical 50*.35
    # Structural 50*.30
    # Competitive 70*.20
    # Reliability 65*.15

    expected = (
        50 * 0.35
        +
        50 * 0.30
        +
        70 * 0.20
        +
        65 * 0.15
    )

    assert result["Score"] == round(expected)



def test_weighted_score_exact_formula():

    factors = [
        {
            "name": "Exact Formula Match",
            "impact": 25,
        }
    ]

    result = calculate_weighted_score(
        factors
    )

    assert (
        result["Category Breakdown"]
        ["Mathematical"]
        ==
        75
    )



def test_weighted_score_caps_category_at_100():

    factors = [
        {
            "name": "Exact Formula Match",
            "impact": 1000,
        }
    ]

    result = calculate_weighted_score(
        factors
    )

    assert (
        result["Category Breakdown"]
        ["Mathematical"]
        ==
        100
    )



def test_weighted_score_floors_category_at_zero():

    factors = [
        {
            "name": "Formula Accuracy",
            "impact": -1000,
        }
    ]

    result = calculate_weighted_score(
        factors
    )

    assert (
        result["Category Breakdown"]
        ["Mathematical"]
        ==
        0
    )



def test_multiple_factors_same_category():

    factors = [
        {
            "name": "Exact Formula Match",
            "impact": 25,
        },
        {
            "name": "Observed Evidence",
            "impact": 8,
        },
    ]

    result = calculate_weighted_score(
        factors
    )

    assert (
        result["Category Breakdown"]
        ["Mathematical"]
        ==
        83
    )



# ==========================================================
# Category Breakdown
# ==========================================================

def test_all_categories_present():

    result = calculate_weighted_score([])

    assert set(
        result["Category Breakdown"].keys()
    ) == {
        "Mathematical",
        "Structural",
        "Competitive",
        "Reliability",
    }



# ==========================================================
# calculate_confidence()
# ==========================================================

def test_calculate_confidence_structure():

    factors = [
        {
            "name": "Exact Formula Match",
            "impact": 25,
        }
    ]

    result = calculate_confidence(
        factors
    )

    assert "Score" in result
    assert "Label" in result
    assert "Category Breakdown" in result
    assert "Factors" in result



def test_calculate_confidence_preserves_factors():

    factors = [
        {
            "name": "Natural Family",
            "impact": 10,
        }
    ]

    result = calculate_confidence(
        factors
    )

    assert result["Factors"] == factors



def test_calculate_confidence_label_matches_score():

    factors = []

    result = calculate_confidence(
        factors
    )

    score = result["Score"]

    if score >= 90:
        expected = "Very High"

    elif score >= 75:
        expected = "High"

    elif score >= 60:
        expected = "Moderate"

    elif score >= 40:
        expected = "Low"

    else:
        expected = "Very Low"

    assert result["Label"] == expected