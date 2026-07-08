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

def relative_residual_norm(actual, predicted):
    if len(actual) != len(predicted):
        return None

    residual_sum = 0
    actual_sum = 0

    for a, p in zip(actual, predicted):
        residual_sum += (a - p) ** 2
        actual_sum += a ** 2

    if actual_sum == 0:
        return 0 if residual_sum == 0 else None

    return sqrt(residual_sum) / sqrt(actual_sum)


"""
tests = [

    ("Perfect Arithmetic",
        0.00,
        1.20,
        20,
        2),

    ("Excellent Arithmetic",
        0.02,
        0.80,
        20,
        2),

    ("Close Competition",
        0.02,
        0.03,
        20,
        2),

    ("High Degree Polynomial",
        0.02,
        0.80,
        20,
        8),

    ("Short Sequence",
        0.02,
        0.80,
        5,
        2),

    ("Long Sequence",
        0.02,
        0.80,
        100,
        2),

    ("Poor Fit",
        0.25,
        0.60,
        20,
        2),
]

for name, winner, second, length, complexity in tests:

    result = confidence_engine(
        winner,
        second,
        length,
        complexity
    )

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    for key, value in result.items():
        if isinstance(value, float):
            print(f"{key:22}: {value:.4f}")
        else:
            print(f"{key:22}: {value}")

"""