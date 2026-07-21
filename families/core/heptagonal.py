from math import sqrt
from analyzers.core.formatter import format_formula

NAME = "Heptagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular heptagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000566"
ALIASES = [
    "Heptagon Numbers",
    "Heptagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Heptagonal",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "polygonal",
    "sides": 7,
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Triangular Numbers",
    "Square Numbers",
    "Pentagonal Numbers",
    "Hexagonal Numbers",
    "Octagonal Numbers",
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

        discriminant = 9 + 40 * term

        if discriminant < 0:

            return False


        root = sqrt(
            discriminant
        )


        if not root.is_integer():

            return False


        n = (
            3 + root
        ) / 10


        if not n.is_integer():

            return False


    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):

    if n == 0:
        return 0

    return n * (5 * n - 3) // 2

def formula(_):
    return format_formula("n(5n-3)/2")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a heptagonal number.",
    ]