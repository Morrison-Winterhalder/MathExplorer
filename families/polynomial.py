from families.constant import is_constant
from analyzers.core.transformations import first_differences, nth_differences, subtract_sequences
from math import factorial

NAME = "Polynomial"

def polynomial_degree(sequence):
    if len(sequence) < 2:
        return None
    degree = 0
    while True:
        status = is_constant(sequence)
        if status is False:
            sequence = first_differences(sequence)
            degree += 1
        elif status is None:
            return None
        else:
            break
    return degree

def is_polynomial(sequence):
    return polynomial_degree(sequence) is not None

def fit_polynomial(sequence):
    degree = polynomial_degree(sequence)

    if degree is None:
        return None

    coefficients = [0] * (degree + 1)
    residual = sequence.copy()
    while degree >= 0:
        index = len(coefficients) - degree - 1
        constant_difference = nth_differences(residual, degree)[0]
        leading_coefficient = constant_difference / factorial(degree)
        basis_coefficients = [0] * len(coefficients)
        coefficients[index] = leading_coefficient
        basis_coefficients[index] = leading_coefficient
        generated = [
            evaluate_polynomial(basis_coefficients, n)
            for n in range(1, len(sequence) + 1)
        ]
        residual = subtract_sequences(residual, generated)
        degree -= 1

    return coefficients

def evaluate_polynomial(coefficients,n):
    value = 0
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        value += (coefficient) * ((n) ** power)
    return value

def complexity(parameters):
    degree = max(0, len(parameters) - 1)
    return degree + 2

recognize = is_polynomial
fit = fit_polynomial
evaluate = evaluate_polynomial