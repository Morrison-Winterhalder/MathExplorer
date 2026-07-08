from families.recurrence import evaluate_linear_recurrence

NAME = "Jacobsthal"

def is_jacobsthal(sequence):
    if len(sequence) < 3:
        return None

    if sequence[0] != 0 or sequence[1] != 1:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + 2 * sequence[i-2]:
            return False

    return True

def fit_jacobsthal(sequence):
    if not is_jacobsthal(sequence):
        return None

    return {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [1, 2]
    }

evaluate = evaluate_linear_recurrence

def complexity(_):
    return 2

fit = fit_jacobsthal
recognize = is_jacobsthal