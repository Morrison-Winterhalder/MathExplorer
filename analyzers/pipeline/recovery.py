from math import factorial
from analyzers.core.transformations import nth_differences, subtract_sequences, first_differences, first_ratios
from analyzers.pipeline.evaluation import evaluate_polynomial
from analyzers.core.properties import polynomial_degree
from analyzers.core.utilities import pretty
from analyzers.core.formatting import format_polynomial, clean_coefficients



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

def recover_polynomial_formula(sequence, report):
    coefficients = recover_polynomial(sequence)
    coefficients = clean_coefficients(coefficients)

    report["Sequence Classification"]["Parameters"] = coefficients
    report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")

def recover_arithmetic_formula(sequence, report):
    coefficients = recover_arithmetic(sequence)
    coefficients = clean_coefficients(coefficients)

    report["Sequence Classification"]["Parameters"] = coefficients
    report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")

def recover_geometric_formula(sequence, report):
    ratio = first_ratios(sequence)[0]

    report["Sequence Classification"]["Parameters"] = {
        "First Term": sequence[0],
        "Ratio": ratio}
    report["Sequence Classification"]["Formula"] = (f"a(n) = {recover_geometric(sequence)}")

def recover_constant_formula(sequence, report):
    report["Sequence Classification"]["Parameters"] = sequence[0]
    report["Sequence Classification"]["Formula"] = f"a(n) = {sequence[0]}"

def recover_triangular_formula(sequence, report):
    report["Sequence Classification"]["Parameters"] = None
    report["Sequence Classification"]["Formula"] = "a(n) = n(n+1)/2"

def recover_pentagonal_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = n(3n-1)/2"
    )

    report["Sequence Classification"]["Parameters"] = None

def recover_fibonacci_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = a(n-1) + a(n-2)"
    )

    report["Sequence Classification"]["Parameters"] = {
        "Seeds": [sequence[0],sequence[1]],
        "RecurrenceCoefficients": [1,1]
    }

def recover_lucas_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = a(n-1) + a(n-2)"
    )

    report["Sequence Classification"]["Parameters"] = {
        "Seeds": [2, 1],
        "RecurrenceCoefficients": [1, 1],
    }

def recover_pell_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = 2a(n-1) + a(n-2)"
    )

    report["Sequence Classification"]["Parameters"] = {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [2, 1],
    }

def recover_jacobsthal_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = a(n-1) + 2a(n-2)"
    )

    report["Sequence Classification"]["Parameters"] = {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [1, 2],
    }

def recover_factorial_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = "a(n) = n!"

    report["Sequence Classification"]["Parameters"] = {}

RECOVERY_HANDLERS = {
    "Polynomial": recover_polynomial_formula,
    "Arithmetic": recover_arithmetic_formula,
    "Geometric": recover_geometric_formula,
    "Constant": recover_constant_formula,
    "Triangular": recover_triangular_formula,
    "Pentagonal": recover_pentagonal_formula,
    "Fibonacci": recover_fibonacci_formula,
    "Lucas": recover_lucas_formula,
    "Pell": recover_pell_formula,
    "Jacobsthal": recover_jacobsthal_formula,
    "Factorial": recover_factorial_formula
}



def recover_formula(sequence, report):
    sequence_type = report["Sequence Classification"]["Type"]
    handler = RECOVERY_HANDLERS.get(sequence_type)
    if handler is not None:
        handler(sequence, report)
