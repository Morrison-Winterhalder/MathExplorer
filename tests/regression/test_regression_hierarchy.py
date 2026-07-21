import pytest

from families.registry import (
    FAMILIES,
    HIERARCHY,
    PluginError
)


# ============================================================
# Shared Registry Data
# ============================================================


LOADED_FAMILY_MAP = {
    family.NAME: family
    for family in FAMILIES
}


LOADED_FAMILY_NAMES = set(
    LOADED_FAMILY_MAP
)


# ============================================================
# Hierarchy Structure
# ============================================================


def test_hierarchy_has_root():

    roots = [

        name

        for name, node in HIERARCHY.items()

        if node["parent"] is None

    ]

    assert roots == [
        "Sequence Families"
    ]


def test_hierarchy_has_no_cycles():

    for name in HIERARCHY:

        visited = set()

        current = name

        while current is not None:

            assert current not in visited, (

                f"Hierarchy cycle detected involving "

                f"{current}"

            )

            visited.add(current)

            current = HIERARCHY[current]["parent"]


def test_every_hierarchy_parent_exists():

    for name, node in HIERARCHY.items():

        parent = node["parent"]

        if parent is not None:

            assert parent in HIERARCHY, (

                f"{name} declares unknown parent "

                f"{parent}"

            )


def test_every_declared_hierarchy_child_is_known():

    for name, node in HIERARCHY.items():

        for child in node["children"]:

            assert (

                child in HIERARCHY

                or child in LOADED_FAMILY_NAMES

            ), (

                f"{name} declares unknown child "

                f"{child}"

            )


# ============================================================
# Parent / Child Consistency
# ============================================================


def test_loaded_family_parent_appears_in_hierarchy():

    for family in FAMILIES:

        parent = family.PARENT

        assert parent in HIERARCHY, (

            f"{family.NAME} declares parent "

            f"{parent}, but that parent is not "

            "present in the hierarchy."

        )


def test_loaded_family_appears_under_declared_parent():

    for family in FAMILIES:

        parent = family.PARENT

        assert family.NAME in (

            HIERARCHY[parent]["children"]

        ), (

            f"{family.NAME} declares "

            f"{parent} as its parent, but is not "

            "listed among that parent's children."

        )


def test_hierarchy_loaded_children_match_parent_metadata():

    for parent_name, node in HIERARCHY.items():

        for child_name in node["children"]:

            child = LOADED_FAMILY_MAP.get(

                child_name

            )

            if child is None:

                continue

            assert child.PARENT == (

                parent_name

            ), (

                f"{child_name} appears under "

                f"{parent_name}, but declares "

                f"{child.PARENT} as its parent."

            )


# ============================================================
# Parent / Child Coverage
# ============================================================


def test_every_loaded_family_has_exactly_one_parent():

    for family in FAMILIES:

        matching_parents = [

            parent_name

            for parent_name, node in HIERARCHY.items()

            if family.NAME in node["children"]

        ]

        assert matching_parents == [

            family.PARENT

        ], (

            f"{family.NAME} appears under "

            f"{matching_parents}, but declares "

            f"{family.PARENT}"

        )


def test_every_hierarchy_parent_has_consistent_loaded_children():

    for parent_name, node in HIERARCHY.items():

        for child_name in node["children"]:

            child = LOADED_FAMILY_MAP.get(

                child_name

            )

            if child is None:

                continue

            assert child.PARENT == parent_name


# ============================================================
# Root Regression
# ============================================================


def test_root_has_no_parent():

    root = HIERARCHY[

        "Sequence Families"

    ]

    assert root["parent"] is None


def test_root_contains_top_level_categories():

    root = HIERARCHY[

        "Sequence Families"

    ]

    expected = {

        "Explicit",

        "Recursive",

        "Combinatorial",

    }

    assert expected.issubset(

        set(root["children"])

    )


# ============================================================
# Hierarchy Depth
# ============================================================


def hierarchy_depth(name):

    if name not in HIERARCHY:

        raise PluginError(
            f"Unknown family: {name}"
        )

    depth = 0

    current = name

    while HIERARCHY[current]["parent"] is not None:

        current = HIERARCHY[current]["parent"]

        depth += 1

    return depth


def test_root_has_depth_zero():

    assert hierarchy_depth(

        "Sequence Families"

    ) == 0


def test_top_level_categories_have_depth_one():

    for name in (

        "Explicit",

        "Recursive",

        "Combinatorial",

    ):

        assert hierarchy_depth(

            name

        ) == 1


def test_child_nodes_are_deeper_than_parents():

    for name, node in HIERARCHY.items():

        parent = node["parent"]

        if parent is None:

            continue

        assert hierarchy_depth(name) > (

            hierarchy_depth(parent)

        )


# ============================================================
# Known Structural Relationships
# ============================================================


@pytest.mark.parametrize(

    "child, parent",

    [

        (

            "Explicit",

            "Sequence Families",

        ),

        (

            "Recursive",

            "Sequence Families",

        ),

        (

            "Combinatorial",

            "Sequence Families",

        ),

        (

            "Basic",

            "Explicit",

        ),

        (

            "Figurate",

            "Explicit",

        ),

        (

            "Special",

            "Explicit",

        ),

        (

            "Polygonal",

            "Figurate",

        ),

        (

            "Centered Polygonal",

            "Figurate",

        ),

        (

            "Linear Recurrence",

            "Recursive",

        ),

    ],

)


def test_known_structural_relationships(

    child,

    parent,

):

    assert HIERARCHY[child]["parent"] == parent


# ============================================================
# Loaded Family Category Regression
# ============================================================


def test_loaded_families_have_valid_parent_categories():

    for family in FAMILIES:

        assert family.PARENT in HIERARCHY


def test_loaded_families_are_reachable_from_root():

    for family in FAMILIES:

        current = family.PARENT

        visited = set()

        while current is not None:

            assert current not in visited

            visited.add(current)

            current = HIERARCHY[current]["parent"]


        assert (

            "Sequence Families"

            in visited

        )


# ============================================================
# No Duplicate Relationships
# ============================================================


def test_hierarchy_children_are_unique():

    for name, node in HIERARCHY.items():

        children = node["children"]

        assert len(children) == len(

            set(children)

        ), (

            f"{name} contains duplicate children."

        )


def test_loaded_families_do_not_have_multiple_hierarchy_parents():

    for family in FAMILIES:

        parents = [

            parent_name

            for parent_name, node in HIERARCHY.items()

            if family.NAME in node["children"]

        ]

        assert len(parents) == 1


# ============================================================
# Final Regression Sanity Check
# ============================================================


def test_hierarchy_regression_is_usable():

    assert HIERARCHY

    assert FAMILIES

    assert "Sequence Families" in HIERARCHY

    for family in FAMILIES:

        assert family.NAME in (

            LOADED_FAMILY_NAMES

        )

        assert family.PARENT in HIERARCHY