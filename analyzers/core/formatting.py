from analyzers.core.utilities import pretty

def format_polynomial(coefficients):
    terms = []

    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i

        if coefficient == 0:
            continue

        # Constant
        if power == 0:
            terms.append(str(pretty(coefficient)))

        # Linear
        elif power == 1:
            if coefficient == 1:
                terms.append("n")
            elif coefficient == -1:
                terms.append("-n")
            else:
                terms.append(f"{pretty(coefficient)}n")

        # Higher powers
        else:
            if coefficient == 1:
                terms.append(f"n^{pretty(power)}")
            elif coefficient == -1:
                terms.append(f"-n^{pretty(power)}")
            else:
                terms.append(
                    f"{pretty(coefficient)}n^{pretty(power)}"
                )

    if not terms:
        return "0"

    polynomial = " + ".join(terms)
    polynomial = polynomial.replace("+ -", "- ")

    return polynomial

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