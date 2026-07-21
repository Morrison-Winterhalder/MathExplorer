import pytest

from families.core.hierarchy import (
    HIERARCHY,
)

from families.registry import (
    FAMILY_MAP,
    FAMILIES,
    PluginError,
    get_family,
    get_parent,
    get_lineage,
    get_children,
    get_depth,
    build_family_tree,
)


# ============================================================
# Basic Hierarchy Structure
# ============================================================


def test_hierarchy_exists():

    assert HIERARCHY is not None


def test_hierarchy_is_a_dictionary():

    assert isinstance(
        HIERARCHY,
        dict
    )


def test_hierarchy_is_not_empty():

    assert len(
        HIERARCHY
    ) > 0


def test_every_hierarchy_node_is_a_dictionary():

    for name, node in HIERARCHY.items():

        assert isinstance(
            node,
            dict
        ), (
            f"{name} hierarchy entry "
            "must be a dictionary"
        )


# ============================================================
# Required Hierarchy Node Metadata
# ============================================================


def test_every_hierarchy_node_has_parent():

    for name, node in HIERARCHY.items():

        assert "parent" in node, (
            f"{name} is missing parent"
        )


def test_every_hierarchy_node_has_children():

    for name, node in HIERARCHY.items():

        assert "children" in node, (
            f"{name} is missing children"
        )


# ============================================================
# Parent Metadata
# ============================================================


def test_hierarchy_parents_are_strings_or_none():

    for name, node in HIERARCHY.items():

        parent = node["parent"]

        assert isinstance(
            parent,
            (
                str,
                type(None)
            )
        )


def test_hierarchy_nodes_do_not_parent_themselves():

    for name, node in HIERARCHY.items():

        assert node["parent"] != name


def test_hierarchy_has_at_least_one_root():

    roots = [

        name

        for name, node in HIERARCHY.items()

        if node["parent"] is None

    ]

    assert len(
        roots
    ) >= 1


# ============================================================
# Children Metadata
# ============================================================


def test_children_are_lists():

    for name, node in HIERARCHY.items():

        assert isinstance(
            node["children"],
            list
        )


def test_children_are_nonempty_or_valid_leaves():

    for name, node in HIERARCHY.items():

        children = node["children"]

        assert children is not None


def test_children_are_strings():

    for name, node in HIERARCHY.items():

        for child in node["children"]:

            assert isinstance(
                child,
                str
            )

            assert child.strip() != ""


def test_children_have_no_duplicates():

    for name, node in HIERARCHY.items():

        children = node["children"]

        assert len(
            children
        ) == len(
            set(children)
        )


def test_nodes_do_not_list_themselves_as_children():

    for name, node in HIERARCHY.items():

        assert name not in (
            node["children"]
        )


# ============================================================
# Parent / Child Consistency
# ============================================================


def test_child_parent_relationships_are_consistent():

    for parent_name, node in HIERARCHY.items():

        for child_name in node["children"]:

            if child_name not in HIERARCHY:

                continue

            child_parent = HIERARCHY[
                child_name
            ]["parent"]

            assert child_parent == (
                parent_name
            ), (
                f"{child_name} is listed under "
                f"{parent_name}, but declares "
                f"{child_parent} as its parent"
            )


def test_parent_child_relationships_are_bidirectional():

    for child_name, node in HIERARCHY.items():

        parent_name = node["parent"]

        if parent_name is None:

            continue

        assert parent_name in HIERARCHY

        assert child_name in (
            HIERARCHY[
                parent_name
            ]["children"]
        )


# ============================================================
# Hierarchy Parent Validity
# ============================================================


def test_all_declared_parents_exist():

    for name, node in HIERARCHY.items():

        parent = node["parent"]

        if parent is None:

            continue

        assert parent in HIERARCHY, (
            f"{name} declares unknown parent "
            f"{parent}"
        )


def test_all_declared_children_exist():

    loaded_family_names = {
        family.NAME
        for family in FAMILIES
    }

    for name, node in HIERARCHY.items():

        for child in node["children"]:

            assert (
                child in HIERARCHY
                or child in loaded_family_names
            ), (
                f"{name} declares unknown child "
                f"{child}"
            )


# ============================================================
# Root Hierarchy
# ============================================================


def test_root_nodes_have_no_parent():

    roots = [

        name

        for name, node in HIERARCHY.items()

        if node["parent"] is None

    ]

    assert roots

    for root in roots:

        assert HIERARCHY[
            root
        ]["parent"] is None


def test_sequence_families_is_root():

    assert HIERARCHY[
        "Sequence Families"
    ]["parent"] is None


def test_sequence_families_contains_major_branches():

    children = HIERARCHY[
        "Sequence Families"
    ]["children"]

    assert "Explicit" in children
    assert "Recursive" in children
    assert "Combinatorial" in children


# ============================================================
# Known Hierarchy Structure
# ============================================================


def test_explicit_is_child_of_sequence_families():

    assert HIERARCHY[
        "Explicit"
    ]["parent"] == (
        "Sequence Families"
    )


def test_recursive_is_child_of_sequence_families():

    assert HIERARCHY[
        "Recursive"
    ]["parent"] == (
        "Sequence Families"
    )


def test_combinatorial_is_child_of_sequence_families():

    assert HIERARCHY[
        "Combinatorial"
    ]["parent"] == (
        "Sequence Families"
    )


def test_basic_is_child_of_explicit():

    assert HIERARCHY[
        "Basic"
    ]["parent"] == (
        "Explicit"
    )


def test_figurate_is_child_of_explicit():

    assert HIERARCHY[
        "Figurate"
    ]["parent"] == (
        "Explicit"
    )


def test_special_is_child_of_explicit():

    assert HIERARCHY[
        "Special"
    ]["parent"] == (
        "Explicit"
    )


def test_linear_recurrence_is_child_of_recursive():

    assert HIERARCHY[
        "Linear Recurrence"
    ]["parent"] == (
        "Recursive"
    )


# ============================================================
# Known Hierarchy Branches
# ============================================================


def test_basic_contains_expected_families():

    children = HIERARCHY[
        "Basic"
    ]["children"]

    expected = {
        "Constant",
        "Arithmetic",
        "Geometric",
        "Polynomial",
    }

    assert expected.issubset(
        set(children)
    )


def test_special_contains_factorials():

    assert "Factorials" in (
        HIERARCHY[
            "Special"
        ]["children"]
    )


def test_linear_recurrence_contains_expected_families():

    children = HIERARCHY[
        "Linear Recurrence"
    ]["children"]

    expected = {
        "Fibonacci",
        "Lucas Numbers",
        "Pell Numbers",
        "Jacobsthal Numbers",
        "Tribonacci Numbers",
        "Tetranacci Numbers",
        "Padovan Numbers",
        "Perrin Numbers",
    }

    assert expected.issubset(
        set(children)
    )


def test_polygonal_contains_expected_families():

    polygonal = get_children(
        "Polygonal"
    )

    names = {
        family.NAME
        for family in polygonal
    }

    expected = {
        "Triangular Numbers",
        "Pentagonal Numbers",
        "Hexagonal Numbers",
        "Heptagonal Numbers",
        "Octagonal Numbers",
        "Nonagonal Numbers",
        "Decagonal Numbers",
    }

    assert expected.issubset(
        names
    )

def test_centered_polygonal_contains_expected_families():

    centered = get_children(
        "Centered Polygonal"
    )

    names = {
        family.NAME
        for family in centered
    }

    expected = {
        "Centered Triangular Numbers",
        "Centered Square Numbers",
        "Centered Pentagonal Numbers",
        "Centered Hexagonal Numbers",
    }

    assert expected.issubset(
        names
    )

def test_centered_polygonal_contains_expected_families():

    children = HIERARCHY[
        "Centered Polygonal"
    ]["children"]

    expected = {
        "Centered Triangular Numbers",
        "Centered Square Numbers",
        "Centered Pentagonal Numbers",
        "Centered Hexagonal Numbers",
    }

    assert expected.issubset(
        set(children)
    )


# ============================================================
# Hierarchy Acyclicity
# ============================================================


def test_hierarchy_contains_no_cycles():

    for start in HIERARCHY:

        visited = set()

        current = start

        while current is not None:

            assert current not in visited, (
                f"Hierarchy cycle detected "
                f"starting at {start}"
            )

            visited.add(
                current
            )

            current = HIERARCHY[
                current
            ]["parent"]


def test_every_node_eventually_reaches_a_root():

    for start in HIERARCHY:

        visited = set()

        current = start

        while current is not None:

            assert current not in visited

            visited.add(
                current
            )

            current = HIERARCHY[
                current
            ]["parent"]

        assert current is None


# ============================================================
# Hierarchy Depth
# ============================================================


def hierarchy_depth(name):

    depth = 0

    current = name

    visited = set()

    while True:

        assert current not in visited

        visited.add(
            current
        )

        parent = HIERARCHY[current]["parent"]

        if parent is None:

            return depth

        depth += 1

        current = parent


def test_root_depth_is_zero():

    for name, node in HIERARCHY.items():

        if node["parent"] is None:

            assert hierarchy_depth(
                name
            ) == 0


def test_explicit_depth_is_one():

    assert hierarchy_depth(
        "Explicit"
    ) == 1


def test_special_depth_is_two():

    assert hierarchy_depth(
        "Special"
    ) == 2


# ============================================================
# Registry / Hierarchy Integration
# ============================================================


def test_registered_family_parents_match_hierarchy():

    for family in FAMILIES:

        if family.NAME not in HIERARCHY:

            continue

        expected_parent = HIERARCHY[
            family.NAME
        ]["parent"]

        if expected_parent is None:

            continue

        assert family.PARENT == (
            expected_parent
        )


def test_registered_family_hierarchy_parents_are_valid():

    for family in FAMILIES:

        if family.PARENT is None:

            continue

        assert (
            family.PARENT in FAMILY_MAP
            or family.PARENT in HIERARCHY
        )


def test_registered_families_are_represented_in_hierarchy_when_expected():

    for family in FAMILIES:

        if family.NAME not in HIERARCHY:

            continue

        hierarchy_parent = HIERARCHY[
            family.NAME
        ]["parent"]

        if hierarchy_parent is None:

            continue

        assert family.PARENT == (
            hierarchy_parent
        )


# ============================================================
# Registry Lineage Integration
# ============================================================


def test_factorials_have_expected_lineage():

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


def test_factorials_have_expected_depth():

    family = get_family(
        "Factorials"
    )

    assert get_depth(
        family
    ) == 3


def test_explicit_has_no_registered_parent():

    family = get_family(
        "Explicit"
    )

    assert get_parent(
        family
    ) is None


# ============================================================
# Registry Children Integration
# ============================================================


def test_special_children_match_registered_families():

    children = get_children(
        "Special"
    )

    names = {
        child.NAME
        for child in children
    }

    expected = {

        family.NAME

        for family in FAMILIES

        if family.PARENT == "Special"

    }

    assert names == expected


def test_factorials_are_a_leaf_family():

    family = get_family(
        "Factorials"
    )

    assert get_children(
        family.NAME
    ) == []


# ============================================================
# Hierarchy Tree Representation
# ============================================================


def test_family_tree_returns_string():

    family = get_family(
        "Factorials"
    )

    tree = build_family_tree(
        family
    )

    assert isinstance(
        tree,
        str
    )


def test_family_tree_contains_family_name():

    family = get_family(
        "Factorials"
    )

    tree = build_family_tree(
        family
    )

    assert "Factorials" in tree


def test_family_tree_contains_lineage():

    family = get_family(
        "Factorials"
    )

    tree = build_family_tree(
        family
    )

    assert "Special" in tree
    assert "Explicit" in tree


def test_family_tree_has_expected_order():

    family = get_family(
        "Factorials"
    )

    tree = build_family_tree(
        family
    )

    factorial_index = tree.index(
        "Factorials"
    )

    special_index = tree.index(
        "Special"
    )

    explicit_index = tree.index(
        "Explicit"
    )

    assert factorial_index < special_index
    assert special_index < explicit_index


# ============================================================
# Final Hierarchy Sanity Check
# ============================================================


def test_hierarchy_is_valid():

    assert HIERARCHY

    for name, node in HIERARCHY.items():

        assert isinstance(
            name,
            str
        )

        assert isinstance(
            node,
            dict
        )

        assert "parent" in node
        assert "children" in node

        assert isinstance(
            node["children"],
            list
        )