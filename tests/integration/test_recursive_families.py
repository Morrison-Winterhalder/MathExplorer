from analyzers.sequence_analysis import analyze_sequence


# ==========================================================
# Fibonacci Numbers
# ==========================================================

def test_fibonacci_pipeline():

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

    assert analysis.family.NAME == (
        "Fibonacci"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        21,
        34,
        55,
        89,
        144,
    ]



# ==========================================================
# Lucas Numbers
# ==========================================================

def test_lucas_pipeline():

    sequence = [
        2,
        1,
        3,
        4,
        7,
        11,
        18,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Lucas Numbers"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        29,
        47,
        76,
        123,
        199,
    ]



# ==========================================================
# Pell Numbers
# ==========================================================

def test_pell_pipeline():

    sequence = [
        0,
        1,
        2,
        5,
        12,
        29,
        70,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Pell Numbers"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        169,
        408,
        985,
        2378,
        5741,
    ]



# ==========================================================
# Recurrence Hierarchy Verification
# ==========================================================

def test_recursive_family_hierarchy():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.PARENT == (
        "Linear Recurrence"
    )

    assert (
        "Recursive"
        in analysis.hierarchy
    )



# ==========================================================
# Recursive Pipeline Trace
# ==========================================================

def test_recursive_pipeline_trace():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
    ]

    analysis = analyze_sequence(sequence)

    events = [
        entry["event"]
        for entry in analysis.trace
    ]

    assert (
        "family_tested"
        in events
    )

    assert (
        "family_selected"
        in events
    )

    assert (
        "verification_completed"
        in events
    )