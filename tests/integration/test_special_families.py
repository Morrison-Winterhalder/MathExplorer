from analyzers.sequence_analysis import analyze_sequence


# ==========================================================
# Factorial Numbers
# ==========================================================

def test_factorial_pipeline():

    sequence = [
        1,
        2,
        6,
        24,
        120,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Factorials"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        720,
        5040,
        40320,
        362880,
        3628800,
    ]



# ==========================================================
# Bell Numbers
# ==========================================================

def test_bell_pipeline():

    sequence = [
        1,
        1,
        2,
        5,
        15,
        52,
        203,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Bell Numbers"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        877,
        4140,
        21147,
        115975,
        678570,
    ]



# ==========================================================
# Catalan Numbers
# ==========================================================

def test_catalan_pipeline():

    sequence = [
        1,
        1,
        2,
        5,
        14,
        42,
        132,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Catalan Numbers"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        429,
        1430,
        4862,
        16796,
        58786,
    ]



# ==========================================================
# Van Eck Sequence
# ==========================================================

def test_van_eck_pipeline():

    sequence = [
        0,
        0,
        1,
        0,
        2,
        0,
        2,
        2,
        1,
        6,
        0,
        5,
        0,
        2,
        6,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Van Eck Numbers"
    )

    assert analysis.verified is True

    assert analysis.predictions_next is not None



# ==========================================================
# Special Family Hierarchy
# ==========================================================

def test_special_family_hierarchy():

    sequence = [
        1,
        2,
        6,
        24,
        120,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.PARENT == (
        "Special"
    )

    assert (
        "Explicit"
        in analysis.hierarchy
    )



# ==========================================================
# Special Pipeline Trace
# ==========================================================

def test_special_pipeline_trace():

    sequence = [
        1,
        2,
        6,
        24,
        120,
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