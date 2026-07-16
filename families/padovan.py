from families.recurrence import evaluate_linear_recurrence

NAME = "Padovan Numbers"
DESCRIPTION = "A sequence where each term equals the sum of the terms three and two positions before it."
REPRESENTATION = "Recursive"

CATEGORY = "Recursive"
SPECIFICITY = 55
PARENT = "Linear Recurrence"
NATURAL_FAMILY = True

OEIS = "A000931"
ALIASES = [
    "Padovan Sequence",
]

FAMILY_TYPE = "Sequence"

TAGS = (
    "Padovan",
    "Recurrence",
)

TRAITS = {
    "construction": "linear_recurrence",
    "order": 3,
    "growth": "exponential",
}

RELATED = [
    "Perrin Numbers",
]

DOMAIN = "Integers"
GROWTH = "Exponential"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
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

    if sequence[:3] != [1, 1, 1]:
        return False

    for i in range(3, len(sequence)):
        if sequence[i] != sequence[i-2] + sequence[i-3]:
            return False

    return True


def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [1, 1, 1],
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
        "The sequence follows the Padovan recurrence relation.",
        "Each term depends on terms two and three positions earlier."
    ]