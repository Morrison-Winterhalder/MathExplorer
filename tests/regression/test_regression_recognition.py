import pytest

from analyzers.sequence_analysis import analyze_sequence


# ============================================================
# Core Recognition Regression Tests
# ============================================================


@pytest.mark.parametrize(
    "sequence, expected_family",
    [

        # ----------------------------------------------------
        # Basic Families
        # ----------------------------------------------------

        (
            [5, 5, 5, 5, 5],
            "Constant",
        ),

        (
            [1, 3, 5, 7, 9],
            "Arithmetic",
        ),

        (
            [2, 4, 8, 16, 32],
            "Geometric",
        ),

        (
            [1, 4, 9, 16, 25],
            "Squares",
        ),

        (
            [1, 8, 27, 64, 125],
            "Cubes",
        ),

        # ----------------------------------------------------
        # Polynomial / Figurate Families
        # ----------------------------------------------------

        (
            [1, 3, 6, 10, 15, 21],
            "Triangular Numbers",
        ),

        (
            [1, 5, 12, 22, 35],
            "Pentagonal Numbers",
        ),

        (
            [1, 6, 15, 28, 45],
            "Hexagonal Numbers",
        ),

        # ----------------------------------------------------
        # Recursive Families
        # ----------------------------------------------------

        (
            [1, 1, 2, 3, 5, 8, 13],
            "Fibonacci",
        ),

        (
            [2, 1, 3, 4, 7, 11, 18],
            "Lucas Numbers",
        ),

        (
            [0, 1, 2, 5, 12, 29, 70],
            "Pell Numbers",
        ),

        (
            [0, 1, 1, 3, 5, 11, 21],
            "Jacobsthal Numbers",
        ),

        # ----------------------------------------------------
        # Special Families
        # ----------------------------------------------------

        (
            [1, 2, 6, 24, 120],
            "Factorials",
        ),

        (
            [1, 1, 2, 5, 14, 42],
            "Catalan Numbers",
        ),

        (
            [1, 1, 2, 5, 15, 52, 203],
            "Bell Numbers",
        ),

        # ----------------------------------------------------
        # Self-Referential Families
        # ----------------------------------------------------

        (
            [
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
            ],
            "Van Eck Numbers",
        ),
    ],
)
def test_known_sequence_recognizes_correct_family(
    sequence,
    expected_family,
):

    analysis = analyze_sequence(
        sequence
    )

    assert analysis is not None

    assert analysis.family is not None

    assert analysis.family.NAME == (
        expected_family
    )


# ============================================================
# Recognition Stability
# ============================================================


def test_fibonacci_recognition_is_stable():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    first = analyze_sequence(
        sequence
    )

    second = analyze_sequence(
        sequence
    )

    assert first.family is not None

    assert second.family is not None

    assert first.family.NAME == (
        second.family.NAME
    )


def test_bell_recognition_is_stable():

    sequence = [
        1,
        1,
        2,
        5,
        15,
        52,
        203,
    ]

    first = analyze_sequence(
        sequence
    )

    second = analyze_sequence(
        sequence
    )

    assert first.family.NAME == (
        "Bell Numbers"
    )

    assert second.family.NAME == (
        "Bell Numbers"
    )


def test_van_eck_recognition_is_stable():

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

    first = analyze_sequence(
        sequence
    )

    second = analyze_sequence(
        sequence
    )

    assert first.family.NAME == (
        "Van Eck Numbers"
    )

    assert second.family.NAME == (
        "Van Eck Numbers"
    )


# ============================================================
# Regression: Specific Families Must Beat Polynomial Fallback
# ============================================================


def test_bell_numbers_do_not_regress_to_polynomial():

    sequence = [
        1,
        1,
        2,
        5,
        15,
        52,
        203,
    ]

    analysis = analyze_sequence(
        sequence
    )

    assert analysis.family.NAME != (
        "Polynomial"
    )

    assert analysis.family.NAME == (
        "Bell Numbers"
    )


def test_van_eck_numbers_do_not_regress_to_polynomial():

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

    analysis = analyze_sequence(
        sequence
    )

    assert analysis.family.NAME != (
        "Polynomial"
    )

    assert analysis.family.NAME == (
        "Van Eck Numbers"
    )


def test_factorials_do_not_regress_to_polynomial():

    sequence = [
        1,
        2,
        6,
        24,
        120,
    ]

    analysis = analyze_sequence(
        sequence
    )

    assert analysis.family.NAME != (
        "Polynomial"
    )

    assert analysis.family.NAME == (
        "Factorials"
    )


# ============================================================
# Recognition Must Produce a Valid Analysis
# ============================================================


@pytest.mark.parametrize(
    "sequence",
    [

        [1, 3, 5, 7, 9],

        [2, 4, 8, 16, 32],

        [1, 1, 2, 3, 5, 8, 13],

        [1, 2, 6, 24, 120],

        [1, 1, 2, 5, 15, 52, 203],

        [
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
        ],
    ],
)
def test_recognition_returns_complete_analysis(
    sequence,
):

    analysis = analyze_sequence(
        sequence
    )

    assert analysis is not None

    assert analysis.family is not None

    assert analysis.recognition_scores is not None

    assert analysis.confidence is not None

    assert analysis.hierarchy is not None


# ============================================================
# Recognition Must Be Deterministic
# ============================================================


@pytest.mark.parametrize(
    "sequence",
    [

        [1, 3, 5, 7, 9],

        [2, 4, 8, 16, 32],

        [1, 1, 2, 3, 5, 8, 13],

        [1, 2, 6, 24, 120],

        [1, 1, 2, 5, 15, 52, 203],
    ],
)
def test_recognition_is_deterministic(
    sequence,
):

    analyses = [
        analyze_sequence(
            sequence
        )
        for _ in range(3)
    ]

    family_names = [
        analysis.family.NAME
        for analysis in analyses
    ]

    assert len(
        set(
            family_names
        )
    ) == 1


# ============================================================
# Recognition Must Not Mutate Input
# ============================================================


@pytest.mark.parametrize(
    "sequence",
    [

        [1, 3, 5, 7, 9],

        [1, 1, 2, 3, 5, 8, 13],

        [1, 2, 6, 24, 120],

        [1, 1, 2, 5, 15, 52, 203],
    ],
)
def test_recognition_does_not_mutate_input(
    sequence,
):

    original = sequence.copy()

    analyze_sequence(
        sequence
    )

    assert sequence == (
        original
    )


# ============================================================
# Regression: Recognition Must Respect Family Specificity
# ============================================================


def test_specific_family_beats_generic_polynomial_fit():

    sequence = [
        1,
        1,
        2,
        5,
        15,
        52,
        203,
    ]

    analysis = analyze_sequence(
        sequence
    )

    assert analysis.family.NAME == (
        "Bell Numbers"
    )


def test_recursive_family_beats_polynomial_interpolation():

    sequence = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
    ]

    analysis = analyze_sequence(
        sequence
    )

    assert analysis.family.NAME == (
        "Fibonacci"
    )


def test_special_family_beats_polynomial_interpolation():

    sequence = [
        1,
        2,
        6,
        24,
        120,
    ]

    analysis = analyze_sequence(
        sequence
    )

    assert analysis.family.NAME == (
        "Factorials"
    )


# ============================================================
# Final Recognition Regression Sanity Check
# ============================================================


def test_all_core_recognition_regressions():

    cases = [

        (
            [5, 5, 5, 5, 5],
            "Constant",
        ),

        (
            [1, 3, 5, 7, 9],
            "Arithmetic",
        ),

        (
            [2, 4, 8, 16, 32],
            "Geometric",
        ),

        (
            [1, 1, 2, 3, 5, 8, 13],
            "Fibonacci",
        ),

        (
            [1, 2, 6, 24, 120],
            "Factorials",
        ),

        (
            [1, 1, 2, 5, 15, 52, 203],
            "Bell Numbers",
        ),

    ]

    for sequence, expected_family in cases:

        analysis = analyze_sequence(
            sequence
        )

        assert analysis is not None

        assert analysis.family is not None

        assert analysis.family.NAME == (
            expected_family
        )