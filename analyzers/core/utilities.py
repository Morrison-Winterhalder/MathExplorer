def pretty(value):

    if isinstance(value, float):
        return f"{value:.4f}"

    if isinstance(value, list):
        return "[" + ", ".join(pretty(x) for x in value) + "]"

    if isinstance(value, tuple):
        return "(" + ", ".join(pretty(x) for x in value) + ")"

    return str(value)