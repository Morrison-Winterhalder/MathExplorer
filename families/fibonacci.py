from families.recurrence import evaluate_linear_recurrence

NAME = "Fibonacci"
DESCRIPTION = "Each term is the sum of the previous two."
REPRESENTATION = "Recurrence"
CATEGORY = "Recurrence"
SPECIFICITY = 50

def recognize(sequence):
    if len(sequence) < 3:
        return False

    if sequence[:2] not in ([0, 1], [1, 1]):
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": sequence[:2],
        "RecurrenceCoefficients": [1, 1]
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return "a(n) = a(n-1) + a(n-2)"


def complexity(_):
    return 2