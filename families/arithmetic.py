from analyzers.core.transformations import first_differences
from families import constant
from families import polynomial

NAME = "Arithmetic"
DESCRIPTION = "Constant first differences."
REPRESENTATION = "Explicit"
CATEGORY = "Arithmetic"

def recognize(sequence):
    if len(sequence) < 2:
        return None
    return constant.recognize(first_differences(sequence))

def fit(sequence):
    if len(sequence) < 2:
        return None

    differences = first_differences(sequence)

    if not constant.recognize(differences):
        return None

    difference = differences[0]

    return {
        "Difference": difference,
        "Intercept": sequence[0] - difference
    }

def evaluate(parameters, n):
    return polynomial.evaluate(
        [
            parameters["Difference"],
            parameters["Intercept"]
        ],
        n
    )

def formula(parameters):
    d = parameters["Difference"]
    b = parameters["Intercept"]

    if b == 0:
        return f"a(n) = {d}n"

    if b > 0:
        return f"a(n) = {d}n + {b}"

    return f"a(n) = {d}n - {abs(b)}"

def complexity(_):
    return 1