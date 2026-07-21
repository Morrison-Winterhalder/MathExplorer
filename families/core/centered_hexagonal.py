from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Centered Hexagonal Numbers"
DESCRIPTION = "Numbers that form centered hexagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Centered Polygonal"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A003215"
ALIASES = [
    "Centered Hexagon Numbers",
    "Centered Hexagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Centered",
    "Hexagonal",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "centered_polygonal",
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Centered Triangular Numbers",
    "Centered Square Numbers",
    "Centered Pentagonal Numbers",
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

    if len(sequence) < MIN_TERMS:
        return None

    for n, term in enumerate(sequence, start=1):

        expected = 3 * n * (n - 1) + 1

        if term != expected:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return 3*n*(n-1)+1

def formula(_):
    return format_formula("3n(n-1)+1")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered hexagonal number.",
    ]