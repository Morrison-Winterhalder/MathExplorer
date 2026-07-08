from analyzers.pipeline.recovery import recover_formula
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

def test_arithmetic_recovery():
    report = {
        "Sequence Classification": {
            "Family": arithmetic,
            "Parameters": {
                "Difference": 2,
                "Intercept": -1
            }
        }
    }

    recover_formula([1,3,5,7,9], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = 2n - 1"


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_recovery():
    report = {
        "Sequence Classification": {
            "Family": geometric,
            "Parameters": {
                "First Term": 2,
                "Ratio": 3
            }
        }
    }

    recover_formula([2,6,18,54,162], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = 2 · 3^(n-1)"


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_recovery():
    report = {
        "Sequence Classification": {
            "Family": polynomial,
            "Parameters": [1,0,0]
        }
    }

    recover_formula([1,4,9,16,25], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = n^2"


# ==========================================================
# Constant
# ==========================================================

def test_constant_recovery():
    report = {
        "Sequence Classification": {
            "Family": constant,
            "Parameters": {
                "Value": 7
            }
        }
    }

    recover_formula([7,7,7,7], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = 7"


# ==========================================================
# Triangular
# ==========================================================

def test_triangular_recovery():
    report = {
        "Sequence Classification": {
            "Family": triangular,
            "Parameters": {}
        }
    }

    recover_formula([1,3,6,10,15], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = n(n+1)/2"


# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_recovery():
    report = {
        "Sequence Classification": {
            "Family": pentagonal,
            "Parameters": {}
        }
    }

    recover_formula([1,5,12,22,35], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = n(3n-1)/2"


# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_recovery():
    report = {
        "Sequence Classification": {
            "Family": fibonacci,
            "Parameters": {}
        }
    }

    recover_formula([1,1,2,3,5], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = a(n-1) + a(n-2)"


# ==========================================================
# Lucas
# ==========================================================

def test_lucas_recovery():
    report = {
        "Sequence Classification": {
            "Family": lucas,
            "Parameters": {}
        }
    }

    recover_formula([2,1,3,4,7], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = a(n-1) + a(n-2)"


# ==========================================================
# Pell
# ==========================================================

def test_pell_recovery():
    report = {
        "Sequence Classification": {
            "Family": pell,
            "Parameters": {}
        }
    }

    recover_formula([0,1,2,5,12], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = 2a(n-1) + a(n-2)"


# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_recovery():
    report = {
        "Sequence Classification": {
            "Family": jacobsthal,
            "Parameters": {}
        }
    }

    recover_formula([0,1,1,3,5], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = a(n-1) + 2a(n-2)"


# ==========================================================
# Factorial
# ==========================================================

def test_factorial_recovery():
    report = {
        "Sequence Classification": {
            "Family": factorial,
            "Parameters": {}
        }
    }

    recover_formula([1,2,6,24,120], report)

    assert report["Sequence Classification"]["Formula"] == "a(n) = n!"


# ==========================================================
# Dispatcher
# ==========================================================

def test_unknown_family_recovery():
    report = {
        "Sequence Classification": {
            "Family": None,
            "Parameters": None
        }
    }

    recover_formula([1,2,3], report)

    assert "Formula" not in report["Sequence Classification"]