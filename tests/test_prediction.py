from analyzers.pipeline.prediction import predict_terms

from families import (
    arithmetic,
    geometric,
    polynomial,
    constant,
    triangular,
    pentagonal,
    fibonacci,
    lucas,
    pell,
    jacobsthal,
    factorial
)

# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_prediction():
    report = {
        "Sequence Classification": {
            "Family": arithmetic,
            "Parameters": {
                "Difference": 2,
                "Intercept": -1
            }
        }
    }

    assert predict_terms([1,3,5,7,9], report) == [11,13,15,17,19]


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_prediction():
    report = {
        "Sequence Classification": {
            "Family": geometric,
            "Parameters": {
                "First Term": 2,
                "Ratio": 3
            }
        }
    }

    assert predict_terms([2,6,18,54,162], report) == [486,1458,4374,13122,39366]


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_prediction():
    report = {
        "Sequence Classification": {
            "Family": polynomial,
            "Parameters": [1,0,0]
        }
    }

    assert predict_terms([1,4,9,16,25], report) == [36,49,64,81,100]


# ==========================================================
# Constant
# ==========================================================

def test_constant_prediction():
    report = {
        "Sequence Classification": {
            "Family": constant,
            "Parameters": {
                "Value": 7
            }
        }
    }

    assert predict_terms([7,7,7,7], report) == [7,7,7,7,7]


# ==========================================================
# Triangular
# ==========================================================

def test_triangular_prediction():
    report = {
        "Sequence Classification": {
            "Family": triangular,
            "Parameters": {}
        }
    }

    assert predict_terms([1,3,6,10,15], report) == [21,28,36,45,55]


# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_prediction():
    report = {
        "Sequence Classification": {
            "Family": pentagonal,
            "Parameters": {}
        }
    }

    assert predict_terms([1,5,12,22,35], report) == [51,70,92,117,145]


# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_prediction():
    report = {
        "Sequence Classification": {
            "Family": fibonacci,
            "Parameters": {
                "Seeds":[1,1],
                "RecurrenceCoefficients":[1,1]
            }
        }
    }

    assert predict_terms([1,1,2,3,5], report) == [8,13,21,34,55]


# ==========================================================
# Lucas
# ==========================================================

def test_lucas_prediction():
    report = {
        "Sequence Classification": {
            "Family": lucas,
            "Parameters": {
                "Seeds":[2,1],
                "RecurrenceCoefficients":[1,1]
            }
        }
    }

    assert predict_terms([2,1,3,4,7], report) == [11,18,29,47,76]


# ==========================================================
# Pell
# ==========================================================

def test_pell_prediction():
    report = {
        "Sequence Classification": {
            "Family": pell,
            "Parameters": {
                "Seeds":[0,1],
                "RecurrenceCoefficients":[2,1]
            }
        }
    }

    assert predict_terms([0,1,2,5,12], report) == [29,70,169,408,985]


# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_prediction():
    report = {
        "Sequence Classification": {
            "Family": jacobsthal,
            "Parameters": {
                "Seeds":[0,1],
                "RecurrenceCoefficients":[1,2]
            }
        }
    }

    assert predict_terms([0,1,1,3,5], report) == [11,21,43,85,171]


# ==========================================================
# Factorial
# ==========================================================

def test_factorial_prediction():
    report = {
        "Sequence Classification": {
            "Family": factorial,
            "Parameters": {}
        }
    }

    assert predict_terms([1,2,6,24,120], report) == [720,5040,40320,362880,3628800]


# ==========================================================
# Unknown Family
# ==========================================================

def test_unknown_prediction():
    report = {
        "Sequence Classification": {
            "Family": None,
            "Parameters": None
        }
    }

    assert predict_terms([1,2,3], report) == []