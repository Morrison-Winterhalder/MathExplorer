from analyzers.pipeline.verification import (
    regenerate_sequence,
    verify_sequence,
    finalize_report,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)



# ==========================================================
# Mock Family
# ==========================================================

class PerfectFamily:

    NAME = "Perfect Family"


    @staticmethod
    def evaluate(parameters, n):

        return n * 2



class IncorrectFamily:

    NAME = "Incorrect Family"


    @staticmethod
    def evaluate(parameters, n):

        return n * 3



# ==========================================================
# Helpers
# ==========================================================

def make_analysis(family=PerfectFamily):

    analysis = SequenceAnalysis(
        [2, 4, 6, 8]
    )


    analysis.classification = {

        "Family": family,

        "Parameters": {},

    }


    return analysis



# ==========================================================
# Regeneration
# ==========================================================

def test_regenerate_sequence():

    analysis = make_analysis()


    result = regenerate_sequence(
        analysis.sequence,
        analysis
    )


    assert result == [

        2,
        4,
        6,
        8,

    ]



def test_regenerate_uses_family_evaluate():

    class TrackingFamily:

        NAME = "Tracking"


        calls = []


        @staticmethod
        def evaluate(parameters, n):

            TrackingFamily.calls.append(n)

            return n


    analysis = make_analysis(
        TrackingFamily
    )


    regenerate_sequence(
        analysis.sequence,
        analysis
    )


    assert TrackingFamily.calls == [

        1,
        2,
        3,
        4,

    ]



# ==========================================================
# Verification
# ==========================================================

def test_verify_sequence_true_when_matching():

    analysis = make_analysis()


    assert verify_sequence(
        analysis.sequence,
        analysis
    ) is True



def test_verify_sequence_false_when_wrong():

    analysis = make_analysis(
        IncorrectFamily
    )


    assert verify_sequence(
        analysis.sequence,
        analysis
    ) is False



# ==========================================================
# Finalization
# ==========================================================

def test_finalize_report_marks_verified():

    analysis = make_analysis()


    finalize_report(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.verification["Verified"]
        is True
    )



def test_finalize_report_generates_predictions():

    analysis = make_analysis()


    finalize_report(
        analysis.sequence,
        analysis
    )


    assert analysis.predictions["Next Terms"] == [

        10,
        12,
        14,
        16,
        18,

    ]



# ==========================================================
# Missing Classification
# ==========================================================

def test_finalize_report_skips_without_family():

    analysis = SequenceAnalysis(
        [1, 2, 3]
    )


    finalize_report(
        analysis.sequence,
        analysis
    )


    assert (
        analysis.verification["Verified"]
        is None
    )


    assert (
        analysis.predictions["Next Terms"]
        is None
    )



# ==========================================================
# Trace
# ==========================================================

def test_verification_started_event():

    analysis = make_analysis()


    finalize_report(
        analysis.sequence,
        analysis
    )


    events = [

        event["event"]

        for event in analysis.analysis_trace

    ]


    assert (
        "verification_started"
        in events
    )



def test_verification_completed_event():

    analysis = make_analysis()


    finalize_report(
        analysis.sequence,
        analysis
    )


    events = [

        event["event"]

        for event in analysis.analysis_trace

    ]


    assert (
        "verification_completed"
        in events
    )



def test_pipeline_completed_event():

    analysis = make_analysis()


    finalize_report(
        analysis.sequence,
        analysis
    )


    events = [

        event["event"]

        for event in analysis.analysis_trace

    ]


    assert (
        "analysis_completed"
        in events
    )



def test_verification_event_order():

    analysis = make_analysis()


    finalize_report(
        analysis.sequence,
        analysis
    )


    events = [

        event["event"]

        for event in analysis.analysis_trace

    ]


    assert events[-3:] == [

        "verification_started",

        "verification_completed",

        "analysis_completed",

    ]