from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.mind_model import render_mind_model
from analyzers.core.event_renderers import EVENT_RENDERERS


def test_every_event_has_stage_and_event():

    report = analyze_sequence([1,4,9,16,25])

    for event in report["Analysis Trace"]:

        assert "stage" in event
        assert "event" in event


def test_all_registered_renderers_are_callable():

    for renderer in EVENT_RENDERERS.values():
        assert callable(renderer)

def test_mind_model_renders():

    report = analyze_sequence([1,4,9,16,25])

    text = render_mind_model(report)

    assert isinstance(text, str)
    assert len(text) > 0

def test_mind_model_contains_all_sections():

    report = analyze_sequence([1,4,9,16,25])

    text = render_mind_model(report)

    for heading in (
        "Recognition",
        "Classification",
        "Confidence",
        "Formula",
        "Prediction",
        "Verification",
        "Reasoning Summary",
        "Analysis Complete",
    ):
        assert heading in text

def test_reasoning_summary_present():

    report = analyze_sequence([1,4,9,16,25])

    text = render_mind_model(report)

    assert "Reasoning Summary" in text
    assert "Selected Squares" in text
    assert "Verification succeeded." in text

def test_pipeline_begins_with_recognition():

    report = analyze_sequence([1,4,9,16,25])

    first = report["Analysis Trace"][0]

    assert first["stage"] == "recognition"


def test_pipeline_finishes_correctly():

    report = analyze_sequence([1,4,9,16,25])

    last = report["Analysis Trace"][-1]

    assert last["event"] == "analysis_completed"


def test_trace_contains_many_events():

    report = analyze_sequence([1,4,9,16,25])

    assert len(report["Analysis Trace"]) >= 20