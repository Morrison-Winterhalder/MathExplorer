from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.trace import (
    first_event,
    last_event,
    has_event,
    events,
    events_for_stage,
)


def test_first_event():

    report = analyze_sequence([1,4,9,16,25])

    event = first_event(report, "family_tested")

    assert event is not None
    assert event["stage"] == "recognition"
    assert event["event"] == "family_tested"


def test_last_event():

    report = analyze_sequence([1,4,9,16,25])

    event = last_event(report, "analysis_completed")

    assert event is not None
    assert event["stage"] == "pipeline"


def test_has_event():

    report = analyze_sequence([1,4,9,16,25])

    assert has_event(report, "confidence_finalized")


def test_events_filter():

    report = analyze_sequence([1,4,9,16,25])

    confidence_events = events(
        report,
        stage="confidence"
    )

    assert len(confidence_events) > 0

    for event in confidence_events:
        assert event["stage"] == "confidence"


def test_events_for_stage():

    report = analyze_sequence([1,4,9,16,25])

    stage = events_for_stage(
        report,
        "prediction"
    )

    assert len(stage) > 0

    for event in stage:
        assert event["stage"] == "prediction"