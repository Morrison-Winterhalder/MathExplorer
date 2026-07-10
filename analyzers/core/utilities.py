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