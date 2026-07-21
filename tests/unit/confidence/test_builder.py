from analyzers.confidence_engine.builder import (
    build_confidence,
    build_summary,
)


# ==========================================================
# build_confidence()
# ==========================================================

def test_build_confidence_very_high_label():

    confidence = {
        "Score": 95
    }

    result = build_confidence(confidence)

    assert result["Label"] == "Very High"


def test_build_confidence_high_label():

    confidence = {
        "Score": 80
    }

    result = build_confidence(confidence)

    assert result["Label"] == "High"


def test_build_confidence_moderate_label():

    confidence = {
        "Score": 50
    }

    result = build_confidence(confidence)

    assert result["Label"] == "Moderate"


def test_build_confidence_low_label():

    confidence = {
        "Score": 20
    }

    result = build_confidence(confidence)

    assert result["Label"] == "Low"


def test_build_confidence_boundary_90():

    confidence = {
        "Score": 90
    }

    result = build_confidence(confidence)

    assert result["Label"] == "Very High"


def test_build_confidence_boundary_70():

    confidence = {
        "Score": 70
    }

    result = build_confidence(confidence)

    assert result["Label"] == "High"


def test_build_confidence_boundary_40():

    confidence = {
        "Score": 40
    }

    result = build_confidence(confidence)

    assert result["Label"] == "Moderate"


def test_build_confidence_adds_reasoning():

    confidence = {
        "Score": 95
    }

    result = build_confidence(confidence)

    # build_reasoning should add explanation fields
    assert len(result) > 1



def test_build_confidence_returns_same_dictionary():

    confidence = {
        "Score": 80
    }

    result = build_confidence(confidence)

    assert result is confidence



# ==========================================================
# build_summary()
# ==========================================================

def test_build_summary_with_strengths():

    confidence = {
        "Label": "High"
    }

    strengths = [
        {
            "Reason": "The formula exactly matches."
        }
    ]

    limitations = []

    result = build_summary(
        confidence,
        strengths,
        limitations
    )

    assert (
        result
        ==
        "Confidence is high because "
        "The formula exactly matches."
    )



def test_build_summary_with_limitation():

    confidence = {
        "Label": "High"
    }

    strengths = [
        {
            "Reason": "The formula exactly matches."
        }
    ]

    limitations = [
        {
            "Reason": "Additional terms are needed."
        }
    ]

    result = build_summary(
        confidence,
        strengths,
        limitations
    )

    assert (
        result
        ==
        "Confidence is high because "
        "The formula exactly matches. "
        "However, additional terms are needed."
    )



def test_build_summary_without_strengths():

    confidence = {
        "Label": "Low"
    }

    strengths = []

    limitations = []

    result = build_summary(
        confidence,
        strengths,
        limitations
    )

    assert (
        result
        ==
        "Confidence is low because "
        "limited supporting evidence is currently available."
    )



def test_build_summary_strength_and_limitation_priority():

    confidence = {
        "Label": "Moderate"
    }

    strengths = [
        {
            "Reason": "Many terms agree."
        },
        {
            "Reason": "Strong fit."
        }
    ]

    limitations = [
        {
            "Reason": "The sample is small."
        }
    ]

    result = build_summary(
        confidence,
        strengths,
        limitations
    )

    assert result.startswith(
        "Confidence is moderate because Many terms agree."
    )

    assert (
        "However, the sample is small."
        in result
    )