from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Cubes"
DESCRIPTION = "Perfect cubes."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 30
PARENT = "Polynomial"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000578"
ALIASES = [
    "Cube Numbers",
    "Perfect Cubes",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Powers",
    "Cubes",
)

TRAITS = {
    "construction": "power",
    "degree": 3,
    "growth": "polynomial",
}

RELATED = [
    "Square Numbers",
    "Fourth Powers",
]

DOMAIN = "Integers"
GROWTH = "Cubic"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

MIN_TERMS = 3
RECOGNITION_METHOD = "Direct Formula"
RELIABILITY = "Exact"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = integer_nth_root(term,3)

        if root**3 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**3

def formula(_):
    expression = "n^3"
    return format_formula(expression)

def complexity(_):
    return 3

def explain(_):
    return [
        "Every term is a perfect cube.",
    ]