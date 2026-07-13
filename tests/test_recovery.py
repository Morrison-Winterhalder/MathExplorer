from analyzers.pipeline.recovery import recover_formula
from analyzers.core.analysis import SequenceAnalysis

from families import (
    arithmetic,
    geometric,
    polynomial,
    constant,
    triangular,
    pentagonal,
    centered_square,
    fibonacci,
    lucas,
    pell,
    jacobsthal,
    tribonacci,
    tetranacci,
    padovan,
    perrin,
    factorial
)


def make_analysis(family, parameters):
    analysis = SequenceAnalysis([])

    analysis.classification = {
        "Family": family,
        "Parameters": parameters
    }

    return analysis


# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_recovery():

    analysis = make_analysis(
        arithmetic,
        {
            "Difference": 2,
            "Intercept": -1
        }
    )

    recover_formula([1,3,5,7,9], analysis)

    assert analysis.formula is not None


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_recovery():

    analysis = make_analysis(
        geometric,
        {
            "First Term": 2,
            "Ratio": 3
        }
    )

    recover_formula([2,6,18,54,162], analysis)

    assert analysis.formula is not None


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_recovery():

    analysis = make_analysis(
        polynomial,
        [1,0,0]
    )

    recover_formula([1,4,9,16,25], analysis)

    assert analysis.formula is not None


# ==========================================================
# Constant
# ==========================================================

def test_constant_recovery():

    analysis = make_analysis(
        constant,
        {
            "Value": 7
        }
    )

    recover_formula([7,7,7,7], analysis)

    assert analysis.formula is not None


# ==========================================================
# Figurate Families
# ==========================================================

def test_triangular_recovery():

    analysis = make_analysis(
        triangular,
        {}
    )

    recover_formula([1,3,6,10,15], analysis)

    assert analysis.formula is not None


def test_pentagonal_recovery():

    analysis = make_analysis(
        pentagonal,
        {}
    )

    recover_formula([1,5,12,22,35], analysis)

    assert analysis.formula is not None


def test_centered_square_recovery():

    analysis = make_analysis(
        centered_square,
        {}
    )

    recover_formula([1,5,13,25,41], analysis)

    assert analysis.formula is not None


# ==========================================================
# Recurrence Families
# ==========================================================

def test_fibonacci_recovery():

    analysis = make_analysis(
        fibonacci,
        {
            "Seeds":[1,1],
            "RecurrenceCoefficients":[1,1]
        }
    )

    recover_formula([1,1,2,3,5], analysis)

    assert analysis.formula is not None


def test_lucas_recovery():

    analysis = make_analysis(
        lucas,
        {
            "Seeds":[2,1],
            "RecurrenceCoefficients":[1,1]
        }
    )

    recover_formula([2,1,3,4,7], analysis)

    assert analysis.formula is not None


def test_pell_recovery():

    analysis = make_analysis(
        pell,
        {
            "Seeds":[0,1],
            "RecurrenceCoefficients":[2,1]
        }
    )

    recover_formula([0,1,2,5,12], analysis)

    assert analysis.formula is not None


def test_jacobsthal_recovery():

    analysis = make_analysis(
        jacobsthal,
        {
            "Seeds":[0,1],
            "RecurrenceCoefficients":[1,2]
        }
    )

    recover_formula([0,1,1,3,5], analysis)

    assert analysis.formula is not None


def test_tribonacci_recovery():

    analysis = make_analysis(
        tribonacci,
        {
            "Seeds":[0,0,1],
            "RecurrenceCoefficients":[1,1,1]
        }
    )

    recover_formula([0,0,1,1,2,4,7], analysis)

    assert analysis.formula is not None


def test_tetranacci_recovery():

    analysis = make_analysis(
        tetranacci,
        {
            "Seeds":[0,0,0,1],
            "RecurrenceCoefficients":[1,1,1,1]
        }
    )

    recover_formula([0,0,0,1,1,2,4], analysis)

    assert analysis.formula is not None


def test_padovan_recovery():

    analysis = make_analysis(
        padovan,
        {
            "Seeds":[1,1,1],
            "RecurrenceCoefficients":[0,1,1]
        }
    )

    recover_formula([1,1,1,2,2], analysis)

    assert analysis.formula is not None


def test_perrin_recovery():

    analysis = make_analysis(
        perrin,
        {
            "Seeds":[3,0,2],
            "RecurrenceCoefficients":[0,1,1]
        }
    )

    recover_formula([3,0,2,3,2], analysis)

    assert analysis.formula is not None


# ==========================================================
# Factorial
# ==========================================================

def test_factorial_recovery():

    analysis = make_analysis(
        factorial,
        {}
    )

    recover_formula([1,2,6,24,120], analysis)

    assert analysis.formula is not None


# ==========================================================
# Edge Cases
# ==========================================================

def test_unknown_family_recovery():

    analysis = make_analysis(
        None,
        None
    )

    recover_formula([1,2,3], analysis)

    assert analysis.formula is None


def test_recovery_handles_missing_parameters():

    analysis = make_analysis(
        arithmetic,
        None
    )

    recover_formula([1,3,5,7], analysis)

    assert analysis.formula is None