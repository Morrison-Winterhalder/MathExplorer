from analyzers.core.transformations import first_ratios
from analyzers.core.formatting import format_polynomial, clean_coefficients
from families.polynomial import fit_polynomial
from families.arithmetic import fit_arithmetic
from families.geometric import fit_geometric

def recover_polynomial_formula(sequence, report):
    coefficients = fit_polynomial(sequence)
    coefficients = clean_coefficients(coefficients)

    report["Sequence Classification"]["Parameters"] = coefficients
    report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")

def recover_arithmetic_formula(sequence, report):
    parameters = fit_arithmetic(sequence)
    coefficients = [
        parameters["Difference"],
        parameters["Intercept"]
    ]
    coefficients = clean_coefficients(coefficients)

    report["Sequence Classification"]["Parameters"] = coefficients
    report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")

def recover_geometric_formula(sequence, report):
    parameters = fit_geometric(sequence)

    report["Sequence Classification"]["Parameters"] = parameters

    report["Sequence Classification"]["Formula"] = (
        f"a(n) = {parameters['First Term']} · "
        f"{parameters['Ratio']}^(n-1)"
    )

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
