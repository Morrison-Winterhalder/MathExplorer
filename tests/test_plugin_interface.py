from families.registry import FAMILIES, FAMILY_MAP, get_family

def test_every_family_has_metadata():
    for family in FAMILIES:
        assert hasattr(family, "NAME")
        assert hasattr(family, "DESCRIPTION")
        assert hasattr(family, "REPRESENTATION")
        assert hasattr(family, "CATEGORY")
        assert hasattr(family, "SPECIFICITY")
        assert hasattr(family, "PARENT")

def test_every_parent_exists():

    for family in FAMILIES:

        if family.PARENT is not None:
            assert get_family(family.PARENT) is not None

def test_every_family_has_required_functions():
    for family in FAMILIES:
        assert callable(family.recognize)
        assert callable(family.fit)
        assert callable(family.evaluate)
        assert callable(family.formula)
        assert callable(family.complexity)

def test_plugins():
    assert len(FAMILIES) == len(FAMILY_MAP)
    for family in FAMILIES:
        assert get_family(family.NAME) is family

def test_family_hierarchy():

    family = get_family(
        "Centered Square Numbers"
    )

    assert family.PARENT == "Centered Polygonal"

    parent = get_family(
        family.PARENT
    )

    assert parent.PARENT == "Polygonal"