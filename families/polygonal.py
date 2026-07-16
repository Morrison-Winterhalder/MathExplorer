NAME = "Polygonal"
DESCRIPTION = "Sequences formed from polygonal number constructions."
REPRESENTATION = "Category"
CATEGORY = "Figurate"
SPECIFICITY = 30
PARENT = "Figurate"

FAMILY_TYPE = "Category"

CHILDREN = [
    "Triangular Numbers",
    "Square Numbers",
    "Pentagonal Numbers",
    "Hexagonal Numbers",
]

TAGS = (
    "Polygonal",
    "Figurate",
    "Geometric",
)

TRAITS = {
    "construction": "polygonal",
    "growth": "quadratic",
    "domain": "integers",
}

RELATED = [
    "Centered Polygonal",
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
RECOGNITION_METHOD = "Parent Category"
RELIABILITY = "Exact"


def recognize(sequence):
    return False


def fit(sequence):
    return None


def evaluate(parameters, n):
    return None


def formula(parameters):
    return "Polygonal Family"


def complexity(parameters):
    return 2


def explain(parameters):
    return [
        "This family represents the general polygonal number hierarchy."
    ]