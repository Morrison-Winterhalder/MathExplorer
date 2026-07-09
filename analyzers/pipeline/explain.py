from families import registry


def update_explanation(sequence, report):

    classification = report["Sequence Classification"]

    family = classification["Family"]

    if family is None:
        report["Explanation"] = None
        return

    recognition = report["Recognition Scores"]["Best Fit"]

    winners = recognition["Winners"]

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

    runner = recognition["Runner Up"]

    if runner is not None:

        reasons.append(
            f"{runner.NAME} also matched the sequence exactly."
        )

        reasons.append(
            f"{family.NAME} was selected because it is more specific."
        )

    # --------------------------------------------------
    # Specificity
    # --------------------------------------------------

    if len(winners) > 1:

        tied = [
            winner["Family"].NAME
            for winner in winners
            if winner["Family"] != family
        ]

        if tied:
            reasons.append(
                f"{', '.join(tied)} also matched exactly."
            )

            reasons.append(
                f"{family.NAME} was selected because it is the more specific family."
            )

    report["Explanation"] = {
        "Summary": f"The sequence was classified as {family.NAME}.",
        "Reasons": reasons,
    }