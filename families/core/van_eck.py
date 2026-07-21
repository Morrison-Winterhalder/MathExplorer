from analyzers.core.formatter import format_formula


NAME = "Van Eck Numbers"
DESCRIPTION = "A self-referential sequence based on previous occurrence distances."
REPRESENTATION = "Recursive"
CATEGORY = "Self-Referential"
SPECIFICITY = 70
PARENT = "Recursive"
NATURAL_FAMILY = True


# Mathematical Metadata
OEIS = "A181391"

ALIASES = [
    "Van Eck's Sequence",
]


CLOSED_FORM = False
EVALUATION_METHOD = "Recursive Generation"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Recursive",
    "Self-Referential",
    "History",
    "Integer",
)


TRAITS = {
    "growth": "irregular",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Look-and-Say Numbers",
]


DOMAIN = "Integers"
GROWTH = "Irregular"


MONOTONIC = False
BOUNDED = False
OSCILLATING = False
PERIODIC = False


FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = False

PARAMETER_NAMES = (
)


MIN_TERMS = 8

RECOGNITION_METHOD = "Recursive Generation"
RELIABILITY = "Exact"



def van_eck_number(n):

    sequence = [0]

    while len(sequence) < n:

        previous = sequence[-1]

        if previous not in sequence[:-1]:
            sequence.append(0)

        else:
            last_index = len(sequence) - 1

            previous_index = (
                len(sequence)
                - 1
                - sequence[-2::-1].index(previous)
            )

            sequence.append(
                last_index - previous_index
            )

    return sequence[n - 1]



def generate(length):

    if length <= 0:
        return []

    sequence = [0]

    while len(sequence) < length:

        previous = sequence[-1]

        positions = [
            i
            for i, value in enumerate(sequence[:-1])
            if value == previous
        ]

        if not positions:
            sequence.append(0)

        else:
            sequence.append(
                (len(sequence) - 1) - positions[-1]
            )

    return sequence



def recognize(sequence):

    generated = generate(len(sequence))

    return generated == sequence



def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {}



def evaluate(parameters, n):

    return generate(n)[-1]



def formula(parameters):

    return format_formula(
        "distance since previous occurrence"
    )



def complexity(_):
    return 3



def explain(parameters):

    return [
        "The sequence matches the Van Eck self-referential generation rule.",
        "Each term depends on when the previous value last appeared.",
        "If the previous term has not appeared before, the next term is 0.",
        "Otherwise, the next term is the distance since its previous occurrence."
    ]