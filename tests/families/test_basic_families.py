import pytest

from families.registry import get_family


# ============================================================
# Basic Family Definitions
# ============================================================

BASIC_FAMILIES = [

    "Constant",
    "Arithmetic",
    "Geometric",
    "Polynomial",

]


POLYNOMIAL_CHILDREN = [

    "Cubes",
    "Squares",
    "Fifth Powers",
    "Fourth Powers",
    "Pronic Numbers",

]


# ============================================================
# Known Sequences
# ============================================================

BASIC_CASES = [

    (
        "Constant",
        [7, 7, 7, 7, 7, 7],
    ),

    (
        "Arithmetic",
        [2, 5, 8, 11, 14, 17],
    ),

    (
        "Geometric",
        [3, 6, 12, 24, 48, 96],
    ),

    (
        "Polynomial",
        [1, 4, 9, 16, 25, 36],
    ),

]


POLYNOMIAL_CASES = [

    (
        "Cubes",
        [1, 8, 27, 64, 125, 216],
    ),

    (
        "Squares",
        [1, 4, 9, 16, 25, 36],
    ),

    (
        "Fifth Powers",
        [1, 32, 243, 1024, 3125],
    ),

    (
        "Fourth Powers",
        [1, 16, 81, 256, 625],
    ),

    (
        "Pronic Numbers",
        [0, 2, 6, 12, 20, 30],
    ),

]


# ============================================================
# Helpers
# ============================================================

def family(
    name,
):

    result = get_family(
        name
    )

    assert result is not None

    return result


# ============================================================
# Basic Family Recognition
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    BASIC_CASES,
)
def test_basic_family_fits_known_sequence(
    family_name,
    sequence,
):

    target = family(
        family_name
    )

    parameters = target.fit(
        sequence
    )

    assert parameters is not None


@pytest.mark.parametrize(
    "family_name, sequence",
    BASIC_CASES,
)
def test_basic_family_reproduces_known_sequence(
    family_name,
    sequence,
):

    target = family(
        family_name
    )

    parameters = target.fit(
        sequence
    )

    assert parameters is not None

    predicted = [

        target.evaluate(
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
# Polynomial Child Families
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    POLYNOMIAL_CASES,
)
def test_polynomial_child_fits_known_sequence(
    family_name,
    sequence,
):

    target = family(
        family_name
    )

    parameters = target.fit(
        sequence
    )

    assert parameters is not None


@pytest.mark.parametrize(
    "family_name, sequence",
    POLYNOMIAL_CASES,
)
def test_polynomial_child_reproduces_known_sequence(
    family_name,
    sequence,
):

    target = family(
        family_name
    )

    parameters = target.fit(
        sequence
    )

    assert parameters is not None

    if family_name == "Pronic Numbers":

        start = 0

    else:

        start = 1

    predicted = [

        target.evaluate(
            parameters,
            n,
        )

        for n
        in range(
            start,
            start + len(sequence),
        )

    ]

    assert predicted == sequence


# ============================================================
# Parent Relationships
# ============================================================

def test_basic_families_have_expected_parent():

    for name in BASIC_FAMILIES:

        target = family(
            name
        )

        assert target.PARENT == "Basic"


def test_polynomial_children_have_expected_parent():

    for name in POLYNOMIAL_CHILDREN:

        target = family(
            name
        )

        assert target.PARENT == "Polynomial"


# ============================================================
# Polynomial Child Complexity
# ============================================================

@pytest.mark.parametrize(
    "family_name, sequence",
    POLYNOMIAL_CASES,
)
def test_polynomial_children_are_more_specific_than_polynomial(
    family_name,
    sequence,
):

    child = family(
        family_name
    )

    polynomial = family(
        "Polynomial"
    )

    child_parameters = child.fit(
        sequence
    )

    polynomial_parameters = polynomial.fit(
        sequence
    )

    assert child_parameters is not None

    assert polynomial_parameters is not None

    child_complexity = child.complexity(
        child_parameters
    )

    polynomial_complexity = polynomial.complexity(
        polynomial_parameters
    )

    assert child_complexity < polynomial_complexity


# ============================================================
# Basic Family Separation
# ============================================================

def test_constant_sequence_is_compatible_with_arithmetic():

    target = family(
        "Arithmetic"
    )

    parameters = target.fit(
        [7, 7, 7, 7, 7, 7]
    )

    assert parameters is not None

    assert parameters["Difference"] == 0

    assert parameters["Intercept"] == 7


def test_arithmetic_sequence_is_not_geometric():

    target = family(
        "Geometric"
    )

    parameters = target.fit(
        [2, 5, 8, 11, 14, 17]
    )

    assert parameters is None


def test_geometric_sequence_is_not_arithmetic():

    target = family(
        "Arithmetic"
    )

    parameters = target.fit(
        [3, 6, 12, 24, 48, 96]
    )

    assert parameters is None


def test_polynomial_child_is_not_constant():

    target = family(
        "Constant"
    )

    parameters = target.fit(
        [1, 4, 9, 16, 25, 36]
    )

    assert parameters is None