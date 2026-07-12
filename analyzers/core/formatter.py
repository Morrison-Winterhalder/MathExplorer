from analyzers.core.utilities import pretty
import re

SUPERSCRIPTS = str.maketrans({
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "+": "⁺",
    "-": "⁻",
    "=": "⁼",
    "(": "⁽",
    ")": "⁾",
    "n": "ⁿ",
})


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

def format_formula(expression):
    """
    Apply all formatting passes to a symbolic formula.
    """

    expression = normalize_spacing(expression)
    expression = normalize_zero_terms(expression)
    expression = normalize_coefficients(expression)
    expression = normalize_signs(expression)
    expression = normalize_operator_spacing(expression)
    expression = normalize_exponents(expression)

    return f"a(n) = {expression}"

def format_recurrence(recurrence):

    recurrence = normalize_spacing(recurrence)
    recurrence = normalize_operator_spacing(recurrence)
    recurrence = normalize_exponents(recurrence)

    return f"a(n) = {recurrence}"

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

def normalize_exponents(expression):
    """
    Convert caret exponents into Unicode superscripts.

    Examples:
        n^2        -> n²
        n^10       -> n¹⁰
        3^(n-1)    -> 3⁽ⁿ⁻¹⁾
    """

    result = []
    i = 0

    while i < len(expression):

        if expression[i] != "^":
            result.append(expression[i])
            i += 1
            continue

        # Skip the caret
        i += 1

        # Parenthesized exponent
        if i < len(expression) and expression[i] == "(":

            depth = 1
            start = i
            i += 1

            while i < len(expression) and depth:

                if expression[i] == "(":
                    depth += 1
                elif expression[i] == ")":
                    depth -= 1

                i += 1

            
            exponent = expression[start:i]
            exponent = exponent.replace(" ", "")    
            result.append(exponent.translate(SUPERSCRIPTS))

        # Simple exponent
        else:

            start = i

            while (
                i < len(expression)
                and expression[i].isalnum()
            ):
                i += 1

            exponent = expression[start:i]
            result.append(exponent.translate(SUPERSCRIPTS))

    return "".join(result)

def normalize_operator_spacing(expression):
    """
    Add spaces around binary + and - operators.

    Examples:
        n+1      -> n + 1
        3n-1     -> 3n - 1
        x+y-z    -> x + y - z

    Leaves unary minus untouched:
        -n
        -3
        3⁽ⁿ⁻¹⁾
    """

    # Binary +
    expression = re.sub(
        r'(?<=[\w\)])\+(?=[\w\(])',
        ' + ',
        expression
    )

    # Binary -
    expression = re.sub(
        r'(?<=[\w\)])-(?=[\w\(])',
        ' - ',
        expression
    )

    return expression

def format_monotonic(family):

    if not family.MONOTONIC:
        return "No"

    if getattr(family, "INCREASING", False):
        return "Increasing"

    if getattr(family, "DECREASING", False):
        return "Decreasing"

    return "Yes"