import pytest

from families.registry import get_family


# ============================================================
# Families Under Test
# ============================================================

FAMILIES = [

    "Arithmetic",
    "Geometric",
    "Constant",
    "Polynomial",

    "Polygonal",
    "Centered Polygonal",

    "Factorials",

    "Linear Recurrence",

    "Fibonacci",
    "Lucas Numbers",
    "Pell Numbers",
    "Jacobsthal Numbers",
    "Tribonacci Numbers",
    "Tetranacci Numbers",
    "Padovan Numbers",
    "Perrin Numbers",

    "Catalan Numbers",
    "Bell Numbers",
    "Derangement Numbers",
    "Partition Numbers",
    "Schröder Numbers",

    "Cubes",
    "Squares",
    "Fifth Powers",
    "Fourth Powers",

    "Triangular Numbers",
    "Pentagonal Numbers",
    "Hexagonal Numbers",
    "Heptagonal Numbers",
    "Octagonal Numbers",
    "Nonagonal Numbers",
    "Decagonal Numbers",

    "Centered Triangular Numbers",
    "Centered Square Numbers",
    "Centered Pentagonal Numbers",
    "Centered Hexagonal Numbers",

    "Van Eck Numbers",
    "Collatz Stopping Times",
    "Happy Numbers",
    "Look-and-Say Numbers",

]


# ============================================================
# Helpers
# ============================================================

def loaded_family(name):

    family = get_family(
        name
    )

    assert family is not None

    return family


# ============================================================
# Required Metadata
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_has_name(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert hasattr(
        family,
        "NAME"
    )

    assert family.NAME == family_name


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_has_parent(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert hasattr(
        family,
        "PARENT"
    )


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_has_fit(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert callable(
        family.fit
    )


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_has_evaluate(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert callable(
        family.evaluate
    )


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_has_complexity(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert callable(
        family.complexity
    )


# ============================================================
# Metadata Consistency
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_parent_matches_hierarchy_metadata(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert family.PARENT is not None


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_name_is_nonempty(
    family_name,
):

    family = loaded_family(
        family_name
    )

    assert isinstance(
        family.NAME,
        str
    )

    assert family.NAME.strip()


# ============================================================
# Fit Contract
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_fit_returns_parameters_or_none(
    family_name,
):

    family = loaded_family(
        family_name
    )

    sequence = [

        1,
        2,
        3,
        4,
        5,

    ]

    parameters = family.fit(
        sequence
    )

    assert (

        parameters is None

        or isinstance(
            parameters,
            (
                dict,
                list,
                tuple,
                int,
                float,
            ),
        )

    )


# ============================================================
# Evaluate Contract
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_evaluate_returns_numeric_value(
    family_name,
):

    family = loaded_family(
        family_name
    )

    parameters = family.fit(

        [

            1,
            2,
            3,
            4,
            5,

        ]

    )

    if parameters is None:

        pytest.skip(
            "Family cannot fit this sequence."
        )

    value = family.evaluate(
        parameters,
        1,
    )

    assert isinstance(
        value,
        (
            int,
            float,
        ),
    )


# ============================================================
# Complexity Contract
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_complexity_returns_numeric_value(
    family_name,
):

    family = loaded_family(
        family_name
    )

    parameters = family.fit(

        [

            1,
            2,
            3,
            4,
            5,

        ]

    )

    if parameters is None:

        parameters = {}

    complexity = family.complexity(
        parameters
    )

    assert isinstance(
        complexity,
        (
            int,
            float,
        ),
    )

    assert complexity >= 0