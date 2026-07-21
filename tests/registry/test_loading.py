import importlib
import inspect

import pytest

from families.registry import (
    FAMILIES,
)


# ============================================================
# Basic Registry Loading
# ============================================================


def test_registry_loads_families():

    assert FAMILIES is not None

    assert len(FAMILIES) > 0


def test_registry_loads_expected_number_of_families():

    assert len(FAMILIES) == 45


def test_all_loaded_families_are_modules():

    for family in FAMILIES:

        assert inspect.ismodule(
            family
        )


def test_all_loaded_families_are_importable():

    for family in FAMILIES:

        imported = importlib.import_module(
            family.__name__
        )

        assert imported is family


# ============================================================
# Family Identity
# ============================================================


def test_every_loaded_family_has_a_name():

    for family in FAMILIES:

        assert hasattr(
            family,
            "NAME"
        )

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

    assert len(names) == len(set(names))


def test_every_loaded_family_has_a_description():

    for family in FAMILIES:

        assert hasattr(
            family,
            "DESCRIPTION"
        )

        assert isinstance(
            family.DESCRIPTION,
            str
        )

        assert family.DESCRIPTION.strip() != ""


# ============================================================
# Required Family Interface
# ============================================================


@pytest.mark.parametrize(
    "attribute",
    [
        "NAME",
        "DESCRIPTION",
        "REPRESENTATION",
        "CATEGORY",
        "SPECIFICITY",
        "PARENT",
        "FAMILY_TYPE",
        "TAGS",
        "TRAITS",
        "DOMAIN",
        "GROWTH",
        "FORMULA_TYPE",
        "REQUIRES_PARAMETERS",
        "PARAMETER_NAMES",
        "MIN_TERMS",
        "RECOGNITION_METHOD",
        "RELIABILITY",
    ]
)
def test_every_family_has_required_metadata(
    attribute
):

    for family in FAMILIES:

        assert hasattr(
            family,
            attribute
        ), (
            f"{family.__name__} is missing "
            f"required metadata: {attribute}"
        )


@pytest.mark.parametrize(
    "function_name",
    [
        "recognize",
        "fit",
        "evaluate",
        "formula",
        "complexity",
        "explain",
    ]
)
def test_every_family_has_required_functions(
    function_name
):

    for family in FAMILIES:

        assert hasattr(
            family,
            function_name
        ), (
            f"{family.__name__} is missing "
            f"required function: {function_name}"
        )

        assert callable(
            getattr(
                family,
                function_name
            )
        )


# ============================================================
# Metadata Type Validation
# ============================================================


def test_family_names_are_strings():

    for family in FAMILIES:

        assert isinstance(
            family.NAME,
            str
        )


def test_family_categories_are_strings():

    for family in FAMILIES:

        assert isinstance(
            family.CATEGORY,
            str
        )


def test_family_representations_are_strings():

    for family in FAMILIES:

        assert isinstance(
            family.REPRESENTATION,
            str
        )


def test_family_specificity_is_numeric():

    for family in FAMILIES:

        assert isinstance(
            family.SPECIFICITY,
            (
                int,
                float
            )
        )


def test_family_natural_flag_is_boolean_when_present():

    for family in FAMILIES:

        if hasattr(
            family,
            "NATURAL_FAMILY"
        ):

            assert isinstance(
                family.NATURAL_FAMILY,
                bool
            )


def test_family_tags_are_iterable():

    for family in FAMILIES:

        assert hasattr(
            family.TAGS,
            "__iter__"
        )


def test_family_traits_are_dictionary():

    for family in FAMILIES:

        assert isinstance(
            family.TRAITS,
            dict
        )


def test_family_parameter_names_are_iterable():

    for family in FAMILIES:

        assert hasattr(
            family.PARAMETER_NAMES,
            "__iter__"
        )


# ============================================================
# Recognition / Fitting Interface
# ============================================================


def test_recognize_is_callable():

    for family in FAMILIES:

        assert callable(
            family.recognize
        )


def test_fit_is_callable():

    for family in FAMILIES:

        assert callable(
            family.fit
        )


def test_evaluate_is_callable():

    for family in FAMILIES:

        assert callable(
            family.evaluate
        )


def test_formula_is_callable():

    for family in FAMILIES:

        assert callable(
            family.formula
        )


def test_complexity_is_callable():

    for family in FAMILIES:

        assert callable(
            family.complexity
        )


def test_explain_is_callable():

    for family in FAMILIES:

        assert callable(
            family.explain
        )


# ============================================================
# Duplicate Module Protection
# ============================================================


def test_no_duplicate_family_modules():

    module_names = [
        family.__name__
        for family in FAMILIES
    ]

    assert len(
        module_names
    ) == len(
        set(module_names)
    )


def test_no_duplicate_family_objects():

    family_ids = [
        id(family)
        for family in FAMILIES
    ]

    assert len(
        family_ids
    ) == len(
        set(family_ids)
    )


# ============================================================
# Registry Stability
# ============================================================


def test_registry_family_order_is_deterministic():

    names = [
        family.NAME
        for family in FAMILIES
    ]

    assert names == sorted(
        names
    )


def test_all_families_belong_to_expected_family_package():

    for family in FAMILIES:

        assert family.__name__.startswith(
            "families."
        )


# ============================================================
# Family Metadata Consistency
# ============================================================


def test_min_terms_are_nonnegative():

    for family in FAMILIES:

        assert family.MIN_TERMS >= 0


def test_specificity_is_nonnegative():

    for family in FAMILIES:

        assert family.SPECIFICITY >= 0


def test_parameter_names_match_parameter_requirement():

    for family in FAMILIES:

        if family.REQUIRES_PARAMETERS:

            assert len(
                family.PARAMETER_NAMES
            ) > 0

        else:

            assert (
                family.PARAMETER_NAMES == ()
                or len(
                    family.PARAMETER_NAMES
                ) == 0
            )


def test_every_family_has_a_reliability_value():

    for family in FAMILIES:

        assert family.RELIABILITY is not None


# ============================================================
# Registry Completeness
# ============================================================


def test_expected_families_are_loaded():

    expected_families = {

        "Constant",

        "Arithmetic",

        "Geometric",

        "Polynomial",

        "Squares",

        "Fibonacci",

        "Lucas Numbers",

        "Pell Numbers",

        "Factorials",

        "Catalan Numbers",

        "Bell Numbers",

        "Van Eck Numbers",

    }

    loaded_names = {

        family.NAME
        for family in FAMILIES

    }

    assert expected_families.issubset(
        loaded_names
    )


def test_registry_contains_multiple_family_categories():

    categories = {

        family.CATEGORY
        for family in FAMILIES
    }

    assert len(
        categories
    ) > 1


def test_registry_contains_natural_families():

    assert any(
        getattr(
            family,
            "NATURAL_FAMILY",
            False
        )

        for family in FAMILIES
    )


# ============================================================
# Import Safety
# ============================================================


def test_loaded_families_have_no_missing_module_reference():

    for family in FAMILIES:

        assert family is not None


def test_loaded_families_have_module_names():

    for family in FAMILIES:

        assert hasattr(
            family,
            "__name__"
        )

        assert isinstance(
            family.__name__,
            str
        )


# ============================================================
# Final Registry Sanity Check
# ============================================================


def test_registry_is_usable():

    assert len(
        FAMILIES
    ) > 0

    for family in FAMILIES:

        assert isinstance(
            family.NAME,
            str
        )

        assert callable(
            family.recognize
        )

        assert callable(
            family.fit
        )

        assert callable(
            family.evaluate
        )

        assert callable(
            family.formula
        )

        assert callable(
            family.complexity
        )

        assert callable(
            family.explain
        )