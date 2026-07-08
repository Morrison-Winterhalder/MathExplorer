from families.recurrence import evaluate_linear_recurrence

NAME = "Pell"

def is_pell(sequence):
    if len(sequence) < 3:
        return None

    if sequence[0] != 0 or sequence[1] != 1:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != 2 * sequence[i-1] + sequence[i-2]:
            return False

    return True

def fit_pell(sequence):
    if is_pell(sequence) is not True:
        return None
    
    return {
        "Seeds": [0,1],
        "RecurrenceCoefficients": [2,1]
    }

evaluate = evaluate_linear_recurrence

def complexity(_):
    return 2

fit = fit_pell
recognize = is_pell