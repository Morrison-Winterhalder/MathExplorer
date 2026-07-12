from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Fourth Powers"
DESCRIPTION = "Perfect fourth powers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 30
PARENT = "Polynomial"

# Mathematical Metadata
OEIS = "A003828"
ALIASES = [
    "Bi-Squares",
    "Fourth Powers",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

TAGS = (
    "Fourth Power",
    "Polynomial",
)

DOMAIN = "Integers"
GROWTH = "Quartic"

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
        root = integer_nth_root(term, 4)

        if root is None:
            return False

        if root ** 4 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**4

def formula(_):
    expression = "n^4"
    return format_formula(expression)

def complexity(_):
    return 4

def explain(_):
    return [
        "Every term is a perfect fourth power.",
        "The sequence matches the formula n⁴ exactly."
    ]