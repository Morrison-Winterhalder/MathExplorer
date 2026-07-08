from analyzers.core.utilities import pretty

def format_polynomial(coefficients):
    polyList = []
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        if coefficient == 0:
            continue
        elif power == 0:
            polyList.append(str(pretty(coefficient)))
        elif power == 1:
            if coefficient == 1:
                polyList.append("n")
            elif coefficient == -1:
                polyList.append("-n")
            else:
                polyList.append(f"{pretty(coefficient)}n")
        else:
            if coefficient == 1:
                polyList.append(f"n^{pretty(power)}")
            elif coefficient == -1:
                polyList.append(f"-n^{pretty(power)}")
            else:
                polyList.append(f"{pretty(coefficient)}n^{pretty(power)}")
    polyString = " + ".join(polyList)
    polyString = polyString.replace("+ -", "- ")
    if not polyList:
        return "0"
    return polyString

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