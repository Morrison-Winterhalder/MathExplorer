def render_explanation(explanation):

    if explanation is None:
        return "No explanation available."

    lines = []

    lines.append("Explanation")
    lines.append("-----------")
    lines.append("")

    # -------------------------
    # Summary
    # -------------------------

    summary = explanation.get("Summary")

    if summary:
        lines.append("Summary")
        lines.append("-------")
        lines.append(summary)
        lines.append("")


    # -------------------------
    # Reasons
    # -------------------------

    reasons = explanation.get("Reasons", [])

    if reasons:

        lines.append("Reasoning")
        lines.append("---------")

        for reason in reasons:
            lines.append(
                f"• {reason}"
            )

        lines.append("")


    # -------------------------
    # Evidence
    # -------------------------

    evidence = explanation.get("Evidence", [])

    if evidence:

        lines.append("Evidence")
        lines.append("--------")

        for item in evidence:
            lines.append(
                f"• {item}"
            )

        lines.append("")


    # -------------------------
    # Warnings
    # -------------------------

    warnings = explanation.get("Warnings", [])

    if warnings:

        lines.append("Warnings")
        lines.append("--------")

        for warning in warnings:
            lines.append(
                f"⚠ {warning}"
            )

        lines.append("")


    return "\n".join(lines)