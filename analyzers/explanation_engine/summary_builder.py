def build_summary(analysis):

    if analysis.family is None:
        return "No family was identified."

    return (
        f"The sequence was classified as "
        f"{analysis.family.NAME}."
    )