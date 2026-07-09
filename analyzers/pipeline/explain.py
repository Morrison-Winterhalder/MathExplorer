from families import registry
from analyzers.core.trace import first_event


def update_explanation(sequence, report):

    classification = report["Sequence Classification"]

    family = classification["Family"]

    if family is None:
        report["Explanation"] = None
        return

    reasons = []

    # --------------------------------------------------
    # Hierarchy
    # --------------------------------------------------

    lineage = registry.get_lineage(family)

    if lineage:
        reasons.append(
            f"{family.NAME} is a subclass of the {lineage[0].NAME} family."
        )

    # --------------------------------------------------
    # Family-specific explanation
    # --------------------------------------------------

    if hasattr(family, "explain"):

        explanation = family.explain(
            classification["Parameters"]
        )

        if explanation is not None:
            reasons.extend(explanation)

    # --------------------------------------------------
    # Specificity
    # --------------------------------------------------

    tie = first_event(report, event="tie_detected")
    resolution = first_event(report, event="tie_resolved")

    if tie is not None:
        tied = [
            name
            for name in tie["families"]
            if name != family.NAME
        ]

        if tied:
            reasons.append(
                f"{', '.join(tied)} also matched exactly."
            )

    if resolution is not None:
        reasons.append(
            f"{family.NAME} was selected because it is the more specific family."
        )

    report["Explanation"] = {
        "Summary": f"The sequence was classified as {family.NAME}.",
        "Reasons": reasons,
    }