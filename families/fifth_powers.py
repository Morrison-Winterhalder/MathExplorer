from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Fifth Powers"
DESCRIPTION = "Perfect fifth powers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 30
PARENT = "Polynomial"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000359"
ALIASES = [
    "Perfect Fifth Powers",
    "Fifth Powers",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Powers",
    "Fifth Power",
)

TRAITS = {
    "construction": "power",
    "degree": 5,
    "growth": "polynomial",
}

RELATED = [
    "Fourth Powers",
]

DOMAIN = "Integers"
GROWTH = "Quintic"

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
        root = integer_nth_root(term,5)

        if root**5 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**5

def formula(_):
    expression = "n^5"
    return format_formula(expression)

def complexity(_):
    return 5

def explain(_):
    return [
        "Every term is a perfect fifth power.",
    ]