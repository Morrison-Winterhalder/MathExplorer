from analyzers.confidence_engine.formatter import (
    confidence_label,
)


# ==========================================================
# Basic Labels
# ==========================================================

def test_confidence_label_very_high():

    assert confidence_label(95) == "Very High"


def test_confidence_label_high():

    assert confidence_label(80) == "High"


def test_confidence_label_moderate():

    assert confidence_label(65) == "Moderate"


def test_confidence_label_low():

    assert confidence_label(45) == "Low"


def test_confidence_label_very_low():

    assert confidence_label(20) == "Very Low"



# ==========================================================
# Boundary Tests
# ==========================================================

def test_confidence_label_boundary_90():

    assert confidence_label(90) == "Very High"


def test_confidence_label_boundary_75():

    assert confidence_label(75) == "High"


def test_confidence_label_boundary_60():

    assert confidence_label(60) == "Moderate"


def test_confidence_label_boundary_40():

    assert confidence_label(40) == "Low"



# ==========================================================
# Edge Cases
# ==========================================================

def test_confidence_label_zero():

    assert confidence_label(0) == "Very Low"


def test_confidence_label_full_score():

    assert confidence_label(100) == "Very High"


def test_confidence_label_negative():

    assert confidence_label(-10) == "Very Low"