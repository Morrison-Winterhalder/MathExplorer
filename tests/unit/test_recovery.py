# tests/unit/test_recovery.py

from analyzers.pipeline.recovery import (
    recover_formula,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)


# ==========================================================
# Mock Families
# ==========================================================

class MockFamily:

    NAME = "Mock Family"

    @staticmethod
    def formula(parameters):

        return "a(n)=n²"



class ParameterFamily:

    NAME = "Parameter Family"

    @staticmethod
    def formula(parameters):

        return parameters["formula"]



class BrokenFamily:

    NAME = "Broken Family"

    @staticmethod
    def formula(parameters):

        raise KeyError("missing parameter")



# ==========================================================
# Helpers
# ==========================================================

def make_analysis(
    family=None,
    parameters=None,
):

    analysis = SequenceAnalysis(
        [1, 2, 3]
    )

    if family is not None:

        analysis.classification = {
            "Family": family,
            "Parameters": parameters or {},
        }

    return analysis



# ==========================================================
# No Classification
# ==========================================================

def test_recovery_skips_without_family():

    analysis = make_analysis()

    recover_formula(
        [1, 2, 3],
        analysis,
    )

    assert analysis.formula is None

    assert (
        analysis.analysis_trace[0]["event"]
        ==
        "recovery_skipped"
    )

    assert (
        analysis.analysis_trace[0]["reason"]
        ==
        "no_classification"
    )



# ==========================================================
# Successful Recovery
# ==========================================================

def test_recovery_generates_formula():

    analysis = make_analysis(
        MockFamily,
        {}
    )

    recover_formula(
        [1, 4, 9],
        analysis,
    )

    assert (
        analysis.formula
        ==
        "a(n)=n²"
    )



def test_recovery_starts_trace():

    analysis = make_analysis(
        MockFamily,
        {}
    )

    recover_formula(
        [1, 4, 9],
        analysis,
    )


    first = analysis.analysis_trace[0]


    assert (
        first["event"]
        ==
        "recovery_started"
    )


    assert (
        first["family"]
        ==
        "Mock Family"
    )



def test_recovery_finishes_trace():

    analysis = make_analysis(
        MockFamily,
        {}
    )

    recover_formula(
        [1, 4, 9],
        analysis,
    )


    last = analysis.analysis_trace[-1]


    assert (
        last["event"]
        ==
        "formula_recovered"
    )


    assert (
        last["formula"]
        ==
        "a(n)=n²"
    )



# ==========================================================
# Parameters
# ==========================================================

def test_recovery_passes_parameters():

    analysis = make_analysis(
        ParameterFamily,
        {
            "formula": "custom formula"
        }
    )


    recover_formula(
        [1],
        analysis,
    )


    assert (
        analysis.formula
        ==
        "custom formula"
    )



# ==========================================================
# Error Handling
# ==========================================================

def test_recovery_handles_formula_failure():

    analysis = make_analysis(
        BrokenFamily,
        {}
    )


    recover_formula(
        [1],
        analysis,
    )


    assert analysis.formula is None


    assert (
        analysis.analysis_trace[-1]["event"]
        ==
        "formula_recovered"
    )


    assert (
        analysis.analysis_trace[-1]["formula"]
        is None
    )



# ==========================================================
# Event Ordering
# ==========================================================

def test_recovery_event_order():

    analysis = make_analysis(
        MockFamily,
        {}
    )


    recover_formula(
        [1],
        analysis,
    )


    events = [
        item["event"]
        for item in analysis.analysis_trace
    ]


    assert events == [
        "recovery_started",
        "formula_recovered",
    ]