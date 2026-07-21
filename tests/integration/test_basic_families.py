from analyzers.sequence_analysis import analyze_sequence


# ==========================================================
# Constant Numbers
# ==========================================================

def test_constant_numbers_pipeline():

    sequence = [
        7,
        7,
        7,
        7,
        7,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Constant"
    )

    assert analysis.verified is True

    assert analysis.predictions_next is not None



# ==========================================================
# Arithmetic Numbers
# ==========================================================

def test_arithmetic_numbers_pipeline():

    sequence = [
        2,
        4,
        6,
        8,
        10,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Arithmetic"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        12,
        14,
        16,
        18,
        20,
    ]



# ==========================================================
# Geometric Numbers
# ==========================================================

def test_geometric_numbers_pipeline():

    sequence = [
        3,
        9,
        27,
        81,
        243,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME == (
        "Geometric"
    )

    assert analysis.verified is True

    assert analysis.predictions_next == [
        729,
        2187,
        6561,
        19683,
        59049,
    ]



# ==========================================================
# Polynomial Numbers
# ==========================================================

def test_polynomial_numbers_pipeline():

    sequence = [
        1,
        4,
        9,
        16,
        25,
    ]

    analysis = analyze_sequence(sequence)

    assert analysis.family is not None

    assert analysis.family.NAME in [
        "Polynomial Numbers",
        "Squares",
    ]

    assert analysis.verified is True

    assert analysis.predictions_next is not None



# ==========================================================
# Basic Family Pipeline Integrity
# ==========================================================

def test_basic_family_pipeline_generates_trace():

    sequence = [
        2,
        4,
        6,
        8,
        10,
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