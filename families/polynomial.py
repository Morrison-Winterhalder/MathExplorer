from families import constant
from analyzers.core.transformations import first_differences, nth_differences, subtract_sequences
from math import factorial

NAME = "Polynomial"
DESCRIPTION = "Finite constant differences."
REPRESENTATION = "Explicit"

def compute_degree(sequence):
    if len(sequence) < 2:
        return None
    degree = 0
    while True:
        status = constant.recognize(sequence)
        if status is False:
            sequence = first_differences(sequence)
            degree += 1
        elif status is None:
            return None
        else:
            break
    return degree



def recognize(sequence):
    if len(sequence) < 2:
        return None
    return compute_degree(sequence) is not None

def fit(sequence):
    degree = compute_degree(sequence)

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
            evaluate(basis_coefficients, n)
            for n in range(1, len(sequence) + 1)
        ]
        residual = subtract_sequences(residual, generated)
        degree -= 1

    return coefficients

def evaluate(coefficients, n):
    value = 0
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        value += coefficient * n**power
    return value

def formula(coefficients):
    terms = []

    degree = len(coefficients) - 1

    for i, coefficient in enumerate(coefficients):
        power = degree - i

        if abs(coefficient) < 1e-12:
            continue

        if power == 0:
            terms.append(f"{coefficient:g}")
        elif power == 1:
            terms.append(f"{coefficient:g}n")
        else:
            terms.append(f"{coefficient:g}n^{power}")

    if not terms:
        return "a(n) = 0"

    return "a(n) = " + " + ".join(terms).replace("+ -", "- ")

def complexity(parameters):
    degree = max(0, len(parameters) - 1)
    return degree + 2
