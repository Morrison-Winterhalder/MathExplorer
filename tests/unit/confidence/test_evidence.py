from analyzers.confidence_engine.evidence import (
    EVIDENCE_CATEGORIES,
)


# ==========================================================
# Structure Tests
# ==========================================================

def test_evidence_categories_exist():

    assert isinstance(
        EVIDENCE_CATEGORIES,
        dict
    )


def test_expected_categories_exist():

    assert set(
        EVIDENCE_CATEGORIES.keys()
    ) == {
        "Mathematical",
        "Structural",
        "Competitive",
        "Reliability",
    }



def test_all_categories_are_lists():

    for category, evidence in EVIDENCE_CATEGORIES.items():

        assert isinstance(
            evidence,
            list
        )


def test_no_empty_categories():

    for category, evidence in EVIDENCE_CATEGORIES.items():

        assert len(evidence) > 0



# ==========================================================
# Mathematical Category
# ==========================================================

def test_mathematical_evidence():

    assert EVIDENCE_CATEGORIES["Mathematical"] == [
        "Exact Formula Match",
        "Formula Accuracy",
        "Observed Evidence",
        "Prediction Verification",
    ]



# ==========================================================
# Structural Category
# ==========================================================

def test_structural_evidence():

    assert EVIDENCE_CATEGORIES["Structural"] == [
        "Hierarchy Consistency",
        "Root Family",
        "Related Family Support",
        "Natural Family",
    ]



# ==========================================================
# Competitive Category
# ==========================================================

def test_competitive_evidence():

    assert EVIDENCE_CATEGORIES["Competitive"] == [
        "No Competition",
        "Family Separation",
        "Competing Explanation",
    ]



# ==========================================================
# Reliability Category
# ==========================================================

def test_reliability_evidence():

    assert EVIDENCE_CATEGORIES["Reliability"] == [
        "Large Evidence Sample",
        "Adequate Evidence Sample",
        "Limited Evidence Sample",
        "Simple Explanation",
        "Complex Explanation",
    ]



# ==========================================================
# Uniqueness Tests
# ==========================================================

def test_all_evidence_names_are_unique():

    evidence = []

    for category in EVIDENCE_CATEGORIES.values():
        evidence.extend(category)

    assert len(evidence) == len(set(evidence))