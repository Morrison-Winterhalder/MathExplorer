def get_family_metadata(family):
    fields = [
        "NAME",
        "DESCRIPTION",
        "CATEGORY",
        "PARENT",
        "SPECIFICITY",

        "OEIS",
        "ALIASES",

        "DOMAIN",
        "GROWTH",

        "MONOTONIC",
        "BOUNDED",
        "OSCILLATING",
        "PERIODIC",

        "FORMULA_TYPE",
        "REQUIRES_PARAMETERS",
        "PARAMETER_NAMES",

        "MIN_TERMS",
        "RECOGNITION_METHOD",
        "RELIABILITY",
    ]

    metadata = {}

    for field in fields:
        if hasattr(family, field):
            metadata[field] = getattr(family, field)

    return metadata