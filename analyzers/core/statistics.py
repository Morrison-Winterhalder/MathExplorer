from math import sqrt

def normalized_rmse(values, expected):
    if len(values) != len(expected):
        raise ValueError("Lists must be the same length.")

    if len(values) == 0:
        return 0.0

    mse = sum((v - e) ** 2 for v, e in zip(values, expected)) / len(values)
    rmse = sqrt(mse)

    scale = max(abs(e) for e in expected)

    if scale == 0:
        return rmse

    return rmse / scale

def r_squared(observed, predicted):
    if len(observed) != len(predicted):
        raise ValueError("Observed and predicted must have the same length.")

    if len(observed) == 0:
        return 1.0

    mean = sum(observed) / len(observed)

    ss_res = sum((o - p) ** 2 for o, p in zip(observed, predicted))
    ss_tot = sum((o - mean) ** 2 for o in observed)

    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0

    return max(0.0, 1 - ss_res / ss_tot)