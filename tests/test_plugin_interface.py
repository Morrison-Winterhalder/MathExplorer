from families.registry import FAMILIES

def test_every_family_has_metadata():
    for family in FAMILIES:
        assert hasattr(family, "NAME")
        assert hasattr(family, "DESCRIPTION")
        assert hasattr(family, "REPRESENTATION")
        assert hasattr(family, "CATEGORY")

def test_every_family_has_required_functions():
    for family in FAMILIES:
        assert callable(family.recognize)
        assert callable(family.fit)
        assert callable(family.evaluate)
        assert callable(family.formula)
        assert callable(family.complexity)