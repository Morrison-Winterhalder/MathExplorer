import pytest

from families.registry import get_family


# ============================================================
# Combinatorial Families
# ============================================================

COMBINATORIAL_CASES = [

    (
        "Catalan Numbers",
        [
            1,
            1,
            2,
            5,
            14,
            42,
            132,
        ],
    ),

    (
        "Bell Numbers",
        [
            1,
            1,
            2,
            5,
            15,
            52,
            203,
        ],
    ),

    (
        "Derangement Numbers",
        [
            0,
            1,
            2,
            9,
            44,
            265,
            1854,
        ],
    ),

    (
        "Partition Numbers",
        [
            1,
            2,
            3,
            5,
            7,
            11,
            15,
        ],
    ),

    (
        "Schröder Numbers",
        [
            1,
            2,
            6,
            22,
            90,
            394,
        ],
    ),

]


# ============================================================
# Helpers
# ============================================================

def get_combinatorial_family(
    family_name,
):

    family = get_family(
        family_name
    )

    assert family is not None

    return family


# ============================================================
# Recognition
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    COMBINATORIAL_CASES,
)
def test_combinatorial_family_fits_known_sequence(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is not None


@pytest.mark.parametrize(
    "family_name, sequence",
    COMBINATORIAL_CASES,
)
def test_combinatorial_family_reproduces_known_sequence(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
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


# ============================================================
# Future Terms
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    COMBINATORIAL_CASES,
)
def test_combinatorial_family_generates_future_terms(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is not None

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
    COMBINATORIAL_CASES,
)
def test_combinatorial_family_predictions_are_deterministic(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is not None

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
# Metadata
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    COMBINATORIAL_CASES,
)
def test_combinatorial_family_has_correct_parent(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
        family_name
    )

    assert family.PARENT == "Combinatorial"


@pytest.mark.parametrize(
    "family_name, sequence",
    COMBINATORIAL_CASES,
)
def test_combinatorial_family_has_expected_category(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
        family_name
    )

    assert family.CATEGORY == "Combinatorial"


# ============================================================
# Distinctive Structural Checks
# ============================================================

def test_catalan_numbers_are_positive_after_initial_terms():

    family = get_combinatorial_family(
        "Catalan Numbers"
    )

    parameters = family.fit(
        [
            1,
            1,
            2,
            5,
            14,
            42,
        ]
    )

    assert parameters is not None

    assert all(

        family.evaluate(
            parameters,
            n,
        ) > 0

        for n
        in range(
            1,
            7,
        )

    )


def test_bell_numbers_are_non_decreasing():

    family = get_combinatorial_family(
        "Bell Numbers"
    )

    parameters = family.fit(
        [
            1,
            1,
            2,
            5,
            15,
            52,
        ]
    )

    assert parameters is not None

    values = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            1,
            7,
        )

    ]

    assert values == sorted(
        values
    )


def test_partition_numbers_are_non_decreasing():

    family = get_combinatorial_family(
        "Partition Numbers"
    )

    parameters = family.fit(
        [
            1,
            2,
            3,
            5,
            7,
            11,
        ]
    )

    assert parameters is not None

    values = [

        family.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            1,
            7,
        )

    ]

    assert values == sorted(
        values
    )


# ============================================================
# Cross-Family Rejection
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    [

        (
            "Catalan Numbers",
            [
                1,
                1,
                2,
                3,
                5,
                8,
                13,
            ],
        ),

        (
            "Bell Numbers",
            [
                1,
                1,
                2,
                3,
                5,
                8,
                13,
            ],
        ),

        (
            "Partition Numbers",
            [
                1,
                2,
                4,
                8,
                16,
                32,
            ],
        ),

    ],
)
def test_combinatorial_family_rejects_obvious_unrelated_sequence(
    family_name,
    sequence,
):

    family = get_combinatorial_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is None