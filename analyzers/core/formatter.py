from analyzers.core.utilities import pretty
import re


def build_polynomial_expression(coefficients):
    terms = []

    for i, coefficient in enumerate(coefficients):

        power = len(coefficients) - 1 - i

        if power == 0:
            terms.append(f"{pretty(coefficient)}")

        elif power == 1:
            terms.append(f"{pretty(coefficient)}n")

        else:
            terms.append(
                f"{pretty(coefficient)}n^{power}"
            )

    return " + ".join(terms)

def clean_coefficients(coefficients, tol=1e-10):
    return [
        0 if abs(c) < tol else c
        for c in coefficients
    ]

def yes_no(value):
    if value is True:
        return "Yes"
    elif value is False:
        return "No"
    else:
        return "Unknown"
    
# ==========================================================
# Formula Formatting
# ==========================================================

def format_formula(formula):
    """
    Apply all formatting passes to a symbolic formula.
    """

    formula = normalize_spacing(formula)
    formula = normalize_coefficients(formula)
    formula = normalize_signs(formula)
    formula = normalize_zero_terms(formula)

    return formula

def normalize_spacing(formula):

    formula = formula.replace("=", " = ")

    while "  " in formula:
        formula = formula.replace("  ", " ")

    return formula.strip()

def normalize_coefficients(formula):

    formula = formula.replace("-1n", "-n")
    formula = formula.replace("1n", "n")

    return formula

def normalize_signs(formula):

    formula = formula.replace("+ -", "- ")

    return formula

def normalize_zero_terms(formula):
    """
    Remove polynomial terms with zero coefficients.
    """

    formula = re.sub(r"\b0n\^\d+\s*\+\s*", "", formula)
    formula = re.sub(r"\b0n\s*\+\s*", "", formula)
    formula = re.sub(r"\+\s*0\b", "", formula)

    return formula.strip()

def normalize_decimals(formula):
    """
    Remove trailing zeros from decimal numbers.
    """

    # Currently unused.
    # Numeric formatting is handled by pretty().
    # Reserved for future formatter extensions.

    return re.sub(
        r"(-?\d+)\.0+\b",
        r"\1",
        formula,
    )