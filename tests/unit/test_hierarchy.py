from analyzers.explanation_engine.hierarchy_builder import (
    hierarchy_reasons,
)

from analyzers.core.analysis import SequenceAnalysis



# ==========================================================
# Mock Families
# ==========================================================

class RootFamily:

    NAME = "Root Family"

    PARENT = None



class ChildFamily:

    NAME = "Child Family"

    PARENT = "Root Family"



# ==========================================================
# Mock Registry Behavior
# ==========================================================

class MockRegistry:

    @staticmethod
    def get_lineage(family):

        if family.NAME == "Child Family":

            return [
                RootFamily
            ]

        return []



# ==========================================================
# Helpers
# ==========================================================

def make_analysis():

    return SequenceAnalysis(
        [1, 2, 3]
    )



# ==========================================================
# No Family Cases
# ==========================================================

def test_hierarchy_reasons_without_family():

    analysis = make_analysis()


    result = hierarchy_reasons(
        analysis
    )


    assert result == []



# ==========================================================
# No Lineage Cases
# ==========================================================

def test_hierarchy_reasons_without_lineage(monkeypatch):

    analysis = make_analysis()

    analysis.classification = {
        "Family": RootFamily
    }


    monkeypatch.setattr(
        "analyzers.explanation_engine.hierarchy_builder.registry",
        MockRegistry
    )


    result = hierarchy_reasons(
        analysis
    )


    assert result == []



# ==========================================================
# Parent Detection
# ==========================================================

def test_hierarchy_reasons_detects_parent(monkeypatch):

    analysis = make_analysis()


    analysis.classification = {
        "Family": ChildFamily
    }


    monkeypatch.setattr(
        "analyzers.explanation_engine.hierarchy_builder.registry",
        MockRegistry
    )


    result = hierarchy_reasons(
        analysis
    )


    assert len(result) == 1



    observation = result[0]


    assert (
        observation.category
        ==
        "hierarchy"
    )


    assert (
        observation.importance
        ==
        9
    )



# ==========================================================
# Observation Content
# ==========================================================

def test_hierarchy_reason_text(monkeypatch):

    analysis = make_analysis()


    analysis.classification = {
        "Family": ChildFamily
    }


    monkeypatch.setattr(
        "analyzers.explanation_engine.hierarchy_builder.registry",
        MockRegistry
    )


    result = hierarchy_reasons(
        analysis
    )


    observation = result[0]


    assert (
        "Child Family"
        in observation.text
    )


    assert (
        "Root Family"
        in observation.text
    )



# ==========================================================
# Observation Metadata
# ==========================================================

def test_hierarchy_reason_metadata(monkeypatch):

    analysis = make_analysis()


    analysis.classification = {
        "Family": ChildFamily
    }


    monkeypatch.setattr(
        "analyzers.explanation_engine.hierarchy_builder.registry",
        MockRegistry
    )


    observation = hierarchy_reasons(
        analysis
    )[0]


    assert (
        observation.type
        ==
        "reason"
    )


    assert (
        observation.confidence
        ==
        "observed"
    )


    assert (
        observation.fact
        ==
        "family_hierarchy"
    )