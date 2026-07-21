from analyzers.pipeline.prediction import (
    predict_terms,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)



# ==========================================================
# Mock Family
# ==========================================================

class TestFamily:

    NAME = "Test Family"


    @staticmethod
    def evaluate(parameters, n):

        return n * 10



# ==========================================================
# Helpers
# ==========================================================

def make_analysis():

    analysis = SequenceAnalysis(
        [1, 2, 3, 4]
    )


    analysis.classification = {

        "Family": TestFamily,

        "Parameters": {},

    }


    return analysis



# ==========================================================
# Missing Classification
# ==========================================================

def test_prediction_skips_without_family():

    analysis = SequenceAnalysis(
        [1, 2, 3]
    )


    result = predict_terms(
        analysis.sequence,
        analysis
    )


    assert result == []


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert (
        "prediction_skipped"
        in events
    )



def test_prediction_skips_without_parameters():

    analysis = SequenceAnalysis(
        [1, 2, 3]
    )


    analysis.classification = {

        "Family": TestFamily,

        "Parameters": None,

    }


    result = predict_terms(
        analysis.sequence,
        analysis
    )


    assert result == []



# ==========================================================
# Prediction Generation
# ==========================================================

def test_prediction_generates_terms():

    analysis = make_analysis()


    result = predict_terms(
        analysis.sequence,
        analysis,
        number_of_terms=5
    )


    assert result == [

        50,
        60,
        70,
        80,
        90,

    ]



def test_prediction_respects_requested_amount():

    analysis = make_analysis()


    result = predict_terms(
        analysis.sequence,
        analysis,
        number_of_terms=3
    )


    assert len(result) == 3



# ==========================================================
# Index Handling
# ==========================================================

def test_prediction_starts_after_sequence():

    analysis = make_analysis()


    result = predict_terms(
        analysis.sequence,
        analysis,
        number_of_terms=1
    )


    assert result[0] == 50



# ==========================================================
# Trace Validation
# ==========================================================

def test_prediction_adds_started_event():

    analysis = make_analysis()


    predict_terms(
        analysis.sequence,
        analysis
    )


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert (
        "prediction_started"
        in events
    )



def test_prediction_adds_formula_event():

    analysis = make_analysis()


    predict_terms(
        analysis.sequence,
        analysis
    )


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert (
        "formula_available"
        in events
    )



def test_prediction_adds_generated_event():

    analysis = make_analysis()


    predict_terms(
        analysis.sequence,
        analysis
    )


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert (
        "predictions_generated"
        in events
    )


    assert (
        "prediction_finalized"
        in events
    )



def test_prediction_trace_order():

    analysis = make_analysis()


    predict_terms(
        analysis.sequence,
        analysis
    )


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert events == [

        "prediction_started",

        "formula_available",

        "predictions_generated",

        "prediction_finalized",

    ]