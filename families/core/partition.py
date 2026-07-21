from analyzers.core.formatter import format_formula


NAME = "Partition Numbers"
DESCRIPTION = "Number of ways to write n as a sum of positive integers."
REPRESENTATION = "Explicit"
CATEGORY = "Combinatorial"
SPECIFICITY = 60
PARENT = "Combinatorial"
NATURAL_FAMILY = True


# Mathematical Metadata
OEIS = "A000041"

ALIASES = [
    "Integer Partitions",
    "Partition Function",
]


CLOSED_FORM = False
EVALUATION_METHOD = "Recursive Relation"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Combinatorial",
    "Partitions",
)


TRAITS = {
    "growth": "combinatorial",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Catalan Numbers",
    "Bell Numbers",
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

RECOGNITION_METHOD = "Partition Recurrence"
RELIABILITY = "Exact"



def partition_number(n):

    """
    Returns p(n):
    Number of integer partitions of n.

    Internal calculation uses p(0)=1,
    but the family indexing exposed to MathExplorer
    begins at n=1.
    """

    if n == 0:
        return 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for k in range(1, n + 1):

        for i in range(k, n + 1):

            partitions[i] += partitions[i - k]

    return partitions[n]



def recognize(sequence):

    if len(sequence) < MIN_TERMS:
        return None


    for index, value in enumerate(sequence, start=1):

        if value != partition_number(index):
            return None


    return True



def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {}



def evaluate(parameters, n):

    return partition_number(n)



def formula(parameters):

    return format_formula(
        "p(n)=number of integer partitions of n"
    )



def complexity(_):

    return 2



def explain(parameters):

    return [
        "The sequence matches the integer partition function.",
        "Each term represents the number of ways n can be written as a sum of positive integers.",
        "Partition numbers are a fundamental combinatorial sequence."
    ]