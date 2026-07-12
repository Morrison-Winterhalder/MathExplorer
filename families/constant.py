from analyzers.core.formatter import format_formula

NAME = "Constant"
DESCRIPTION = "All terms are equal."
REPRESENTATION = "Explicit"
CATEGORY = "Constant"
SPECIFICITY = 20
PARENT = "Arithmetic"

# Mathematical Metadata
OEIS = "A010701"
ALIASES = [
    "Constant Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Constant"

TAGS = (
    "Constant",
    "Polynomial",
)

DOMAIN = "Real Numbers"
GROWTH = "Constant"

MONOTONIC = True
BOUNDED = True
OSCILLATING = False
PERIODIC = True

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = True
PARAMETER_NAMES = (
    "Value",
)

MIN_TERMS = 1
RECOGNITION_METHOD = "Constant Values"
RELIABILITY = "Exact"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for value in sequence[1:]:
        if value != sequence[0]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Value": sequence[0]
    }


def evaluate(parameters, n):
    return parameters["Value"]

def formula(parameters):
    return format_formula(str(parameters["Value"]))

def complexity(_):
    return 0

def explain(parameters):
    return [
        f"Every term is equal to {parameters['Value']}.",
        "The sequence has zero first differences."
    ]
