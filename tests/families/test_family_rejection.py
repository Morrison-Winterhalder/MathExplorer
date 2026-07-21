import pytest

from families.registry import get_family


# ============================================================
# Families That Should Reject These Sequences
# ============================================================

REJECTION_CASES = [

    (
        "Arithmetic",
        [1, 1, 2, 3, 5, 8, 13],
    ),

    (
        "Geometric",
        [1, 1, 2, 3, 5, 8, 13],
    ),

    (
        "Fibonacci",
        [1, 2, 6, 24, 120, 720],
    ),

    (
        "Factorials",
        [1, 1, 2, 3, 5, 8, 13],
    ),

    (
        "Squares",
        [1, 2, 3, 4, 5, 6],
    ),

    (
        "Cubes",
        [1, 4, 9, 16, 25, 36],
    ),

    (
        "Pell Numbers",
        [1, 1, 2, 3, 5, 8, 13],
    ),

    (
        "Jacobsthal Numbers",
        [1, 1, 2, 3, 5, 8, 13],
    ),

]


# ============================================================
# Rejection Tests
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    REJECTION_CASES,
)
def test_family_rejects_unrelated_sequence(
    family_name,
    sequence,
):

    family = get_family(
        family_name
    )

    assert family is not None

    parameters = family.fit(
        sequence
    )

    assert parameters is None


# ============================================================
# Cross-Family Rejection
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    [

        (
            "Arithmetic",
            [1, 2, 4, 8, 16, 32],
        ),

        (
            "Geometric",
            [1, 2, 3, 4, 5, 6],
        ),

        (
            "Fibonacci",
            [1, 2, 6, 24, 120, 720],
        ),

        (
            "Factorials",
            [1, 1, 2, 3, 5, 8, 13],
        ),

        (
            "Squares",
            [1, 8, 27, 64, 125, 216],
        ),

        (
            "Cubes",
            [1, 4, 9, 16, 25, 36],
        ),

    ],
)
def test_family_does_not_accept_obvious_competing_family(
    family_name,
    sequence,
):

    family = get_family(
        family_name
    )

    assert family is not None

    parameters = family.fit(
        sequence
    )

    assert parameters is None


# ============================================================
# Rejection Determinism
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    REJECTION_CASES,
)
def test_rejection_is_deterministic(
    family_name,
    sequence,
):

    family = get_family(
        family_name
    )

    first = family.fit(
        sequence
    )

    second = family.fit(
        sequence
    )

    assert first == second