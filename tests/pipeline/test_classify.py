from analyzers.pipeline.classify import (
    update_classification,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)


# ==========================================================
# Mock Families
# ==========================================================

class ParentFamily:

    NAME = "Parent Family"


class SimpleFamily:

    NAME = "Simple Family"
    PARENT = "Parent Family"

    @staticmethod
    def complexity(parameters):
        return 1


class ComplexFamily:

    NAME = "Complex Family"
    PARENT = "Parent Family"

    @staticmethod
    def complexity(parameters):
        return 5


# ==========================================================
# Mock Registry
# ==========================================================

class MockRegistry:

    @staticmethod
    def build_family_tree(family):

        return (
            f"{family.NAME}\n"
            "└── Parent Family"
        )


# ==========================================================
# Helpers
# ==========================================================

def make_analysis():

    return SequenceAnalysis(
        [1, 2, 3]
    )


def recognized_analysis():

    analysis = make_analysis()

    analysis.recognition_scores = {
        "Best Fit": {
            "Winners": [
                {
                    "Family": ComplexFamily,
                    "Parameters": {},
                    "Metadata": {
                        "NAME": "Complex Family"
                    },
                },
                {
                    "Family": SimpleFamily,
                    "Parameters": {
                        "test": True
                    },
                    "Metadata": {
                        "NAME": "Simple Family"
                    },
                },
            ]
        }
    }

    return analysis



# ==========================================================
# Unknown Classification
# ==========================================================

def test_classification_unknown_when_no_best_fit():

    analysis = make_analysis()

    analysis.recognition_scores = {
        "Best Fit": None
    }


    update_classification(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.classification["Type"]
        ==
        "Unknown"
    )


    assert (
        analysis.family
        is None
    )


    assert (
        analysis.classification["Reason"]
        ==
        "No family successfully recognized the sequence."
    )



def test_unknown_classification_trace():

    analysis = make_analysis()

    analysis.recognition_scores = {
        "Best Fit": None
    }


    update_classification(
        analysis.sequence,
        analysis
    )


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert (
        "classification_started"
        in events
    )

    assert (
        "classification_completed"
        in events
    )



# ==========================================================
# Winner Selection
# ==========================================================

def test_classification_selects_lowest_complexity(monkeypatch):

    monkeypatch.setattr(
        "analyzers.pipeline.classify.registry",
        MockRegistry
    )


    analysis = recognized_analysis()


    update_classification(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.family
        ==
        SimpleFamily
    )



def test_classification_stores_parameters():

    analysis = recognized_analysis()


    update_classification(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.parameters
        ==
        {
            "test": True
        }
    )



def test_classification_stores_metadata():

    analysis = recognized_analysis()


    update_classification(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.classification["Metadata"]
        ==
        {
            "NAME": "Simple Family"
        }
    )



# ==========================================================
# Hierarchy
# ==========================================================

def test_classification_builds_hierarchy(monkeypatch):

    monkeypatch.setattr(
        "analyzers.pipeline.classify.registry",
        MockRegistry
    )


    analysis = recognized_analysis()


    update_classification(
        analysis.sequence,
        analysis
    )


    assert (
        "Simple Family"
        in
        analysis.hierarchy
    )


    assert (
        "Parent Family"
        in
        analysis.hierarchy
    )



# ==========================================================
# Trace
# ==========================================================

def test_classification_adds_family_selected_event():

    analysis = recognized_analysis()


    update_classification(
        analysis.sequence,
        analysis
    )


    selected = [
        event
        for event in analysis.analysis_trace
        if event["event"] == "family_selected"
    ]


    assert len(selected) == 1


    assert (
        selected[0]["family"]
        ==
        "Simple Family"
    )



def test_classification_completed_contains_family():

    analysis = recognized_analysis()


    update_classification(
        analysis.sequence,
        analysis
    )


    completed = [
        event
        for event in analysis.analysis_trace
        if event["event"] == "classification_completed"
    ][0]


    assert (
        completed["family"]
        ==
        "Simple Family"
    )