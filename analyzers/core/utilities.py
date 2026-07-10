from math import isqrt

def pretty(value):

    if isinstance(value, float):

        if value.is_integer():
            return str(int(value))

        return f"{value:.4f}".rstrip("0").rstrip(".")

    if isinstance(value, list):
        return "[" + ", ".join(pretty(x) for x in value) + "]"

    if isinstance(value, tuple):
        return "(" + ", ".join(pretty(x) for x in value) + ")"

    return str(value)

def integer_nth_root(n, power):
    """
    Returns the nearest integer nth root of n.

    Even powers reject negative inputs by returning None.
    Odd powers preserve the sign.
    """

    if power <= 0:
        raise ValueError("power must be positive")

    if n < 0:
        if power % 2 == 0:
            return None
        return -round((-n) ** (1 / power))

    return round(n ** (1 / power))