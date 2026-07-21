import math

from analyzers.core.formatter import format_formula
from analyzers.core.utilities import pretty


NAME = "Bell Numbers"
DESCRIPTION = "Number of partitions of a set."
REPRESENTATION = "Recursive"
CATEGORY = "Combinatorial"
SPECIFICITY = 60
PARENT = "Combinatorial"
NATURAL_FAMILY = True


# Mathematical Metadata
OEIS = "A000110"

ALIASES = [
    "Bell",
    "Bell Sequence",
    "Set Partition Numbers",
]

CLOSED_FORM = False
EVALUATION_METHOD = "Bell Recurrence"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Combinatorial",
    "Recursive",
    "Partition",
)


TRAITS = {
    "growth": "combinatorial",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Catalan Numbers",
    "Partition Numbers",
]


DOMAIN = "Integers"
GROWTH = "Combinatorial"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False


FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = False

PARAMETER_NAMES = (
)


MIN_TERMS = 5

RECOGNITION_METHOD = "Bell Recurrence"
RELIABILITY = "Exact"



def bell_number(n):

    if n == 0:
        return 1

    bell = [
        [0 for _ in range(n + 1)]
        for _ in range(n + 1)
    ]

    bell[0][0] = 1

    for i in range(1, n + 1):

        bell[i][0] = bell[i-1][i-1]

        for j in range(1, i + 1):

            bell[i][j] = (
                bell[i-1][j-1]
                +
                bell[i][j-1]
            )

    return bell[n][0]



def recognize(sequence):

    if len(sequence) < MIN_TERMS:
        return None

    for index, value in enumerate(sequence):

        expected = bell_number(index)

        if value != expected:
            return False

    return True



def fit(sequence):

    if recognize(sequence) is not True:
        return None

    predicted = [
        evaluate({}, n)
        for n in range(1, len(sequence) + 1)
    ]

    residuals = [
        actual - expected
        for actual, expected in zip(sequence, predicted)
    ]

    return {
        "Parameters": {},
        "Predicted": predicted,
        "Residuals": residuals,
    }



def evaluate(parameters, n):

    return bell_number(n - 1)



def formula(parameters):

    return format_formula(
        "B(n+1)=Σ(k=0 to n) C(n,k)B(k)"
    )



def complexity(_):

    return 2



def explain(parameters):

    return [
        "The sequence matches the Bell number recurrence.",
        "Bell numbers count the number of partitions of a set.",
        "Each term represents the number of ways a set of n elements can be divided into non-empty subsets."
    ]