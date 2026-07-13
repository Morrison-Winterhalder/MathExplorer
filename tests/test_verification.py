from analyzers.pipeline.verification import verify_sequence
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

def test_arithmetic_verification():
    analysis = make_analysis(
        arithmetic,
        {"Difference": 2, "Intercept": -1}
    )

    assert verify_sequence(
        [1,3,5,7,9],
        analysis
    )


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_verification():
    analysis = make_analysis(
        geometric,
        {"First Term": 2, "Ratio": 3}
    )

    assert verify_sequence(
        [2,6,18,54,162],
        analysis
    )


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_verification():
    analysis = make_analysis(
        polynomial,
        [1,0,0]
    )

    assert verify_sequence(
        [1,4,9,16,25],
        analysis
    )


# ==========================================================
# Constant
# ==========================================================

def test_constant_verification():
    analysis = make_analysis(
        constant,
        {"Value": 7}
    )

    assert verify_sequence(
        [7,7,7,7],
        analysis
    )


# ==========================================================
# Triangular
# ==========================================================

def test_triangular_verification():
    analysis = make_analysis(
        triangular,
        {}
    )

    assert verify_sequence(
        [1,3,6,10,15],
        analysis
    )


# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_verification():
    analysis = make_analysis(
        pentagonal,
        {}
    )

    assert verify_sequence(
        [1,5,12,22,35],
        analysis
    )

# ==========================================================
# Centered Square
# ==========================================================

def test_centered_square_verification():
    analysis = make_analysis(
        centered_square,
        {}
    )

    assert verify_sequence(
        [1,5,13,25,41],
        analysis
    )

# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_verification():
    analysis = make_analysis(
        fibonacci,
        {
            "Seeds":[1,1],
            "RecurrenceCoefficients":[1,1]
        }
    )

    assert verify_sequence(
        [1,1,2,3,5],
        analysis
    )


# ==========================================================
# Lucas
# ==========================================================

def test_lucas_verification():
    analysis = make_analysis(
        lucas,
        {
            "Seeds":[2,1],
            "RecurrenceCoefficients":[1,1]
        }
    )

    assert verify_sequence(
        [2,1,3,4,7],
        analysis
    )


# ==========================================================
# Pell
# ==========================================================

def test_pell_verification():
    analysis = make_analysis(
        pell,
        {
            "Seeds":[0,1],
            "RecurrenceCoefficients":[2,1]
        }
    )

    assert verify_sequence(
        [0,1,2,5,12],
        analysis
    )


# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_verification():
    analysis = make_analysis(
        jacobsthal,
        {
            "Seeds":[0,1],
            "RecurrenceCoefficients":[1,2]
        }
    )

    assert verify_sequence(
        [0,1,1,3,5],
        analysis
    )

# ==========================================================
# Tribonacci
# ==========================================================

def test_tribonacci_verification():
    analysis = make_analysis(
        tribonacci,
        {
            "Seeds":[0,0,1],
            "RecurrenceCoefficients":[1,1,1]
        }
    )

    assert verify_sequence(
        [0,0,1,1,2,4,7],
        analysis
    )

# ==========================================================
# Factorial
# ==========================================================

def test_factorial_verification():
    analysis = make_analysis(
        factorial,
        {}
    )

    assert verify_sequence(
        [1,2,6,24,120],
        analysis
    )


# ==========================================================
# Incorrect Parameters
# ==========================================================

def test_failed_verification():
    analysis = make_analysis(
        arithmetic,
        {
            "Difference":3,
            "Intercept":-2
        }
    )

    assert not verify_sequence(
        [1,3,5,7,9],
        analysis
    )