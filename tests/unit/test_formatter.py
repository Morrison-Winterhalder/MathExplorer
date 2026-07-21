from analyzers.core.formatter import (
    build_polynomial_expression,
    clean_coefficients,
    yes_no,
    format_formula,
    format_recurrence,
    normalize_spacing,
    normalize_coefficients,
    normalize_signs,
    normalize_zero_terms,
    normalize_decimals,
    normalize_exponents,
    normalize_operator_spacing,
    format_monotonic,
)


# ==========================================================
# build_polynomial_expression()
# ==========================================================

def test_build_polynomial_quadratic():
    assert build_polynomial_expression([1, 2, 3]) == "1n^2 + 2n + 3"


def test_build_polynomial_linear():
    assert build_polynomial_expression([4, 5]) == "4n + 5"


def test_build_polynomial_constant():
    assert build_polynomial_expression([7]) == "7"


# ==========================================================
# clean_coefficients()
# ==========================================================

def test_clean_coefficients_small():
    assert clean_coefficients(
        [1e-12, 2, -1e-15]
    ) == [0, 2, 0]


def test_clean_coefficients_normal():
    assert clean_coefficients(
        [1, -2, 3]
    ) == [1, -2, 3]


# ==========================================================
# yes_no()
# ==========================================================

def test_yes():
    assert yes_no(True) == "Yes"


def test_no():
    assert yes_no(False) == "No"


def test_unknown():
    assert yes_no(None) == "Unknown"


# ==========================================================
# normalize_spacing()
# ==========================================================

def test_normalize_spacing():
    assert normalize_spacing("n=2") == "n = 2"


def test_normalize_spacing_multiple():
    assert normalize_spacing("a  =   b") == "a = b"


# ==========================================================
# normalize_coefficients()
# ==========================================================

def test_normalize_coefficients_positive():
    assert normalize_coefficients("1n+1") == "n+1"


def test_normalize_coefficients_negative():
    assert normalize_coefficients("-1n+1") == "-n+1"


# ==========================================================
# normalize_signs()
# ==========================================================

def test_normalize_signs():
    assert normalize_signs("n + -1") == "n - 1"


# ==========================================================
# normalize_zero_terms()
# ==========================================================

def test_remove_zero_power():
    assert normalize_zero_terms(
        "0n^2 + 3n + 1"
    ) == "3n + 1"


def test_remove_zero_linear():
    assert normalize_zero_terms(
        "0n + 5"
    ) == "5"


def test_remove_zero_constant():
    assert normalize_zero_terms(
        "3n + 0"
    ) == "3n"


# ==========================================================
# normalize_decimals()
# ==========================================================

def test_normalize_decimals():
    assert normalize_decimals("3.000") == "3"


# ==========================================================
# normalize_exponents()
# ==========================================================

def test_simple_exponent():
    assert normalize_exponents("n^2") == "n²"


def test_double_digit_exponent():
    assert normalize_exponents("n^10") == "n¹⁰"


def test_parenthesized_exponent():
    assert normalize_exponents("3^(n-1)") == "3⁽ⁿ⁻¹⁾"


# ==========================================================
# normalize_operator_spacing()
# ==========================================================

def test_binary_plus():
    assert normalize_operator_spacing("n+1") == "n + 1"


def test_binary_minus():
    assert normalize_operator_spacing("3n-1") == "3n - 1"


def test_multiple_operators():
    assert normalize_operator_spacing(
        "x+y-z"
    ) == "x + y - z"


def test_unary_minus():
    assert normalize_operator_spacing(
        "-n+1"
    ) == "-n + 1"


# ==========================================================
# format_formula()
# ==========================================================

def test_format_formula():
    assert format_formula(
        "1n^2+2n+3"
    ) == "a(n) = n² + 2n + 3"


def test_format_formula_zero_terms():
    assert format_formula(
        "0n^2+3n+0"
    ) == "a(n) = 3n"


# ==========================================================
# format_recurrence()
# ==========================================================

def test_format_recurrence():
    assert format_recurrence(
        "a(n-1)+a(n-2)"
    ) == "a(n) = a(n - 1) + a(n - 2)"


# ==========================================================
# format_monotonic()
# ==========================================================

class IncreasingFamily:
    MONOTONIC = True
    INCREASING = True


class DecreasingFamily:
    MONOTONIC = True
    DECREASING = True


class GenericFamily:
    MONOTONIC = True


class NonMonotonicFamily:
    MONOTONIC = False


def test_format_monotonic_increasing():
    assert format_monotonic(IncreasingFamily) == "Increasing"


def test_format_monotonic_decreasing():
    assert format_monotonic(DecreasingFamily) == "Decreasing"


def test_format_monotonic_yes():
    assert format_monotonic(GenericFamily) == "Yes"


def test_format_monotonic_no():
    assert format_monotonic(NonMonotonicFamily) == "No"