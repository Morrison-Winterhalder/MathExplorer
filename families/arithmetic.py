from analyzers.core.transformations import first_differences
from families.constant import is_constant
from families.polynomial import evaluate_polynomial

NAME = "Arithmetic"

def is_arithmetic(sequence):
    if len(sequence) < 2:
        return None
    return is_constant(first_differences(sequence))

def fit_arithmetic(sequence):
    if not is_arithmetic(sequence):
        return None

    differences = first_differences(sequence)
    difference = first_differences(sequence)[0]

    return {
        "Difference": difference,
        "Intercept": sequence[0]-difference
    }

def evaluate_arithmetic(parameters, n):
    coefficients = [
        parameters["Difference"],
        parameters["Intercept"]
    ]

    return evaluate_polynomial(coefficients, n)

def complexity(_):
    return 1

fit = fit_arithmetic
evaluate = evaluate_arithmetic
recognize = is_arithmetic