from families.core.recurrence import evaluate_linear_recurrence

NAME = "Tetranacci Numbers"
DESCRIPTION = "A sequence where each term is the sum of the previous four terms."
REPRESENTATION = "Recursive"

CATEGORY = "Recursive"
SPECIFICITY = 60
PARENT = "Linear Recurrence"
NATURAL_FAMILY = True

OEIS = "A000078"
ALIASES = [
    "Tetranacci Sequence",
]

FAMILY_TYPE = "Sequence"

TAGS = (
    "Tetranacci",
    "Recurrence",
)

TRAITS = {
    "construction": "linear_recurrence",
    "order": 4,
    "growth": "exponential",
}

RELATED = [
    "Tribonacci Numbers",
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

MIN_TERMS = 7
RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"


def recognize(sequence):

    if len(sequence) < 5:
        return None

    if sequence[:4] != [0, 0, 0, 1]:
        return False

    for i in range(4, len(sequence)):
        if sequence[i] != sum(sequence[i-4:i]):
            return False

    return True


def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [0, 0, 0, 1],
        "RecurrenceCoefficients": [1, 1, 1, 1],
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return (
        "a(n) = a(n - 1) + a(n - 2) "
        "+ a(n - 3) + a(n - 4)"
    )


def complexity(_):
    return 4


def explain(_):
    return [
        "The sequence follows the Tetranacci recurrence relation.",
        "Each term is generated from the previous four terms."
    ]