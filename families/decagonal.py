from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Decagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular decagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

# Mathematical Metadata
OEIS = "A001107"
ALIASES = [
    "Decagon Numbers",
    "Decagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

TAGS = (
    "Figurate",
    "Polygonal",
    "Decagonal",
)

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
        value = 4 * term + 4
        if term < 0:
            return False
        root = isqrt(value)

        if root * root != value:
            return False

        if (2 + root) % 4 != 0:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (4 * n - 3)

def formula(_):
    return format_formula("n(4n-3)")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a decagonal number.",
        "The sequence matches the decagonal number formula exactly."
    ]