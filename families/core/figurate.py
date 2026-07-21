NAME = "Figurate"
DESCRIPTION = "Sequences representing geometric arrangements of points."
REPRESENTATION = "Category"
CATEGORY = "Structural"
SPECIFICITY = 20
PARENT = "Explicit"

FAMILY_TYPE = "Category"

CHILDREN = [
    "Polygonal",
    "Centered Polygonal",
]

TAGS = (
    "Figurate",
    "Geometric",
    "Visual",
)

TRAITS = {
    "construction": "geometric",
    "growth": "polynomial",
    "domain": "integers",
}

RELATED = [
    "Polynomial",
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
    "Shape",
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
    return "Figurate Number Family"


def complexity(parameters):
    return 2


def explain(parameters):
    return [
        "This is a parent category for figurate number families.",
        "Child families include polygonal and centered polygonal numbers."
    ]