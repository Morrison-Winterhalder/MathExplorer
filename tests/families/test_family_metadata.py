import pytest

from families.registry import get_family
from analyzers.core.metadata import get_family_metadata


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

def get_metadata(
    family_name,
):

    family = get_family(
        family_name
    )

    assert family is not None

    metadata = get_family_metadata(
        family
    )

    assert isinstance(
        metadata,
        dict
    )

    return metadata


# ============================================================
# Required Metadata Fields
# ============================================================

REQUIRED_FIELDS = {

    "NAME",

    "DESCRIPTION",

    "CATEGORY",

    "PARENT",

    "SPECIFICITY",

    "DOMAIN",

    "GROWTH",

    "MONOTONIC",

    "BOUNDED",

    "OSCILLATING",

    "PERIODIC",

    "FORMULA_TYPE",

    "REQUIRES_PARAMETERS",

    "PARAMETER_NAMES",

    "MIN_TERMS",

    "RECOGNITION_METHOD",

    "RELIABILITY",

}


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_family_metadata_contains_required_fields(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    missing = (

        REQUIRED_FIELDS

        - set(
            metadata
        )

    )

    assert not missing, (

        f"{family_name} is missing metadata fields: "
        f"{sorted(missing)}"

    )


# ============================================================
# Metadata Identity
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_name_matches_family_name(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert metadata["NAME"] == family_name


# ============================================================
# Metadata Type Safety
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_description_is_nonempty_string(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert isinstance(
        metadata["DESCRIPTION"],
        str
    )

    assert metadata["DESCRIPTION"].strip()


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_category_is_nonempty_string(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert isinstance(
        metadata["CATEGORY"],
        str
    )

    assert metadata["CATEGORY"].strip()


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_specificity_is_numeric(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert isinstance(
        metadata["SPECIFICITY"],
        (
            int,
            float,
        ),
    )


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_specificity_is_nonnegative(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert metadata["SPECIFICITY"] >= 0


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_min_terms_is_positive(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert isinstance(
        metadata["MIN_TERMS"],
        int
    )

    assert metadata["MIN_TERMS"] > 0


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_requires_parameters_is_boolean(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert isinstance(
        metadata["REQUIRES_PARAMETERS"],
        bool
    )


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_parameter_names_are_tuple(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert isinstance(
        metadata["PARAMETER_NAMES"],
        tuple
    )


@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_parameter_names_are_strings(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    assert all(

        isinstance(
            name,
            str
        )

        for name
        in metadata["PARAMETER_NAMES"]

    )


# ============================================================
# Parameter Metadata Consistency
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_parameter_requirement_matches_parameter_names(
    family_name,
):

    metadata = get_metadata(
        family_name
    )

    requires_parameters = (

        metadata[
            "REQUIRES_PARAMETERS"
        ]

    )

    parameter_names = (

        metadata[
            "PARAMETER_NAMES"
        ]

    )

    if requires_parameters:

        assert parameter_names

    else:

        assert parameter_names == ()


# ============================================================
# Metadata Stability
# ============================================================

@pytest.mark.parametrize(
    "family_name",
    FAMILIES,
)
def test_metadata_is_deterministic(
    family_name,
):

    family = get_family(
        family_name
    )

    first = get_family_metadata(
        family
    )

    second = get_family_metadata(
        family
    )

    assert first == second