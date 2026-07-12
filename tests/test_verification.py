from analyzers.pipeline.verification import verify_sequence

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

# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": arithmetic,
            "Parameters": {"Difference": 2, "Intercept": -1}
        }
    }

    assert verify_sequence([1,3,5,7,9], report)


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": geometric,
            "Parameters": {"First Term": 2, "Ratio": 3}
        }
    }

    assert verify_sequence([2,6,18,54,162], report)


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": polynomial,
            "Parameters": [1,0,0]
        }
    }

    assert verify_sequence([1,4,9,16,25], report)


# ==========================================================
# Constant
# ==========================================================

def test_constant_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": constant,
            "Parameters": {"Value": 7}
        }
    }

    assert verify_sequence([7,7,7,7], report)


# ==========================================================
# Triangular
# ==========================================================

def test_triangular_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": triangular,
            "Parameters": {}
        }
    }

    assert verify_sequence([1,3,6,10,15], report)


# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": pentagonal,
            "Parameters": {}
        }
    }

    assert verify_sequence([1,5,12,22,35], report)

# ==========================================================
# Centered Square
# ==========================================================

def test_centered_square_verification():

    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": centered_square,
            "Parameters": {}
        }
    }

    assert verify_sequence(
        [1,5,13,25,41],
        report
    )

# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": fibonacci,
            "Parameters": {
                "Seeds":[1,1],
                "RecurrenceCoefficients":[1,1]
            }
        }
    }

    assert verify_sequence([1,1,2,3,5], report)


# ==========================================================
# Lucas
# ==========================================================

def test_lucas_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": lucas,
            "Parameters": {
                "Seeds":[2,1],
                "RecurrenceCoefficients":[1,1]
            }
        }
    }

    assert verify_sequence([2,1,3,4,7], report)


# ==========================================================
# Pell
# ==========================================================

def test_pell_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": pell,
            "Parameters": {
                "Seeds":[0,1],
                "RecurrenceCoefficients":[2,1]
            }
        }
    }

    assert verify_sequence([0,1,2,5,12], report)


# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": jacobsthal,
            "Parameters": {
                "Seeds":[0,1],
                "RecurrenceCoefficients":[1,2]
            }
        }
    }

    assert verify_sequence([0,1,1,3,5], report)

# ==========================================================
# Tribonacci
# ==========================================================

def test_tribonacci_verification():

    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": tribonacci,
            "Parameters": {
                "Seeds": [0,0,1],
                "RecurrenceCoefficients": [1,1,1]
            }
        }
    }

    assert verify_sequence(
        [0,0,1,1,2,4,7],
        report
    )

# ==========================================================
# Factorial
# ==========================================================

def test_factorial_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": factorial,
            "Parameters": {}
        }
    }

    assert verify_sequence([1,2,6,24,120], report)


# ==========================================================
# Incorrect Parameters
# ==========================================================

def test_failed_verification():
    report = {
        "Analysis Trace": [],
        "Sequence Classification": {
            "Family": arithmetic,
            "Parameters": {"Difference": 3, "Intercept": -2}
        }
    }

    assert not verify_sequence([1,3,5,7,9], report)