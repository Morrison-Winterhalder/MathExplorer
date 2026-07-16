def build_categories(
    hierarchy,
    family,
    specificity,
    evidence,
    warnings,
):
    return {
        "Hierarchy": hierarchy,
        "Family": family,
        "Specificity": specificity,
        "Evidence": evidence,
        "Warnings": warnings,
    }