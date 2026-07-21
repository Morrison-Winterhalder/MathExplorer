import pytest

from families.registry import get_family


# ============================================================
# Known Valid Family Sequences
# ============================================================

FAMILY_CASES = [

    (
        "Arithmetic",
        [1, 2, 3, 4, 5, 6],
    ),

    (
        "Geometric",
        [1, 2, 4, 8, 16, 32],
    ),

    (
        "Constant",
        [7, 7, 7, 7, 7, 7],
    ),

    (
        "Polynomial",
        [1, 4, 9, 16, 25, 36],
    ),

    (
        "Squares",
        [1, 4, 9, 16, 25, 36],
    ),

    (
        "Cubes",
        [1, 8, 27, 64, 125, 216],
    ),

    (
        "Fourth Powers",
        [1, 16, 81, 256, 625],
    ),

    (
        "Fifth Powers",
        [1, 32, 243, 1024, 3125],
    ),

    (
        "Triangular Numbers",
        [1, 3, 6, 10, 15, 21],
    ),

    (
        "Pentagonal Numbers",
        [1, 5, 12, 22, 35, 51],
    ),

    (
        "Hexagonal Numbers",
        [1, 6, 15, 28, 45, 66],
    ),

    (
        "Fibonacci",
        [1, 1, 2, 3, 5, 8, 13],
    ),

    (
        "Lucas Numbers",
        [2, 1, 3, 4, 7, 11, 18],
    ),

    (
        "Pell Numbers",
        [0, 1, 2, 5, 12, 29, 70],
    ),

    (
        "Jacobsthal Numbers",
        [0, 1, 1, 3, 5, 11, 21],
    ),

    (
        "Tribonacci Numbers",
        [0, 0, 1, 1, 2, 4, 7, 13],
    ),

    (
        "Factorials",
        [1, 2, 6, 24, 120, 720],
    ),

]


# ============================================================
# Fit / Evaluate Consistency
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_family_fit_returns_parameters_for_known_sequence(
    family_name,
    sequence,
):

    family = get_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is not None


@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_family_evaluate_reproduces_known_sequence(
    family_name,
    sequence,
):

    family = get_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is not None

    predicted = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            1,
            len(sequence) + 1,
        )

    ]

    assert predicted == sequence


@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_family_fit_evaluate_is_deterministic(
    family_name,
    sequence,
):

    family = get_family(
        family_name
    )

    first_parameters = family.fit(
        sequence
    )

    second_parameters = family.fit(
        sequence
    )

    assert first_parameters == second_parameters

    first_predictions = [

        family.evaluate(
            first_parameters,
            n,
        )

        for n
        in range(
            1,
            len(sequence) + 1,
        )

    ]

    second_predictions = [

        family.evaluate(
            second_parameters,
            n,
        )

        for n
        in range(
            1,
            len(sequence) + 1,
        )

    ]

    assert first_predictions == second_predictions