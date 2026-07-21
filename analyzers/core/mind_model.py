from analyzers.core.trace import events_for_stage
from analyzers.core.event_renderers import EVENT_RENDERERS, render_reasoning_summary, render_analysis_complete

STAGES = [
    "recognition",
    "classification",
    "confidence",
    "recovery",
    "prediction",
    "verification",
]


def render_stage(lines, report, stage):
    """
    Render one pipeline stage from the Analysis Trace.
    """

    stage_events = events_for_stage(report, stage)

    if not stage_events:
        return

    section = []

    for event in stage_events:

        renderer = EVENT_RENDERERS.get(event["event"])

        if renderer is not None:
            renderer(section, event, report)

    # Skip completely empty stages
    if not section:
        return
    
    if not any(line.strip() for line in section):
        return

    titles = {
        "observation": "Observations",
        "recognition": "Recognition",
        "classification": "Classification",
        "confidence": "Confidence",
        "recovery": "Formula",
        "prediction": "Prediction",
        "verification": "Verification",
    }

    lines.append(titles.get(stage, stage.title()))
    lines.append("-" * 52)
    lines.append("")

    lines.extend(section)
    lines.append("")


def render_mind_model(report):
    """
    Render the developer mind-model directly from the Analysis Trace.
    """

    trace = report.get("Analysis Trace", [])

    if not trace:
        return "No analysis trace available."

    lines = []

    lines.append("=" * 60)
    lines.append("        MathExplorer Developer Mind-Model")
    lines.append("=" * 60)
    lines.append("")

    for stage in STAGES:
        render_stage(lines, report, stage)
    
    lines.append("")

    render_reasoning_summary(lines, report)
    render_analysis_complete(lines, report)

    return "\n".join(lines)