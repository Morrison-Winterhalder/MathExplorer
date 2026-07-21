import pytest

from families.registry import (
    FAMILIES,
    FAMILY_MAP,
    PluginError,
    get_family,
    get_metadata,
    get_parent,
    get_lineage,
    get_children,
    get_depth,
    get_siblings,
    get_related,
)


def test_get_family_returns_correct_family():

    family = get_family(
        "Factorials"
    )

    assert family is not None
    assert family.NAME == "Factorials"


def test_get_family_returns_none_for_unknown_family():

    family = get_family(
        "Definitely Not A Family"
    )

    assert family is None


def test_get_family_required_raises_for_unknown_family():

    try:

        get_family(
            "Definitely Not A Family",
            required=True
        )

    except Exception as error:

        import sys

        print(
            "Registry module object:",
            sys.modules.get(
                "families.registry"
            )
        )

        print(
            "PluginError module:",
            PluginError.__module__
        )

        print(
            "PluginError class ID:",
            id(PluginError)
        )

        print(
            "Exception class ID:",
            id(type(error))
        )

        print(
            "Exception class module:",
            type(error).__module__
        )

        print(
            "Raised type:",
            type(error)
        )

        print(
            "Expected type:",
            PluginError
        )

        print(
            "Same class:",
            type(error) is PluginError
        )

        print(
            "Raised class ID:",
            id(type(error))
        )

        print(
            "Expected class ID:",
            id(PluginError)
        )

        assert isinstance(
            error,
            PluginError
        )

    else:

        pytest.fail(
            "PluginError was not raised"
        )

def test_get_family_required_does_not_raise_for_existing_family():

    family = get_family(
        "Factorials",
        required=True
    )

    assert family is not None
    assert family.NAME == "Factorials"


def test_family_map_contains_all_loaded_families():

    for family in FAMILIES:

        assert family.NAME in FAMILY_MAP

        assert (
            FAMILY_MAP[family.NAME]
            is family
        )


def test_get_metadata_returns_uppercase_metadata():

    family = get_family(
        "Factorials"
    )

    metadata = get_metadata(
        family
    )

    assert isinstance(
        metadata,
        dict
    )

    for key in metadata:

        assert key.isupper()


def test_get_metadata_contains_family_name():

    family = get_family(
        "Factorials"
    )

    metadata = get_metadata(
        family
    )

    assert metadata["NAME"] == (
        "Factorials"
    )


def test_get_metadata_contains_required_metadata():

    family = get_family(
        "Factorials"
    )

    metadata = get_metadata(
        family
    )

    required = {
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
    }

    assert required.issubset(
        metadata.keys()
    )


def test_get_parent_returns_correct_parent():

    family = get_family(
        "Factorials"
    )

    parent = get_parent(
        family
    )

    assert parent is not None

    assert parent.NAME == (
        "Special"
    )


def test_get_parent_returns_none_for_root_family():

    family = get_family(
        "Explicit"
    )

    parent = get_parent(
        family
    )

    assert parent is None


def test_get_lineage_returns_parent_chain():

    family = get_family(
        "Factorials"
    )

    lineage = get_lineage(
        family
    )

    names = [
        parent.NAME
        for parent in lineage
    ]

    assert names == [
        "Special",
        "Explicit",
    ]


def test_get_lineage_is_ordered_from_nearest_to_farthest_parent():

    family = get_family(
        "Factorials"
    )

    lineage = get_lineage(
        family
    )

    assert lineage[0].NAME == (
        "Special"
    )

    assert lineage[-1].NAME == (
        "Explicit"
    )


def test_root_family_has_empty_lineage():

    family = get_family(
        "Explicit"
    )

    lineage = get_lineage(
        family
    )

    assert lineage == []


def test_get_children_returns_direct_children():

    children = get_children(
        "Special"
    )

    assert children

    for child in children:

        assert child.PARENT == (
            "Special"
        )


def test_get_children_returns_empty_list_for_leaf_family():

    children = get_children(
        "Factorials"
    )

    assert children == []


def test_get_depth_returns_zero_for_root_family():

    family = get_family(
        "Sequence Families"
    )

    assert get_depth(
        family
    ) == 0


def test_get_depth_returns_correct_depth_for_child():

    family = get_family(
        "Factorials"
    )

    assert get_depth(
        family
    ) == 3


def test_get_siblings_returns_families_with_same_parent():

    family = get_family(
        "Factorials"
    )

    siblings = get_siblings(
        family
    )

    for sibling in siblings:

        assert sibling.PARENT == (
            family.PARENT
        )

        assert sibling.NAME != (
            family.NAME
        )


def test_get_siblings_does_not_include_family_itself():

    family = get_family(
        "Factorials"
    )

    siblings = get_siblings(
        family
    )

    sibling_names = [
        sibling.NAME
        for sibling in siblings
    ]

    assert family.NAME not in (
        sibling_names
    )


def test_root_family_has_no_siblings():

    family = get_family(
        "Explicit"
    )

    assert get_siblings(
        family
    ) == []


def test_get_related_returns_correct_family_objects():

    family = get_family(
        "Factorials"
    )

    related = get_related(
        family
    )

    assert isinstance(
        related,
        list
    )

    for related_family in related:

        assert related_family.NAME in (
            family.RELATED
        )


def test_get_related_matches_declared_related_names():

    family = get_family(
        "Factorials"
    )

    related = get_related(
        family
    )

    related_names = [
        related_family.NAME
        for related_family in related
    ]

    assert related_names == (
        family.RELATED
    )


def test_get_related_returns_empty_list_when_no_related_families():

    for family in FAMILIES:

        if not family.RELATED:

            assert get_related(
                family
            ) == []

            break