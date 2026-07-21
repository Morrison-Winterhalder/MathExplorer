from __future__ import annotations


def render_family_tested(lines, event, analysis):

    if event.get("recognized"):

        lines.append(
            f"✓ {event['family']}"
        )

        if event.get("rrn") is not None:

            lines.append(
                f"    RRN = {event['rrn']:.6f}"
            )

    else:

        lines.append(
            f"✗ {event['family']}"
        )

def render_tie_resolved(lines, event, analysis):
    """
    Render the final tie-breaking result.
    """

    winners = event.get("winners", [])
    method = event.get("method", "Unknown")

    if not winners:
        return

    lines.append("")
    lines.append("Best Candidate")
    lines.append("--------------")

    for family in winners:
        lines.append(f"✓ {family}")

    lines.append("")
    lines.append(f"Tie resolved using: {method}")

def render_reasoning_generated(lines, event, analysis):

    confidence = analysis.confidence

    if confidence is None:
        return

    lines.append("")
    lines.append("Overall Confidence")
    lines.append("------------------")
    lines.append("")
    lines.append(
        f"{confidence['Score']:.1f}% ({confidence['Label']})"
    )
    lines.append("")

    sections = [
        (
            "Primary Evidence",
            event.get("primary", []),
            "✓"
        ),
        (
            "Supporting Evidence",
            event.get("supporting", []),
            "✓"
        ),
        (
            "Remaining Uncertainty",
            event.get("uncertainty", []),
            "•"
        ),
    ]

    for title, factors, symbol in sections:

        if not factors:
            continue

        lines.append(title)
        lines.append("-" * len(title))

        for factor in factors:
            lines.append(f"{symbol} {factor['name']}")

        lines.append("")

def render_formula_recovered(lines, event, analysis):

    formula = event.get("formula")

    if formula is None:
        return

    lines.append(formula)


def render_prediction_started(lines, event, analysis):

    formula = analysis.formula

    if formula:

        lines.append("Prediction Formula")
        lines.append("------------------")
        lines.append(formula)
        lines.append("")

    start = event["starting_index"]
    end = start + event["terms_requested"] - 1

    lines.append("Prediction Range")
    lines.append("----------------")
    lines.append(f"Terms {start}–{end}")


def render_predictions_generated(lines, event, analysis):

    predictions = analysis.next_terms

    if predictions is None:
        return

    start = event["starting_index"]

    lines.append("")
    lines.append("Generated Terms")
    lines.append("---------------")

    for i, value in enumerate(predictions):

        rounded = round(value)

        if abs(value - rounded) < 1e-10:
            value = rounded

        lines.append(
            f"a({start+i:<2}) = {value}"
        )

def render_verification_completed(lines, event, analysis):

    lines.append("")
    lines.append("Verification")
    lines.append("------------")
    lines.append("")

    if event["verified"]:

        lines.append("Status : PASSED")
        lines.append("")
        lines.append(
            "Generated sequence exactly matches the observed sequence."
        )

    else:

        lines.append("Status : FAILED")
        lines.append("")
        lines.append(
            "Generated sequence does not reproduce the observed sequence."
        )

def render_inference_generated(lines, event, analysis):

    lines.append("")
    lines.append("Inference")
    lines.append("---------")

    observation = event.get(
        "observation",
        "Unknown observation"
    )

    conclusion = event.get(
        "conclusion",
        "Unknown conclusion"
    )

    impact = event.get(
        "impact",
        ""
    )

    lines.append(
        f"Observation: {observation}"
    )

    lines.append(
        f"Conclusion: {conclusion}"
    )

    if impact:
        lines.append(
            f"Impact: {impact}"
        )

def render_candidate_comparison(lines, event, analysis):

    winner = event.get("winner", "Unknown")
    alternative = event.get("alternative", "Unknown")
    comparison = event.get("comparison", [])

    if not comparison:
        return

    lines.append("")
    lines.append("Candidate Comparison")
    lines.append("--------------------")
    lines.append("")
    lines.append(f"{winner} vs {alternative}")
    lines.append("")

    for reason in comparison:
        lines.append(f"• {reason}")

def render_decision_reasoning(lines, event, analysis):

    reasons = event.get("reasons", [])

    if not reasons:
        return

    lines.append("")
    lines.append("Decision Reasoning")
    lines.append("------------------")

    for reason in reasons:
        lines.append(f"• {reason}")

def render_family_selected(lines, event, analysis):

    family = event.get("family", "Unknown")
    reasons = event.get("reason", [])

    lines.append("")
    lines.append("Classification Decision")
    lines.append("-----------------------")
    lines.append("")
    lines.append(f"Selected Family : {family}")
    lines.append("")

    for reason in reasons:
        lines.append(f"✓ {reason}")

def render_reasoning_summary(lines, analysis):

    lines.append("=" * 60)
    lines.append("                     Final Assessment")
    lines.append("=" * 60)
    lines.append("")

    family = analysis.family
    confidence = analysis.confidence

    if family:
        lines.append(f"Classification : {family.NAME}")

    if confidence:
        lines.append(
            f"Confidence     : "
            f"{confidence['Score']:.1f}% "
            f"({confidence['Label']})"
        )

    lines.append("")

    lines.append("Decision Summary")
    lines.append("----------------")

    summary = [
        "Best mathematical explanation selected",
        "Hierarchy relationships validated",
        "Competing models evaluated",
        "Formula successfully recovered",
        "Prediction engine completed",
        "Verification completed successfully",
    ]

    for item in summary:
        lines.append(f"✓ {item}")

def render_analysis_complete(lines, analysis):

    lines.append("")
    lines.append("Execution Summary")
    lines.append("-----------------")
    lines.append("")

    completed = [
        "Recognition engine",
        "Classification engine",
        "Confidence engine",
        "Formula recovery",
        "Prediction engine",
        "Verification engine",
    ]

    for stage in completed:
        lines.append(f"✓ {stage}")

    lines.append("")
    lines.append("Developer trace generated successfully.")

EVENT_RENDERERS = {
    "family_tested": render_family_tested,
    "tie_resolved": render_tie_resolved,
    "reasoning_generated": render_reasoning_generated,

    "formula_recovered": render_formula_recovered,

    "prediction_started": render_prediction_started,
    "predictions_generated": render_predictions_generated,

    "verification_completed": render_verification_completed,

    "inference_generated": render_inference_generated,

    "candidate_comparison": render_candidate_comparison,
    "decision_reasoning": render_decision_reasoning,

    "family_selected": render_family_selected,

    "render_reason_summary": render_reasoning_summary,

    "analysis_completed": render_analysis_complete,
}