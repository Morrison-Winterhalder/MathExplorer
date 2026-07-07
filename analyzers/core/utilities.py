def pretty(value):
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        return value

    elif isinstance(value, list):
        return [pretty(v) for v in value]

    elif isinstance(value, dict):
        return {k: pretty(v) for k, v in value.items()}

    return value