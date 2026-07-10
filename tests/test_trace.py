from analyzers.sequence_analysis import analyze_sequence


def test_pipeline_emits_all_stages():

    report = analyze_sequence([1, 4, 9, 16, 25])

    stages = {
        event["stage"]
        for event in report["Analysis Trace"]
    }

    assert stages == {
        "recognition",
        "ranking",
        "classification",
        "confidence",
        "recovery",
        "prediction",
        "verification",
        "pipeline",
    }


def test_pipeline_stage_order():

    report = analyze_sequence([1, 4, 9, 16, 25])

    seen = []

    for event in report["Analysis Trace"]:

        if event["stage"] not in seen:
            seen.append(event["stage"])

    assert seen == [
        "recognition",
        "ranking",
        "classification",
        "confidence",
        "recovery",
        "prediction",
        "verification",
        "pipeline",
    ]


def test_trace_not_empty():

    report = analyze_sequence([1,4,9,16,25])

    assert len(report["Analysis Trace"]) > 0