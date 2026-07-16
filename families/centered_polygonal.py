NAME = "Centered Polygonal"
DESCRIPTION = "Sequences formed by placing polygonal layers around a central point."
REPRESENTATION = "Category"
CATEGORY = "Figurate"
SPECIFICITY = 35
PARENT = "Figurate"

FAMILY_TYPE = "Category"

CHILDREN = [
    "Centered Triangular Numbers",
    "Centered Square Numbers",
    "Centered Pentagonal Numbers",
    "Centered Hexagonal Numbers",
]

TAGS = (
    "Centered",
    "Polygonal",
    "Figurate",
)

TRAITS = {
    "construction": "centered_polygonal",
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Polygonal",
]
DOMAIN = "Integers"
GROWTH = "Polynomial"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = True
PARAMETER_NAMES = (
    "Number of sides",
)

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

MIN_TERMS = 3
RECOGNITION_METHOD = "Figurate Formula"
RELIABILITY = "Exact"


def recognize(sequence):
    return False


def fit(sequence):
    return None


def evaluate(parameters, n):
    return None


def formula(parameters):
    return "Centered Polygonal Family"


def complexity(parameters):
    return 2


def explain(parameters):
    return [
        "This is a parent category for centered polygonal number families."
    ]