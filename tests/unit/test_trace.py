from analyzers.core.trace import (
    events,
    events_for_stage,
    first_event,
    last_event,
    has_event,
    count_events,
    stages,
    unique_events,
)


def sample_report():

    return {
        "Analysis Trace": [
            {
                "stage": "Recognition",
                "event": "family_tested",
                "family": "Arithmetic",
            },
            {
                "stage": "Recognition",
                "event": "family_tested",
                "family": "Geometric",
            },
            {
                "stage": "Scoring",
                "event": "score_updated",
                "score": 75,
            },
            {
                "stage": "Scoring",
                "event": "confidence_updated",
                "confidence": 80,
            },
            {
                "stage": "Prediction",
                "event": "prediction_started",
            },
            {
                "stage": "Prediction",
                "event": "prediction_finished",
            },
        ]
    }


# ==========================================================
# events()
# ==========================================================

def test_events_returns_all_events():

    report = sample_report()

    result = events(report)

    assert len(result) == 6


def test_events_empty_report():

    assert events({}) == []


def test_events_filter_stage():

    report = sample_report()

    result = events(
        report,
        stage="Recognition"
    )

    assert len(result) == 2
    assert all(
        event["stage"] == "Recognition"
        for event in result
    )


def test_events_filter_event():

    report = sample_report()

    result = events(
        report,
        event="family_tested"
    )

    assert len(result) == 2


def test_events_filter_stage_and_event():

    report = sample_report()

    result = events(
        report,
        stage="Prediction",
        event="prediction_started"
    )

    assert len(result) == 1
    assert result[0]["event"] == "prediction_started"


def test_events_missing_filter_returns_empty():

    report = sample_report()

    assert events(
        report,
        event="missing"
    ) == []


# ==========================================================
# events_for_stage()
# ==========================================================

def test_events_for_stage():

    report = sample_report()

    result = events_for_stage(
        report,
        "Scoring"
    )

    assert len(result) == 2


# ==========================================================
# first_event()
# ==========================================================

def test_first_event():

    report = sample_report()

    result = first_event(
        report,
        "family_tested"
    )

    assert result["family"] == "Arithmetic"


def test_first_event_missing():

    report = sample_report()

    assert first_event(
        report,
        "unknown"
    ) is None


# ==========================================================
# last_event()
# ==========================================================

def test_last_event():

    report = sample_report()

    result = last_event(
        report,
        "family_tested"
    )

    assert result["family"] == "Geometric"


def test_last_event_missing():

    report = sample_report()

    assert last_event(
        report,
        "unknown"
    ) is None


# ==========================================================
# has_event()
# ==========================================================

def test_has_event_true():

    report = sample_report()

    assert has_event(
        report,
        "score_updated"
    ) is True


def test_has_event_false():

    report = sample_report()

    assert has_event(
        report,
        "missing"
    ) is False


# ==========================================================
# count_events()
# ==========================================================

def test_count_events_all():

    report = sample_report()

    assert count_events(report) == 6


def test_count_events_by_event():

    report = sample_report()

    assert count_events(
        report,
        event="family_tested"
    ) == 2


def test_count_events_by_stage():

    report = sample_report()

    assert count_events(
        report,
        stage="Prediction"
    ) == 2


def test_count_events_combined():

    report = sample_report()

    assert count_events(
        report,
        stage="Prediction",
        event="prediction_finished"
    ) == 1


# ==========================================================
# stages()
# ==========================================================

def test_stages_preserves_order():

    report = sample_report()

    assert stages(report) == [
        "Recognition",
        "Scoring",
        "Prediction",
    ]


def test_stages_empty():

    assert stages({}) == []


# ==========================================================
# unique_events()
# ==========================================================

def test_unique_events_preserves_order():

    report = sample_report()

    assert unique_events(report) == [
        "family_tested",
        "score_updated",
        "confidence_updated",
        "prediction_started",
        "prediction_finished",
    ]


def test_unique_events_empty():

    assert unique_events({}) == []