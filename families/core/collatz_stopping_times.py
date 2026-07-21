from analyzers.core.formatter import format_formula


NAME = "Collatz Stopping Times"
DESCRIPTION = "Number of steps required for Collatz convergence."
REPRESENTATION = "Recursive"
CATEGORY = "Special"
SPECIFICITY = 55
PARENT = "Recursive"
NATURAL_FAMILY = True


OEIS = "A006577"

ALIASES = [
    "Total Stopping Time",
]


CLOSED_FORM = False
EVALUATION_METHOD = "Recursive Process"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Recursive",
    "Iterative",
)


TRAITS = {
    "growth": "irregular",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Happy Numbers",
]


DOMAIN = "Integers"
GROWTH = "Irregular"


MONOTONIC = None
BOUNDED = False
OSCILLATING = True
PERIODIC = False


FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = False

PARAMETER_NAMES = ()

MIN_TERMS = 5

RECOGNITION_METHOD = "Iterative Process"
RELIABILITY = "Exact"



def stopping_time(n):

    steps = 0

    while n != 1:

        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1

        steps += 1

    return steps



def recognize(sequence):

    expected = [
        stopping_time(n)
        for n in range(1, len(sequence)+1)
    ]

    return sequence == expected



def fit(sequence):

    if recognize(sequence):
        return {}

    return None



def evaluate(parameters, n):

    return stopping_time(n)



def formula(parameters):

    return format_formula(
        "Iterative Collatz transformation"
    )



def complexity(_):

    return 3



def explain(parameters):

    return [
        "Each term records the number of Collatz iterations required to reach 1.",
        "The sequence is generated through recursive integer transformation."
    ]