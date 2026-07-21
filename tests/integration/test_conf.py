from analyzers.sequence_analysis import analyze_sequence


def test_confidence_is_generated_for_strong_recognition():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.confidence is not None

    assert analysis.confidence_score is not None

    assert 0 <= analysis.confidence_score <= 100


def test_confidence_contains_factors():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.confidence is not None

    assert analysis.confidence_factors is not None

    assert isinstance(
        analysis.confidence_factors,
        list,
    )


def test_confidence_contains_label():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.confidence_label is not None

    assert isinstance(
        analysis.confidence_label,
        str,
    )

def test_confidence_trace_contains_reasoning():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    reasoning_events = [

        event

        for event in analysis.analysis_trace

        if (
            event.get("stage") == "confidence"
            and
            event.get("event") == "reasoning_generated"
        )

    ]

    assert reasoning_events

    reasoning = reasoning_events[-1]

    assert "primary" in reasoning

    assert "supporting" in reasoning

    assert "uncertainty" in reasoning


def test_confidence_has_primary_or_supporting_reasoning():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    reasoning_events = [

        event

        for event in analysis.analysis_trace

        if (
            event.get("stage") == "confidence"
            and
            event.get("event") == "reasoning_generated"
        )

    ]

    assert reasoning_events

    reasoning = reasoning_events[-1]

    assert (

        reasoning["primary"]

        or

        reasoning["supporting"]

        or

        reasoning["uncertainty"]

    )


def test_confidence_score_is_numeric():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    assert isinstance(
        analysis.confidence_score,
        (int, float),
    )


def test_confidence_factors_have_expected_structure():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(sequence)

    factors = analysis.confidence_factors

    assert factors

    for factor in factors:

        assert isinstance(
            factor,
            dict,
        )

        assert "impact" in factor