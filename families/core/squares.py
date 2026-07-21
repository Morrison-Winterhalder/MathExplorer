from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Squares"
DESCRIPTION = "Perfect squares."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 30
PARENT = "Polynomial"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000290"
ALIASES = [
    "Square Numbers",
    "Perfect Squares",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Square",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "polygonal",
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Triangular Numbers",
    "Cubes",
]
DOMAIN = "Integers"
GROWTH = "Quadratic"

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
        if term < 0:
            return False

        root = integer_nth_root(term,2)

        if root * root != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n*n

def formula(_):
    expression = "n^2"
    return format_formula(expression)

def complexity(_):
    return 2

def explain(_):

    return [
        "Every term is a perfect square.",
    ]