import pytest

from families.registry import (
    FAMILIES,
    FAMILY_MAP,
)


# ============================================================
# Required Metadata Presence
# ============================================================


REQUIRED_METADATA = [
    "NAME",
    "DESCRIPTION",
    "REPRESENTATION",
    "CATEGORY",
    "SPECIFICITY",
    "PARENT",
    "FAMILY_TYPE",
    "TAGS",
    "TRAITS",
    "RELATED",
    "DOMAIN",
    "GROWTH",
    "FORMULA_TYPE",
    "REQUIRES_PARAMETERS",
    "PARAMETER_NAMES",
    "MIN_TERMS",
    "RECOGNITION_METHOD",
    "RELIABILITY",
]


@pytest.mark.parametrize(
    "attribute",
    REQUIRED_METADATA
)
def test_every_family_has_required_metadata(
    attribute
):

    for family in FAMILIES:

        assert hasattr(
            family,
            attribute
        ), (
            f"{family.NAME} is missing "
            f"metadata: {attribute}"
        )


# ============================================================
# NAME
# ============================================================


def test_family_names_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.NAME,
            str
        )

        assert family.NAME.strip() != ""


def test_family_names_are_unique():

    names = [
        family.NAME
        for family in FAMILIES
    ]

    assert len(
        names
    ) == len(
        set(names)
    )


def test_family_names_match_family_map():

    for family in FAMILIES:

        assert family.NAME in FAMILY_MAP

        assert FAMILY_MAP[
            family.NAME
        ] is family


# ============================================================
# DESCRIPTION
# ============================================================


def test_descriptions_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.DESCRIPTION,
            str
        )

        assert family.DESCRIPTION.strip() != ""


# ============================================================
# REPRESENTATION
# ============================================================


def test_representations_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.REPRESENTATION,
            str
        )

        assert family.REPRESENTATION.strip() != ""


# ============================================================
# CATEGORY
# ============================================================


def test_categories_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.CATEGORY,
            str
        )

        assert family.CATEGORY.strip() != ""


# ============================================================
# SPECIFICITY
# ============================================================


def test_specificity_is_numeric():

    for family in FAMILIES:

        assert isinstance(
            family.SPECIFICITY,
            (
                int,
                float
            )
        )


def test_specificity_is_nonnegative():

    for family in FAMILIES:

        assert family.SPECIFICITY >= 0


# ============================================================
# PARENT
# ============================================================


def test_parent_is_string_or_none():

    for family in FAMILIES:

        assert isinstance(
            family.PARENT,
            (
                str,
                type(None)
            )
        )


def test_parent_is_not_self():

    for family in FAMILIES:

        assert family.PARENT != (
            family.NAME
        )


def test_family_parents_are_valid():

    for family in FAMILIES:

        if family.PARENT is None:

            continue

        assert (
            family.PARENT in FAMILY_MAP
            or family.PARENT in {
                "Sequence Families",
                "Explicit",
                "Recursive",
                "Combinatorial",
                "Basic",
                "Figurate",
                "Polygonal",
                "Centered Polygonal",
                "Special",
                "Linear Recurrence",
            }
        )


# ============================================================
# FAMILY_TYPE
# ============================================================


def test_family_types_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.FAMILY_TYPE,
            str
        )

        assert family.FAMILY_TYPE.strip() != ""


# ============================================================
# TAGS
# ============================================================


def test_tags_are_tuples():

    for family in FAMILIES:

        assert isinstance(
            family.TAGS,
            tuple
        )


def test_tags_contain_strings():

    for family in FAMILIES:

        for tag in family.TAGS:

            assert isinstance(
                tag,
                str
            )

            assert tag.strip() != ""


def test_tags_have_no_duplicates():

    for family in FAMILIES:

        assert len(
            family.TAGS
        ) == len(
            set(
                family.TAGS
            )
        )


# ============================================================
# TRAITS
# ============================================================


def test_traits_are_dictionaries():

    for family in FAMILIES:

        assert isinstance(
            family.TRAITS,
            dict
        )


def test_trait_keys_are_strings():

    for family in FAMILIES:

        for key in family.TRAITS:

            assert isinstance(
                key,
                str
            )


def test_trait_values_are_not_none():

    for family in FAMILIES:

        for value in family.TRAITS.values():

            assert value is not None


# ============================================================
# RELATED
# ============================================================


def test_related_is_a_list():

    for family in FAMILIES:

        assert isinstance(
            family.RELATED,
            list
        )


def test_related_entries_are_strings():

    for family in FAMILIES:

        for related in family.RELATED:

            assert isinstance(
                related,
                str
            )

            assert related.strip() != ""


def test_related_has_no_duplicates():

    for family in FAMILIES:

        assert len(
            family.RELATED
        ) == len(
            set(
                family.RELATED
            )
        )

# ============================================================
# DOMAIN
# ============================================================


def test_domains_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.DOMAIN,
            str
        )

        assert family.DOMAIN.strip() != ""


# ============================================================
# GROWTH
# ============================================================


def test_growth_descriptions_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.GROWTH,
            str
        )

        assert family.GROWTH.strip() != ""


# ============================================================
# FORMULA_TYPE
# ============================================================


def test_formula_types_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.FORMULA_TYPE,
            str
        )

        assert family.FORMULA_TYPE.strip() != ""


# ============================================================
# PARAMETER CONFIGURATION
# ============================================================


def test_requires_parameters_is_boolean():

    for family in FAMILIES:

        assert isinstance(
            family.REQUIRES_PARAMETERS,
            bool
        )


def test_parameter_names_are_tuples():

    for family in FAMILIES:

        assert isinstance(
            family.PARAMETER_NAMES,
            tuple
        )


def test_parameter_names_are_strings():

    for family in FAMILIES:

        for parameter in family.PARAMETER_NAMES:

            assert isinstance(
                parameter,
                str
            )

            assert parameter.strip() != ""


def test_parameter_names_have_no_duplicates():

    for family in FAMILIES:

        assert len(
            family.PARAMETER_NAMES
        ) == len(
            set(
                family.PARAMETER_NAMES
            )
        )


def test_parameter_configuration_is_consistent():

    for family in FAMILIES:

        if family.REQUIRES_PARAMETERS:

            assert len(
                family.PARAMETER_NAMES
            ) > 0

        else:

            assert len(
                family.PARAMETER_NAMES
            ) == 0


# ============================================================
# MIN_TERMS
# ============================================================


def test_min_terms_are_integers():

    for family in FAMILIES:

        assert isinstance(
            family.MIN_TERMS,
            int
        )


def test_min_terms_are_nonnegative():

    for family in FAMILIES:

        assert family.MIN_TERMS >= 0


# ============================================================
# RECOGNITION METHOD
# ============================================================


def test_recognition_methods_are_nonempty():

    for family in FAMILIES:

        assert isinstance(
            family.RECOGNITION_METHOD,
            str
        )

        assert family.RECOGNITION_METHOD.strip() != ""


# ============================================================
# RELIABILITY
# ============================================================


def test_reliability_values_are_nonempty():

    for family in FAMILIES:

        assert family.RELIABILITY is not None


# ============================================================
# NATURAL FAMILY
# ============================================================


def test_natural_family_is_boolean_when_present():

    for family in FAMILIES:

        if hasattr(
            family,
            "NATURAL_FAMILY"
        ):

            assert isinstance(
                family.NATURAL_FAMILY,
                bool
            )


# ============================================================
# OPTIONAL METADATA
# ============================================================


def test_optional_metadata_has_expected_types():

    for family in FAMILIES:

        if hasattr(
            family,
            "AUTHOR"
        ):

            assert isinstance(
                family.AUTHOR,
                str
            )

        if hasattr(
            family,
            "VERSION"
        ):

            assert isinstance(
                family.VERSION,
                str
            )

        if hasattr(
            family,
            "SOURCE"
        ):

            assert isinstance(
                family.SOURCE,
                str
            )

        if hasattr(
            family,
            "PLUGIN"
        ):

            assert isinstance(
                family.PLUGIN,
                bool
            )


# ============================================================
# Metadata Consistency
# ============================================================


def test_family_metadata_is_not_empty():

    for family in FAMILIES:

        assert family.NAME
        assert family.DESCRIPTION
        assert family.REPRESENTATION
        assert family.CATEGORY
        assert family.FAMILY_TYPE
        assert family.DOMAIN
        assert family.GROWTH
        assert family.FORMULA_TYPE
        assert family.RECOGNITION_METHOD
        assert family.RELIABILITY is not None


def test_family_metadata_is_uppercase_constants():

    for family in FAMILIES:

        metadata = {

            key: value

            for key, value in vars(
                family
            ).items()

            if key.isupper()

        }

        assert "NAME" in metadata
        assert "DESCRIPTION" in metadata
        assert "CATEGORY" in metadata

# ============================================================
# Final Metadata Sanity Check
# ============================================================


def test_all_family_metadata_is_valid():

    for family in FAMILIES:

        assert isinstance(
            family.NAME,
            str
        )

        assert isinstance(
            family.DESCRIPTION,
            str
        )

        assert isinstance(
            family.REPRESENTATION,
            str
        )

        assert isinstance(
            family.CATEGORY,
            str
        )

        assert isinstance(
            family.SPECIFICITY,
            (
                int,
                float
            )
        )

        assert isinstance(
            family.FAMILY_TYPE,
            str
        )

        assert isinstance(
            family.TAGS,
            tuple
        )

        assert isinstance(
            family.TRAITS,
            dict
        )

        assert isinstance(
            family.RELATED,
            list
        )

        assert isinstance(
            family.REQUIRES_PARAMETERS,
            bool
        )

        assert isinstance(
            family.PARAMETER_NAMES,
            tuple
        )

        assert isinstance(
            family.MIN_TERMS,
            int
        )

        assert family.MIN_TERMS >= 0