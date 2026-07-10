from analyzers.sequence_analysis import analyze_sequence


def test_mind_model_exists():

    report = analyze_sequence([1,4,9,16,25])

    assert "Developer Mind-Model" in report


def test_mind_model_is_string():

    report = analyze_sequence([1,4,9,16,25])

    assert isinstance(
        report["Developer Mind-Model"],
        str
    )


def test_mind_model_contains_sections():

    report = analyze_sequence([1,4,9,16,25])

    model = report["Developer Mind-Model"]

    for section in (
        "Recognition",
        "Classification",
        "Confidence",
        "Formula",
        "Prediction",
        "Verification",
        "Reasoning Summary",
        "Analysis Complete",
    ):
        assert section in model


def test_mind_model_contains_formula():

    report = analyze_sequence([1,4,9,16,25])

    model = report["Developer Mind-Model"]

    assert "a(n)" in model


def test_mind_model_contains_family():

    report = analyze_sequence([1,4,9,16,25])

    assert "Squares" in report["Developer Mind-Model"]


def test_mind_model_contains_verification():

    report = analyze_sequence([1,4,9,16,25])

    model = report["Developer Mind-Model"]

    assert "Verification Passed" in model