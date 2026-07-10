from __future__ import annotations
from analyzers.core.trace import first_event, events, has_event


def render_family_tested(lines, event, report):
    symbol = "✓" if event.get("recognized") else "✗"
    family = event.get("family", "Unknown")

    lines.append(f"{symbol} {family}")

    rrn = event.get("rrn")
    if event.get("recognized") and rrn is not None:
        lines.append(f"    RRN = {rrn:.6f}")


def render_family_ranked(lines, event, report):

    rank = event["rank"]
    family = event["family"]
    score = event["ranking_score"]

    if rank == 1:
        lines.append("")
        lines.append("Ranking")
        lines.append("-------")

    lines.append(
        f"{rank}. {family:<20} {score:.6f}"
    )

def render_ranking_calculated(lines, event, report):

    lines.append(f"✓ {event['family']}")
    lines.append(f"    RRN = {event['rrn']:.6f}")
    lines.append(f"    Complexity = {event['complexity']}")
    lines.append(
        f"    Ranking Score = {event['ranking_score']:.6f}"
    )

def render_tie_detected(lines, event, report):
    families = event.get("families", [])

    lines.append("")
    lines.append("Tie detected:")
    for family in families:
        lines.append(f"    {family}")


def render_tie_resolved(lines, event, report):
    method = event.get("method", "unknown method")
    winners = event.get("winners", [])

    lines.append("")
    lines.append(f"Resolved by {method}:")

    for family in winners:
        lines.append(f"    {family}")


def render_winner_selected(lines, event, report):
    winners = event.get("winners", [])

    lines.append("Best Candidate")
    lines.append("---------------")
    for family in winners:
        lines.append(f"{family}")


def render_classification_completed(lines, event, report):

    family = event["family"]

    if family is None:
        lines.append("No family selected.")
        return

    lines.append("")
    lines.append("Reason")
    lines.append("------")

    resolution = first_event(report, "tie_resolved")

    if resolution is None:
        lines.append("Lowest ranking score.")
    else:
        lines.append(
            f"Tie resolved using {resolution['method']}."
        )

    hierarchy = report["Sequence Classification"]["Hierarchy"]

    if hierarchy:
        lines.append("")
        lines.append("Hierarchy")
        lines.append("---------")
        lines.append(hierarchy)


def render_winner_assessed(lines, event, report):

    lines.append("Confidence Inputs")
    lines.append("-----------------")

    lines.append(
        f"Winning Family : {event['family']}"
    )

    lines.append(
        f"Winner Error   : {event['rrn']:.6f}"
    )


def render_competition_assessed(lines, event, report):

    if event["runner_up"] is None:

        lines.append("Runner-Up      : None")
        return

    lines.append(
        f"Runner-Up      : {event['runner_up']}"
    )

    lines.append(
        f"Runner Error   : {event['runner_up_rrn']:.6f}"
    )

    lines.append(
        f"Separation     : {event['separation']:.6f}"
    )

def render_complexity_assessed(lines, event, report):
    complexity = event.get("complexity")
    if complexity is not None:
        lines.append(
            f"Complexity     : {complexity}"
        )


def render_sample_size_assessed(lines, event, report):
    sample_size = event.get("sample_size")
    if sample_size is not None:
        lines.append(
            f"Sample Size    : {sample_size} terms"
        )


def render_confidence_calculated(lines, event, report):

    lines.append("")
    lines.append("Confidence Score")
    lines.append("----------------")

    lines.append(
        "Base Score            +60.00"
    )

    lines.append(
        f"Fit Penalty           -{event['fit_penalty']:.2f}"
    )

    lines.append(
        f"Competition Penalty   -{event['competition_penalty']:.2f}"
    )

    lines.append(
        f"Sample Bonus          +{event['sample_size_bonus']:.2f}"
    )

    lines.append(
        f"Complexity Penalty    -{event['complexity_penalty']:.2f}"
    )

    lines.append("")
    lines.append(
        f"Computed Score           {event['score']:.2f}"
    )


def render_tie_adjustment(lines, event, report):
    adjustment = event.get("adjustment")
    if adjustment is not None:
        lines.append(f"Tie adjustment: {adjustment}")


def render_confidence_finalized(lines, event, report):

    lines.append("")
    lines.append("Final Confidence")
    lines.append("----------------")

    lines.append(
        f"{event['score']:.1f}% ({event['label']})"
    )


def render_formula_recovered(lines, event, report):

    formula = event.get("formula")

    lines.append("Recovered Formula")
    lines.append("-----------------")

    if formula is None:
        lines.append("Unavailable.")
        return
    
    lines.append(formula)


def render_prediction_started(lines, event, report):

    formula = report["Sequence Classification"]["Formula"]

    lines.append("Using Formula")
    lines.append("-------------")

    lines.append(formula)

    lines.append("")

    start = event["starting_index"]
    end = start + event["terms_requested"] - 1

    lines.append(
        f"Predicting terms {start}-{end}"
    )


def render_predictions_generated(lines, event, report):

    predictions = report["Predictions"]["Next Terms"]

    start = event["starting_index"]

    lines.append("")
    lines.append("Generated Terms")
    lines.append("---------------")

    for i, value in enumerate(predictions):

        lines.append(
            f"a({start+i}) = {value}"
        )

def render_verification_completed(lines, event, report):

    if event["verified"]:

        lines.append("Verification Passed")
        lines.append("-------------------")

        lines.append("")
        lines.append(
            "Generated sequence matches the input."
        )

    else:

        lines.append("")
        lines.append("Verification Failed")

def render_reasoning_summary(lines, report):

    lines.append("Reasoning Summary")
    lines.append("-" * 60)
    lines.append("")

    tested = len(events(report, event="family_tested"))

    accepted = len([
        event
        for event in events(report, event="family_tested")
        if event.get("recognized")
    ])

    classification = report["Sequence Classification"]
    confidence = classification["Confidence"]

    lines.append(
        f"• Tested {tested} candidate families."
    )

    if accepted == 1:
        lines.append("• 1 family matched the sequence.")
    else:
        lines.append(f"• {accepted} families matched the sequence.")

    if classification["Family"] is not None:
        lines.append(
            f"• Selected {classification['Family'].NAME}."
        )

    if confidence is not None:
        lines.append(
            f"• Confidence: "
            f"{confidence['Score']:.1f}% "
            f"({confidence['Label']})."
        )

    if classification.get("Formula") is not None:
        lines.append(
            "• Symbolic formula recovered."
        )

    verified = report["Verification"]["Verified"]

    if verified:
        lines.append(
            "• Verification succeeded."
        )
    elif verified is False:
        lines.append(
            "• Verification failed."
        )

    lines.append("")

def render_analysis_complete(lines, report):

    lines.append("Analysis Complete")
    lines.append("-" * 60)
    lines.append("")

    lines.append(
        "✓ Pipeline executed successfully."
    )

    lines.append(
        "✓ Developer trace complete."
    )

    lines.append("")

EVENT_RENDERERS = {
    "family_tested": render_family_tested,
    "family_ranked": render_family_ranked,
    "ranking_calculated": render_ranking_calculated,
    "tie_detected": render_tie_detected,
    "tie_resolved": render_tie_resolved,
    "winner_selected": render_winner_selected,
    "classification_completed": render_classification_completed,

    "winner_assessed": render_winner_assessed,
    "competition_assessed": render_competition_assessed,
    "complexity_assessed": render_complexity_assessed,
    "sample_size_assessed": render_sample_size_assessed,
    "confidence_calculated": render_confidence_calculated,
    "tie_adjustment": render_tie_adjustment,
    "confidence_finalized": render_confidence_finalized,

    "formula_recovered": render_formula_recovered,

    "prediction_started": render_prediction_started,
    "predictions_generated": render_predictions_generated,

    "verification_completed": render_verification_completed,

    "render_reason_summary": render_reasoning_summary,

    "analysis_completed": render_analysis_complete,
}