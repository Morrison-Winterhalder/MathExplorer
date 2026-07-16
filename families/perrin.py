from families.recurrence import evaluate_linear_recurrence

NAME = "Perrin Numbers"
DESCRIPTION = "A sequence where each term is the sum of the terms two and three positions before it."
REPRESENTATION = "Recursive"

CATEGORY = "Recursive"
SPECIFICITY = 55
PARENT = "Linear Recurrence"
NATURAL_FAMILY = True

OEIS = "A001608"
ALIASES = [
    "Perrin Sequence",
]

FAMILY_TYPE = "Sequence"

TAGS = (
    "Perrin",
    "Recurrence",
)

TRAITS = {
    "construction": "linear_recurrence",
    "order": 3,
    "growth": "exponential",
}

RELATED = [
    "Padovan Numbers",
]

DOMAIN = "Integers"
GROWTH = "Exponential"

MONOTONIC = False
BOUNDED = False
OSCILLATING = True
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

MIN_TERMS = 6
RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"


def recognize(sequence):

    if len(sequence) < 4:
        return None

    if sequence[:3] != [3, 0, 2]:
        return False

    for i in range(3, len(sequence)):
        if sequence[i] != sequence[i-2] + sequence[i-3]:
            return False

    return True


def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [3, 0, 2],
        "RecurrenceCoefficients": [0, 1, 1],
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return "a(n) = a(n - 2) + a(n - 3)"


def complexity(_):
    return 3


def explain(_):
    return [
        "The sequence follows the Perrin recurrence relation.",
        "Each term depends on terms two and three positions earlier."
    ]