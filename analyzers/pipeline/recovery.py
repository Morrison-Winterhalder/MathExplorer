from analyzers.core.formatting import format_polynomial, clean_coefficients

def recover_polynomial_formula(sequence, report):
    parameters = report["Sequence Classification"]["Parameters"]
    coefficients = clean_coefficients(parameters)

    report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")

def recover_arithmetic_formula(sequence, report):
    parameters = report["Sequence Classification"]["Parameters"]
    coefficients = [
        parameters["Difference"],
        parameters["Intercept"]
    ]
    coefficients = clean_coefficients(coefficients)

    report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")

def recover_geometric_formula(sequence, report):
    parameters = report["Sequence Classification"]["Parameters"]

    report["Sequence Classification"]["Formula"] = (
        f"a(n) = {parameters['First Term']} · "
        f"{parameters['Ratio']}^(n-1)"
    )

def recover_constant_formula(sequence, report):
    parameters = report["Sequence Classification"]["Parameters"]

    report["Sequence Classification"]["Formula"] = (
        f"a(n) = {parameters['Value']}"
    )

def recover_triangular_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = "a(n) = n(n+1)/2"

def recover_pentagonal_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = n(3n-1)/2"
    )

def recover_fibonacci_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = a(n-1) + a(n-2)"
    )

def recover_lucas_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = a(n-1) + a(n-2)"
    )

def recover_pell_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = 2a(n-1) + a(n-2)"
    )

def recover_jacobsthal_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = (
        "a(n) = a(n-1) + 2a(n-2)"
    )

def recover_factorial_formula(sequence, report):
    report["Sequence Classification"]["Formula"] = "a(n) = n!"

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
    family = report["Sequence Classification"]["Family"]
    if family is None:
        return
    handler = RECOVERY_HANDLERS.get(family.NAME)
    if handler is not None:
        handler(sequence, report)
