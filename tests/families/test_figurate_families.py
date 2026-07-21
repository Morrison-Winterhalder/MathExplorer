import pytest

from families.registry import get_family


# ============================================================
# Polygonal Families
# ============================================================

POLYGONAL_CASES = [

    (
        "Triangular Numbers",
        [
            1,
            3,
            6,
            10,
            15,
            21,
        ],
    ),

    (
        "Pentagonal Numbers",
        [
            1,
            5,
            12,
            22,
            35,
            51,
        ],
    ),

    (
        "Hexagonal Numbers",
        [
            1,
            6,
            15,
            28,
            45,
            66,
        ],
    ),

    (
        "Heptagonal Numbers",
        [
            1,
            7,
            18,
            34,
            55,
            81,
        ],
    ),

    (
        "Octagonal Numbers",
        [
            1,
            8,
            21,
            40,
            65,
            96,
        ],
    ),

    (
        "Nonagonal Numbers",
        [
            1,
            9,
            24,
            46,
            75,
            111,
        ],
    ),

    (
        "Decagonal Numbers",
        [
            1,
            10,
            27,
            52,
            85,
            126,
        ],
    ),

]


# ============================================================
# Centered Polygonal Families
# ============================================================

CENTERED_POLYGONAL_CASES = [

    (
        "Centered Triangular Numbers",
        [
            1,
            4,
            10,
            19,
            31,
            46,
        ],
    ),

    (
        "Centered Square Numbers",
        [
            1,
            5,
            13,
            25,
            41,
            61,
        ],
    ),

    (
        "Centered Pentagonal Numbers",
        [
            1,
            6,
            16,
            31,
            51,
            76,
        ],
    ),

    (
        "Centered Hexagonal Numbers",
        [
            1,
            7,
            19,
            37,
            61,
            91,
        ],
    ),

]


ALL_CASES = (

    POLYGONAL_CASES

    +

    CENTERED_POLYGONAL_CASES

)


# ============================================================
# Helpers
# ============================================================

def get_figurate_family(
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
    ALL_CASES,
)
def test_figurate_family_fits_known_sequence(
    family_name,
    sequence,
):

    family = get_figurate_family(
        family_name
    )

    parameters = family.fit(
        sequence
    )

    assert parameters is not None


@pytest.mark.parametrize(
    "family_name, sequence",
    ALL_CASES,
)
def test_figurate_family_reproduces_known_sequence(
    family_name,
    sequence,
):

    family = get_figurate_family(
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
# Future Predictions
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    ALL_CASES,
)
def test_figurate_family_generates_future_terms(
    family_name,
    sequence,
):

    family = get_figurate_family(
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


# ============================================================
# Determinism
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    ALL_CASES,
)
def test_figurate_predictions_are_deterministic(
    family_name,
    sequence,
):

    family = get_figurate_family(
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
# Hierarchy
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    POLYGONAL_CASES,
)
def test_polygonal_family_has_correct_parent(
    family_name,
    sequence,
):

    family = get_figurate_family(
        family_name
    )

    assert family.PARENT == "Polygonal"


@pytest.mark.parametrize(
    "family_name, sequence",
    CENTERED_POLYGONAL_CASES,
)
def test_centered_polygonal_family_has_correct_parent(
    family_name,
    sequence,
):

    family = get_figurate_family(
        family_name
    )

    assert family.PARENT == "Centered Polygonal"


# ============================================================
# Distinctive Mathematical Structure
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    ALL_CASES,
)
def test_figurate_sequences_are_positive(
    family_name,
    sequence,
):

    family = get_figurate_family(
        family_name
    )

    parameters = family.fit(
        sequence
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
            len(sequence) + 1,
        )

    ]

    assert all(
        value > 0
        for value in values
    )


@pytest.mark.parametrize(
    "family_name, sequence",
    ALL_CASES,
)
def test_figurate_sequences_are_non_decreasing(
    family_name,
    sequence,
):

    family = get_figurate_family(
        family_name
    )

    parameters = family.fit(
        sequence
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
            len(sequence) + 1,
        )

    ]

    assert values == sorted(
        values
    )


# ============================================================
# Polygonal Growth
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    POLYGONAL_CASES,
)
def test_polygonal_first_differences_are_arithmetic(
    family_name,
    sequence,
):

    family = get_figurate_family(
        family_name
    )

    parameters = family.fit(
        sequence
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
            len(sequence) + 1,
        )

    ]

    differences = [

        values[i + 1]
        - values[i]

        for i
        in range(
            len(values) - 1
        )

    ]

    second_differences = [

        differences[i + 1]
        - differences[i]

        for i
        in range(
            len(differences) - 1
        )

    ]

    assert len(
        set(
            second_differences
        )
    ) == 1


# ============================================================
# Cross-Family Separation
# ============================================================

def test_triangular_numbers_are_not_square_numbers():

    family = get_figurate_family(
        "Squares"
    )

    parameters = family.fit(
        [
            1,
            3,
            6,
            10,
            15,
            21,
        ]
    )

    assert parameters is None


def test_pentagonal_numbers_are_not_triangular_numbers():

    family = get_figurate_family(
        "Triangular Numbers"
    )

    parameters = family.fit(
        [
            1,
            5,
            12,
            22,
            35,
            51,
        ]
    )

    assert parameters is None