from analyzers.core.formatter import format_formula

NAME = "Hexagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular hexagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

# Mathematical Metadata
OEIS = "A000384"
ALIASES = [
    "Hexagon Numbers",
    "Hexagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

TAGS = (
    "Figurate",
    "Polygonal",
    "Hexagonal",
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

    for n, value in enumerate(sequence, start=1):
        if value != evaluate({}, n):
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (2 * n - 1)


def formula(_):
    expression = "n(2n-1)"
    return format_formula(expression)


def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a hexagonal number.",
        "The sequence matches the hexagonal number formula exactly."
    ]