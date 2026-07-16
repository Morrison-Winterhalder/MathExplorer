from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Octagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular octagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000567"
ALIASES = [
    "Octagon Numbers",
    "Octagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Octagonal",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "polygonal",
    "sides": 8,
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Triangular Numbers",
    "Square Numbers",
    "Pentagonal Numbers",
    "Hexagonal Numbers",
    "Heptagonal Numbers",
    "Nonagonal Numbers",
    "Decagonal Numbers",
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
        value = 3 * term + 1
        if value < 0:
            return False
        root = isqrt(value)

        if root * root != value:
            return False

        if (1 + root) % 3 != 0:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (3 * n - 2)

def formula(_):
    return format_formula("n(3n-2)")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is an octagonal number.",
    ]