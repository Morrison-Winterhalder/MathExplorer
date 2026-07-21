from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Decagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular decagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A001107"
ALIASES = [
    "Decagon Numbers",
    "Decagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Decagonal",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "polygonal",
    "sides": 10,
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Triangular Numbers",
    "Square Numbers",
    "Pentagonal Numbers",
    "Hexagonal Numbers",
    "Heptagonal Numbers",
    "Octagonal Numbers",
    "Nonagonal Numbers",
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

        discriminant = 9 + 16 * term

        if discriminant < 0:

            return False


        root = isqrt(
            discriminant
        )


        if root * root != discriminant:

            return False


        if (
            3 + root
        ) % 8 != 0:

            return False


    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):

    if n == 0:
        return 0

    return n * (4 * n - 3)

def formula(_):
    return format_formula("n(4n-3)")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a decagonal number.",
    ]