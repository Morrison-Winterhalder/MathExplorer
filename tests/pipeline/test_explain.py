from analyzers.pipeline.explain import (
    update_explanation,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)



# ==========================================================
# Mock Family
# ==========================================================

class TestFamily:

    NAME = "Test Family"



# ==========================================================
# No Family
# ==========================================================

def test_explanation_skips_without_family():

    analysis = SequenceAnalysis(
        [1, 2, 3]
    )


    update_explanation(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.explanation
        is None
    )



# ==========================================================
# Successful Explanation
# ==========================================================

def test_explanation_is_generated(monkeypatch):

    analysis = SequenceAnalysis(
        [1, 2, 3]
    )


    analysis.classification = {
        "Family": TestFamily
    }


    expected = {

        "Summary": "Test explanation",

        "Reasons": [

            "Reason one"

        ]

    }


    def fake_builder(sequence, report):

        assert sequence == [
            1,
            2,
            3
        ]

        assert report is analysis

        return expected



    monkeypatch.setattr(
        "analyzers.pipeline.explain.build_explanation",
        fake_builder
    )


    update_explanation(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.explanation
        ==
        expected
    )



# ==========================================================
# Builder Invocation
# ==========================================================

def test_explanation_uses_existing_family(monkeypatch):

    analysis = SequenceAnalysis(
        [5, 10, 15]
    )


    analysis.classification = {
        "Family": TestFamily
    }


    called = {
        "value": False
    }



    def fake_builder(sequence, report):

        called["value"] = True

        return {}



    monkeypatch.setattr(
        "analyzers.pipeline.explain.build_explanation",
        fake_builder
    )


    update_explanation(
        analysis.sequence,
        analysis
    )


    assert (
        called["value"]
        is True
    )



# ==========================================================
# Replacement Behavior
# ==========================================================

def test_existing_explanation_is_replaced(monkeypatch):

    analysis = SequenceAnalysis(
        [1, 1, 2]
    )


    analysis.classification = {
        "Family": TestFamily
    }


    analysis.explanation = {
        "Old": True
    }



    monkeypatch.setattr(
        "analyzers.pipeline.explain.build_explanation",
        lambda sequence, report: {
            "New": True
        }
    )


    update_explanation(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.explanation
        ==
        {
            "New": True
        }
    )