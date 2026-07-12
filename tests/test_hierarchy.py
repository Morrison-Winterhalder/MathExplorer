from families.registry import (
    get_family,
    get_lineage,
    build_family_tree,
)


# ==========================================================
# Parent Exists
# ==========================================================

def test_centered_square_parent():

    family = get_family(
        "Centered Square Numbers"
    )

    assert family.PARENT == "Centered Polygonal"


# ==========================================================
# Full Lineage
# ==========================================================

def test_centered_square_lineage():

    family = get_family(
        "Centered Square Numbers"
    )

    lineage = get_lineage(family)

    names = [
        parent.NAME
        for parent in lineage
    ]

    assert names == [
        "Centered Polygonal",
        "Polygonal",
        "Figurate",
        "Explicit"
    ]


# ==========================================================
# Tree Rendering
# ==========================================================

def test_family_tree():

    family = get_family(
        "Centered Square Numbers"
    )

    tree = build_family_tree(family)

    assert "Centered Square Numbers" in tree
    assert "Centered Polygonal" in tree
    assert "Polygonal" in tree
    assert "Figurate" in tree


# ==========================================================
# All Parents Valid
# ==========================================================

def test_all_parents_exist():

    from families.registry import FAMILIES

    for family in FAMILIES:

        if family.PARENT is not None:
            assert get_family(
                family.PARENT
            ) is not None