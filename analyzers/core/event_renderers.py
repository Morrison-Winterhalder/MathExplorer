from __future__ import annotations
from analyzers.core.trace import first_event, events, has_event


def render_family_tested(lines, event, analysis):
    symbol = "✓" if event.get("recognized") else "✗"
    family = event.get("family", "Unknown")

    lines.append(f"{symbol} {family}")

    rrn = event.get("rrn")
    if event.get("recognized") and rrn is not None:
        lines.append(f"    RRN = {rrn:.6f}")


def render_family_ranked(lines, event, analysis):

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

def render_ranking_calculated(lines, event, analysis):

    lines.append(f"✓ {event['family']}")
    lines.append(f"    RRN = {event['rrn']:.6f}")
    lines.append(f"    Complexity = {event['complexity']}")
    lines.append(
        f"    Ranking Score = {event['ranking_score']:.6f}"
    )

def render_tie_detected(lines, event, analysis):
    families = event.get("families", [])

    lines.append("")
    lines.append("Tie detected:")
    for family in families:
        lines.append(f"    {family}")


def render_tie_resolved(lines, event, analysis):
    method = event.get("method", "unknown method")
    winners = event.get("winners", [])

    lines.append("")
    lines.append(f"Resolved by {method}:")

    for family in winners:
        lines.append(f"    {family}")


def render_winner_selected(lines, event, analysis):
    winners = event.get("winners", [])

    lines.append("Best Candidate")
    lines.append("---------------")
    for family in winners:
        lines.append(f"{family}")


def render_classification_completed(lines, event, analysis):

    family_name = event["family"]

    winner = analysis.best_fit["Winners"][0]
    family = winner["Family"]

    if family is None:
        lines.append("No family selected.")
        return

    lines.append("")
    lines.append("Reason")
    lines.append("------")

    resolution = first_event(analysis, "tie_resolved")

    if resolution is None:
        lines.append("Lowest ranking score.")
    else:
        lines.append(
            f"Tie resolved using {resolution['method']}."
        )

    # -----------------------------------------
    # Why this family was selected
    # -----------------------------------------

    lines.append("")
    lines.append("Why This Family Was Selected")
    lines.append("----------------------------")

    lines.append(
        f"Selected: {family_name}"
    )

    lines.append("")

    if getattr(family, "NATURAL_FAMILY", False):

        lines.append(
            "✓ Recognized mathematical family"
        )

    else:

        lines.append(
            "✓ General mathematical model"
        )

    if family.PARENT is not None:

        lines.append(
            "✓ Correct hierarchy placement"
        )

    complexity = family.complexity(
        analysis.best_fit["Winners"][0]["Parameters"]
    )

    if complexity <= 3:

        lines.append(
            "✓ Lower complexity explanation"
        )

    lines.append(
        "✓ Generalizes beyond observed terms"
    )

    # -----------------------------------------
    # Hierarchy
    # -----------------------------------------

    hierarchy = analysis.hierarchy

    if hierarchy:

        lines.append("")
        lines.append("Hierarchy")
        lines.append("---------")
        lines.append(hierarchy)
        lines.append(hierarchy)


def render_winner_assessed(lines, event, analysis):

    lines.append("Confidence Inputs")
    lines.append("-----------------")

    lines.append(
        f"Winning Family : {event['family']}"
    )

    lines.append(
        f"Winner Error   : {event['rrn']:.6f}"
    )


def render_competition_assessed(lines, event, analysis):

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

def render_complexity_assessed(lines, event, analysis):
    complexity = event.get("complexity")
    if complexity is not None:
        lines.append(
            f"Complexity     : {complexity}"
        )


def render_sample_size_assessed(lines, event, analysis):
    sample_size = event.get("sample_size")
    if sample_size is not None:
        lines.append(
            f"Sample Size    : {sample_size} terms"
        )


def render_confidence_calculated(lines, event, analysis):

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


def render_tie_adjustment(lines, event, analysis):
    adjustment = event.get("adjustment")
    if adjustment is not None:
        lines.append(f"Tie adjustment: {adjustment}")


def render_confidence_finalized(lines, event, analysis):

    lines.append("")
    lines.append("Final Confidence")
    lines.append("----------------")

    lines.append(
        f"{event['score']:.1f}% ({event['label']})"
    )

def render_reasoning_generated(lines, event, analysis):

    lines.append("Overall Confidence")
    lines.append("------------------")
    lines.append("")

    confidence = analysis.confidence

    if confidence is not None:

        lines.append(
            f"{confidence['Score']:.1f}% ({confidence['Label']})"
        )

    lines.append("")


    if event["primary"]:

        lines.append("Primary Evidence")
        lines.append("----------------")

        for factor in event["primary"]:

            lines.append(
                f"+ {factor['name']}"
            )

        lines.append("")


    if event["supporting"]:

        lines.append("Supporting Evidence")
        lines.append("-------------------")

        for factor in event["supporting"]:

            lines.append(
                f"+ {factor['name']}"
            )

        lines.append("")


    if event["uncertainty"]:

        lines.append("Remaining Uncertainty")
        lines.append("---------------------")

        for factor in event["uncertainty"]:

            lines.append(
                f"- {factor['name']}"
            )

        lines.append("")

def render_formula_recovered(lines, event, analysis):

    formula = event.get("formula")

    lines.append("Recovered Formula")
    lines.append("-----------------")

    if formula is None:
        lines.append("Unavailable.")
        return
    
    lines.append(formula)


def render_prediction_started(lines, event, analysis):

    formula = analysis.formula

    lines.append("Using Formula")
    lines.append("-------------")

    if formula is None:
        lines.append("Unavailable.")
    else:
        lines.append(formula)

    lines.append("")

    start = event["starting_index"]
    end = start + event["terms_requested"] - 1

    lines.append(
        f"Predicting terms {start}-{end}"
    )


def render_predictions_generated(lines, event, analysis):

    predictions = analysis.next_terms

    if predictions is None:
        return

    start = event["starting_index"]

    lines.append("")
    lines.append("Generated Terms")
    lines.append("---------------")

    for i, value in enumerate(predictions):

        display = round(value)

        if abs(value - display) < 1e-10:

            value = display

        lines.append(
            f"a({start+i}) = {value}"
        )

def render_verification_completed(lines, event, analysis):

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

    lines.append("")
    lines.append("Candidate Comparison")
    lines.append("-------------------")

    winner = event.get(
        "winner",
        "Unknown"
    )

    alternative = event.get(
        "alternative",
        "Unknown"
    )

    lines.append(
        f"{winner} vs {alternative}"
    )

    lines.append("")

    for reason in event.get(
        "comparison",
        []
    ):
        lines.append(
            f"• {reason}"
        )

def render_family_selected(lines, event, analysis):

    lines.append("")
    lines.append("Why This Family Was Selected")
    lines.append("----------------------------")

    family = event.get(
        "family",
        "Unknown"
    )

    lines.append(
        f"Selected: {family}"
    )

    lines.append("")

    for reason in event.get(
        "reason",
        []
    ):
        lines.append(
            f"✓ {reason}"
        )

def render_reasoning_summary(lines, analysis):

    lines.append("")
    lines.append("Reasoning Summary")
    lines.append("-" * 60)
    lines.append("")

    lines.append(
        "MathExplorer completed a structural analysis of the sequence."
    )

    lines.append("")

    selected = analysis.family

    if selected:

        lines.append(
            f"Final classification: {selected.NAME}"
        )

    confidence = analysis.confidence

    if confidence:

        lines.append(
            f"Confidence: {confidence['Score']:.1f}% "
            f"({confidence['Label']})"
        )

    lines.append("")

    lines.append(
        "The decision was based on:"
    )

    lines.append(
        "• Mathematical accuracy"
    )

    lines.append(
        "• Structural simplicity"
    )

    lines.append(
        "• Family hierarchy consistency"
    )

    lines.append(
        "• Generalization beyond observed terms"
    )

def render_analysis_complete(lines, analysis):

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
    "reasoning_generated": render_reasoning_generated,

    "formula_recovered": render_formula_recovered,

    "prediction_started": render_prediction_started,
    "predictions_generated": render_predictions_generated,

    "verification_completed": render_verification_completed,

    "inference_generated": render_inference_generated,

    "candidate_comparison": render_candidate_comparison,

    "family_selected": render_family_selected,

    "render_reason_summary": render_reasoning_summary,

    "analysis_completed": render_analysis_complete,
}