from analyzers.pipeline.prediction import predict_terms
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

def test_arithmetic_prediction():

    analysis = make_analysis(
        arithmetic,
        {
            "Difference": 2,
            "Intercept": -1
        }
    )

    assert predict_terms(
        [1,3,5,7,9],
        analysis
    ) == [11,13,15,17,19]


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_prediction():

    analysis = make_analysis(
        geometric,
        {
            "First Term": 2,
            "Ratio": 3
        }
    )

    assert predict_terms(
        [2,6,18,54,162],
        analysis
    ) == [486,1458,4374,13122,39366]


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_prediction():

    analysis = make_analysis(
        polynomial,
        [1,0,0]
    )

    assert predict_terms(
        [1,4,9,16,25],
        analysis
    ) == [36,49,64,81,100]


# ==========================================================
# Constant
# ==========================================================

def test_constant_prediction():

    analysis = make_analysis(
        constant,
        {
            "Value": 7
        }
    )

    assert predict_terms(
        [7,7,7,7],
        analysis
    ) == [7,7,7,7,7]


# ==========================================================
# Triangular
# ==========================================================

def test_triangular_prediction():

    analysis = make_analysis(
        triangular,
        {}
    )

    assert predict_terms(
        [1,3,6,10,15],
        analysis
    ) == [21,28,36,45,55]


# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_prediction():

    analysis = make_analysis(
        pentagonal,
        {}
    )

    assert predict_terms(
        [1,5,12,22,35],
        analysis
    ) == [51,70,92,117,145]

# ==========================================================
# Centered Square
# ==========================================================

def test_centered_square_prediction():

    analysis = make_analysis(
        centered_square,
        {}
    )

    assert predict_terms(
        [1,5,13,25,41],
        analysis
    ) == [61,85,113,145,181]

# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_prediction():

    analysis = make_analysis(
        fibonacci,
        {
            "Seeds":[1,1],
            "RecurrenceCoefficients":[1,1]
        }
    )

    assert predict_terms(
        [1,1,2,3,5],
        analysis
    ) == [8,13,21,34,55]


# ==========================================================
# Lucas
# ==========================================================

def test_lucas_prediction():

    analysis = make_analysis(
        lucas,
        {
            "Seeds":[2,1],
            "RecurrenceCoefficients":[1,1]
        }
    )

    assert predict_terms(
        [2,1,3,4,7],
        analysis
    ) == [11,18,29,47,76]


# ==========================================================
# Pell
# ==========================================================

def test_pell_prediction():

    analysis = make_analysis(
        pell,
        {
            "Seeds":[0,1],
            "RecurrenceCoefficients":[2,1]
        }
    )

    assert predict_terms(
        [0,1,2,5,12],
        analysis
    ) == [29,70,169,408,985]


# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_prediction():

    analysis = make_analysis(
        jacobsthal,
        {
            "Seeds":[0,1],
            "RecurrenceCoefficients":[1,2]
        }
    )

    assert predict_terms(
        [0,1,1,3,5],
        analysis
    ) == [11,21,43,85,171]

# ==========================================================
# Tribonacci
# ==========================================================

def test_tribonacci_prediction():

    analysis = make_analysis(
        tribonacci,
        {
            "Seeds":[0,0,1],
            "RecurrenceCoefficients":[1,1,1]
        }
    )

    assert predict_terms(
        [0,0,1,1,2,4,7],
        analysis
    ) == [13,24,44,81,149]


# ==========================================================
# Tetranacci
# ==========================================================

def test_tetranacci_prediction():

    analysis = make_analysis(
        tetranacci,
        {
            "Seeds":[0,0,0,1],
            "RecurrenceCoefficients":[1,1,1,1]
        }
    )

    assert predict_terms(
        [0,0,0,1,1,2,4],
        analysis
    ) == [8,15,29,56,108]


# ==========================================================
# Padovan
# ==========================================================

def test_padovan_prediction():

    analysis = make_analysis(
        padovan,
        {
            "Seeds":[1,1,1],
            "RecurrenceCoefficients":[0,1,1]
        }
    )

    assert predict_terms(
        [1,1,1,2,2],
        analysis
    ) == [3,4,5,7,9]


# ==========================================================
# Perrin
# ==========================================================

def test_perrin_prediction():

    analysis = make_analysis(
        perrin,
        {
            "Seeds":[3,0,2],
            "RecurrenceCoefficients":[0,1,1]
        }
    )

    assert predict_terms(
        [3,0,2,3,2],
        analysis
    ) == [5,5,7,10,12]

# ==========================================================
# Factorial
# ==========================================================

def test_factorial_prediction():

    analysis = make_analysis(
        factorial,
        {}
    )

    assert predict_terms(
        [1,2,6,24,120],
        analysis
    ) == [720,5040,40320,362880,3628800]


# ==========================================================
# Unknown Family
# ==========================================================

def test_unknown_prediction():

    analysis = make_analysis(
        None,
        None
    )

    assert predict_terms(
        [1,2,3],
        analysis
    ) == []