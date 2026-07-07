from math import factorial
from analyzers.core.transformations import nth_differences, subtract_sequences, first_differences, first_ratios
from analyzers.pipeline.evaluation import evaluate_polynomial
from analyzers.core.properties import polynomial_degree
from analyzers.core.utilities import pretty

def recover_polynomial(sequence):
    if len(sequence) < 2:
        return None
    degree = polynomial_degree(sequence)
    coefficients = [0] * (degree + 1)
    remaining = sequence.copy()
    while degree >= 0:
        index = len(coefficients) - degree - 1
        constant_difference = nth_differences(remaining,degree)[0]
        leading = constant_difference / factorial(degree)
        temp_coefficients = [0] * len(coefficients)
        coefficients[index] = leading
        temp_coefficients[index] = leading
        generated = []
        for n in range(1, len(sequence) + 1):
            generated.append(evaluate_polynomial(temp_coefficients, n))
        remaining = subtract_sequences(remaining,generated)
        degree -= 1
    return coefficients

def recover_arithmetic(sequence):
    if len(sequence) < 2:
        return []
    return [first_differences(sequence)[0],(sequence[0]-first_differences(sequence)[0])]

def recover_geometric(sequence):
    if len(sequence) < 2:
        return None
    return f"{pretty(sequence[0])} · {pretty(first_ratios(sequence)[0])}^(n-1)"