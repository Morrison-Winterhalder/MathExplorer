NAME = "Hexagonal"
DESCRIPTION = "Hexagonal numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"


def recognize(sequence):
    if len(sequence) == 0:
        return None

    for n, value in enumerate(sequence, start=1):
        if value != evaluate({}, n):
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (2 * n - 1)


def formula(_):
    return "a(n) = n(2n - 1)"


def complexity(_):
    return 2