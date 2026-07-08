from families.recurrence import evaluate_linear_recurrence

NAME = "Jacobsthal"
DESCRIPTION = "Each term equals the previous term plus twice the term before."
REPRESENTATION = "Recurrence"


def recognize(sequence):
    if len(sequence) < 3:
        return None

    if sequence[:2] != [0, 1]:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + 2 * sequence[i - 2]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [1, 2]
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return "a(n) = a(n-1) + 2a(n-2)"


def complexity(_):
    return 2