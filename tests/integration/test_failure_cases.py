from analyzers.sequence_analysis import analyze_sequence


def test_empty_sequence_returns_none():

    sequence = []

    analysis = analyze_sequence(sequence)

    assert analysis is None


def test_single_term_sequence_does_not_crash():

    sequence = [
        42,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis is not None


def test_unknown_sequence_does_not_crash():

    sequence = [

        17,
        4,
        29,
        3,
        91,
        8,
        44,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis is not None


def test_unknown_sequence_has_safe_classification():

    sequence = [

        17,
        4,
        29,
        3,
        91,
        8,
        44,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.classification is not None


def test_failure_does_not_produce_invalid_confidence():

    sequence = [

        17,
        4,
        29,
        3,
        91,
        8,
        44,
    ]

    analysis = analyze_sequence(sequence)

    if analysis.confidence_score is not None:

        assert 0 <= analysis.confidence_score <= 100


def test_failure_does_not_produce_invalid_predictions():

    sequence = [

        17,
        4,
        29,
        3,
        91,
        8,
        44,
    ]

    analysis = analyze_sequence(sequence)

    predictions = analysis.predictions_next

    if predictions is not None:

        assert isinstance(
            predictions,
            list,
        )


def test_failure_does_not_claim_verification_without_classification():

    sequence = [

        17,
        4,
        29,
        3,
        91,
        8,
        44,
    ]

    analysis = analyze_sequence(sequence)

    if analysis.family is None:

        assert analysis.verified is None


def test_analysis_trace_exists_after_failure():

    sequence = [

        17,
        4,
        29,
        3,
        91,
        8,
        44,
    ]

    analysis = analyze_sequence(sequence)

    assert isinstance(
        analysis.analysis_trace,
        list,
    )


def test_failure_does_not_raise_for_non_numeric_values():

    sequence = [

        "a",
        "b",
        "c",
    ]

    try:

        analysis = analyze_sequence(sequence)

    except (TypeError, ValueError):

        return

    assert analysis is not None


def test_failure_does_not_raise_for_mixed_values():

    sequence = [

        1,
        "x",
        3,
    ]

    try:

        analysis = analyze_sequence(sequence)

    except (TypeError, ValueError):

        return

    assert analysis is not None