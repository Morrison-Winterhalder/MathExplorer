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
        "Squares",
        [1, 4, 9, 16, 25, 36],
    ),

    (
        "Cubes",
        [1, 8, 27, 64, 125, 216],
    ),

    (
        "Fourth Powers",
        [1, 16, 81, 256, 625, 1296],
    ),

    (
        "Fifth Powers",
        [1, 32, 243, 1024, 3125, 7776],
    ),

    (
        "Triangular Numbers",
        [1, 3, 6, 10, 15, 21],
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
# Helpers
# ============================================================

def get_family_and_parameters(
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

    assert parameters is not None

    return family, parameters


# ============================================================
# Prediction Generation
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_family_can_generate_future_terms(
    family_name,
    sequence,
):

    family, parameters = (

        get_family_and_parameters(
            family_name,
            sequence,
        )

    )

    future_terms = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            len(sequence) + 1,
            len(sequence) + 4,
        )

    ]

    assert len(
        future_terms
    ) == 3


@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_future_terms_are_numeric(
    family_name,
    sequence,
):

    family, parameters = (

        get_family_and_parameters(
            family_name,
            sequence,
        )

    )

    future_terms = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            len(sequence) + 1,
            len(sequence) + 4,
        )

    ]

    assert all(

        isinstance(
            term,
            (
                int,
                float,
            ),
        )

        for term
        in future_terms

    )


# ============================================================
# Prediction Continuity
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_predictions_preserve_observed_sequence(
    family_name,
    sequence,
):

    family, parameters = (

        get_family_and_parameters(
            family_name,
            sequence,
        )

    )

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


# ============================================================
# Prediction Determinism
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_predictions_are_deterministic(
    family_name,
    sequence,
):

    family, parameters = (

        get_family_and_parameters(
            family_name,
            sequence,
        )

    )

    first = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            len(sequence) + 1,
            len(sequence) + 4,
        )

    ]

    second = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            len(sequence) + 1,
            len(sequence) + 4,
        )

    ]

    assert first == second


# ============================================================
# Prediction Stability
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    FAMILY_CASES,
)
def test_repeated_predictions_do_not_mutate_parameters(
    family_name,
    sequence,
):

    family, parameters = (

        get_family_and_parameters(
            family_name,
            sequence,
        )

    )

    original_parameters = parameters

    family.evaluate(
        parameters,
        len(sequence) + 1,
    )

    family.evaluate(
        parameters,
        len(sequence) + 2,
    )

    family.evaluate(
        parameters,
        len(sequence) + 3,
    )

    assert parameters == original_parameters