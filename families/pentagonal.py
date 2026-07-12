from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Pentagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular pentagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

# Mathematical Metadata
OEIS = "A000326"
ALIASES = [
    "Pentagon Numbers",
    "Pentagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

TAGS = (
    "Figurate",
    "Polygonal",
    "Pentagonal",
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

    for value in sequence:
        discriminant = 1 + 24 * value
        if discriminant < 0:
            return False
        root = isqrt(discriminant)

        if root * root != discriminant:
            return False

        n = (1 + root) / 6

        if not n.is_integer():
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (3 * n - 1) // 2


def formula(_):
    expression = "n(3n-1)/2"
    return format_formula(expression)


def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a pentagonal number.",
        "The sequence matches the pentagonal number formula exactly."
    ]