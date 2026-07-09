from analyzers.sequence_analysis import analyze_sequence


def test_explanation_exists():

    report = analyze_sequence([1,4,9,16,25])

    assert report["Explanation"] is not None
    assert len(report["Explanation"]["Reasons"]) >= 2


def test_explanation_has_summary():

    report = analyze_sequence([1,4,9,16,25])

    assert report["Explanation"]["Summary"] != ""


def test_explanation_has_reasons():

    report = analyze_sequence([1,4,9,16,25])

    assert len(report["Explanation"]["Reasons"]) > 0
    