from analyzers.core.transformations import first_differences
from analyzers.core.formatter import format_formula
from families import constant
from families import polynomial

NAME = "Arithmetic"
DESCRIPTION = "Constant first differences."
REPRESENTATION = "Explicit"
CATEGORY = "Arithmetic"
SPECIFICITY = 20
PARENT = "Explicit"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = None
ALIASES = [
    "Linear Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Constant",
    "Simple",
)

TRAITS = {
    "growth": "constant",
    "construction": "explicit",
    "domain": "integers",
}

RELATED = [
    "Arithmetic",
]

DOMAIN = "Real Numbers"
GROWTH = "Linear"

MONOTONIC = None
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = True
PARAMETER_NAMES = (
    "Difference",
    "Intercept",
)

MIN_TERMS = 3
RECOGNITION_METHOD = "Constant First Differences"
RELIABILITY = "Exact"

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

    expression = f"{d}n"

    if b > 0:
        expression += f" + {b}"
    elif b < 0:
        expression += f" - {abs(b)}"

    return format_formula(expression)

def complexity(_):
    return 1

def explain(parameters):

    return [
        f"The sequence has a constant difference of {parameters['Difference']}."
    ]