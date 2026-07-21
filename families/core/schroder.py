from analyzers.core.formatter import format_formula


NAME = "Schröder Numbers"
DESCRIPTION = "Counts large Schröder paths and related combinatorial structures."
REPRESENTATION = "Recursive"
CATEGORY = "Combinatorial"
SPECIFICITY = 60
PARENT = "Combinatorial"
NATURAL_FAMILY = True


# Mathematical Metadata
OEIS = "A006318"

ALIASES = [
    "Large Schroder Numbers",
    "Little Schröder Numbers",
]


CLOSED_FORM = False
EVALUATION_METHOD = "Recursive Relation"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Combinatorial",
    "Recursive",
    "Paths",
)


TRAITS = {
    "growth": "combinatorial",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Catalan Numbers",
    "Bell Numbers",
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

RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"



def schroder_number(n):

    """
    Large Schröder numbers.

    Internal recurrence starts from S(0)=1,
    but MathExplorer indexing begins at n=1.
    """

    if n == 0:
        return 1

    values = [0] * (n + 1)

    values[0] = 1

    for i in range(1, n + 1):

        total = values[i - 1]

        for k in range(i):

            total += values[k] * values[i - 1 - k]

        values[i] = total

    return values[n]



def recognize(sequence):

    if len(sequence) < MIN_TERMS:
        return None


    for index, value in enumerate(sequence, start=1):

        if value != schroder_number(index - 1):
            return None


    return True



def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {}



def evaluate(parameters, n):

    return schroder_number(n - 1)



def formula(parameters):

    return format_formula(
        "S(n)=S(n-1)+Σ(S(k)S(n-1-k))"
    )



def complexity(_):

    return 2



def explain(parameters):

    return [
        "The sequence matches the large Schröder number recurrence.",
        "Schröder numbers count several classes of combinatorial objects.",
        "The recurrence builds each term from previous sequence values."
    ]