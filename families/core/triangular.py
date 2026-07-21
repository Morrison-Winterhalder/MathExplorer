from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Triangular Numbers"
DESCRIPTION = "Numbers formed by adding consecutive positive integers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000217"
ALIASES = [
    "Triangle Numbers",
    "Triangular Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Triangular",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "polygonal",
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Square Numbers",
    "Pentagonal Numbers",
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

        value = 8 * term + 1
        if value < 0:
            return False
        root = isqrt(value)

        if root * root != value:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (n + 1) // 2


def formula(_):
    expression = "n(n+1)/2"
    return format_formula(expression)


def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a triangular number.",
    ]