from analyzers.pipeline.confidence import (
    update_confidence,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)



# ==========================================================
# Mock Family
# ==========================================================

class TestFamily:

    NAME = "Test Family"

    PARENT = "Root"

    NATURAL_FAMILY = True


    @staticmethod
    def complexity(parameters):

        return 1



# ==========================================================
# Helpers
# ==========================================================

def make_analysis():

    analysis = SequenceAnalysis(
        [1, 2, 3, 5]
    )


    analysis.recognition_scores = {

        "Best Fit": {

            "Winners": [

                {

                    "Family": TestFamily,

                    "Parameters": {},

                    "RRN": 0,

                }

            ],

            "Runner Up Score": None,

        }

    }


    return analysis



# ==========================================================
# Basic Confidence Creation
# ==========================================================

def test_confidence_generates_result():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.confidence
        is not None
    )


    assert (
        "Score"
        in analysis.confidence
    )


    assert (
        "Label"
        in analysis.confidence
    )



def test_confidence_contains_factors():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    assert (
        "Factors"
        in analysis.confidence
    )


    assert (
        len(
            analysis.confidence["Factors"]
        )
        > 0
    )



# ==========================================================
# Trace
# ==========================================================

def test_confidence_adds_reasoning_trace():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    events = [

        event["event"]

        for event in analysis.analysis_trace

    ]


    assert (
        "reasoning_generated"
        in events
    )



def test_reasoning_trace_contains_categories():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    reasoning = [

        event

        for event in analysis.analysis_trace

        if event["event"] == "reasoning_generated"

    ][0]


    assert (
        "primary"
        in reasoning
    )


    assert (
        "supporting"
        in reasoning
    )


    assert (
        "uncertainty"
        in reasoning
    )



# ==========================================================
# Factor Behavior
# ==========================================================

def test_exact_match_creates_primary_factor():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    names = [

        factor["name"]

        for factor in analysis.confidence["Factors"]

    ]


    assert (
        "Exact Formula Match"
        in names
    )



def test_natural_family_factor_exists():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    names = [

        factor["name"]

        for factor in analysis.confidence["Factors"]

    ]


    assert (
        "Natural Family"
        in names
    )



# ==========================================================
# Runner Up Handling
# ==========================================================

def test_confidence_handles_no_runner():

    analysis = make_analysis()


    update_confidence(
        analysis.sequence,
        analysis
    )


    competition = [

        factor

        for factor in analysis.confidence["Factors"]

        if factor["name"] == "No Competition"

    ]


    assert len(competition) == 1