from analyzers.pipeline.scoring import (
    score_family,
    choose_best_fit,
)

from analyzers.core.analysis import (
    SequenceAnalysis,
)


# ==========================================================
# Mock Families
# ==========================================================

class PerfectFamily:

    NAME = "Perfect Family"
    SPECIFICITY = 50

    @staticmethod
    def fit(sequence):

        return {
            "Parameters": {},
            "Predicted": sequence.copy(),
        }


    @staticmethod
    def evaluate(parameters, n):

        return n


    @staticmethod
    def complexity(parameters):

        return 1


    @staticmethod
    def formula(parameters):

        return "a(n)=n"



class FailedFamily:

    NAME = "Failed Family"
    SPECIFICITY = 50


    @staticmethod
    def fit(sequence):

        return None



class SpecificFamily:

    NAME = "Specific Family"
    SPECIFICITY = 90

    @staticmethod
    def complexity(parameters):

        return 1



class GeneralFamily:

    NAME = "General Family"
    SPECIFICITY = 10

    @staticmethod
    def complexity(parameters):

        return 1



class ComplexFamily:

    NAME = "Complex Family"
    SPECIFICITY = 50

    @staticmethod
    def complexity(parameters):

        return 10



# ==========================================================
# Helpers
# ==========================================================

def make_analysis():

    return SequenceAnalysis(
        [1, 2, 3]
    )



def make_score(
    family,
    rrn,
    complexity=1,
):

    return {

        "Family": family,

        "Parameters": {},

        "Predicted": [
            1,
            2,
            3
        ],

        "Residuals": [
            0,
            0,
            0
        ],

        "RRN": rrn,

        "NRMSE": rrn,

        "R2": 1.0,

        "Metadata": {},

        "Complexity": complexity,

    }



# ==========================================================
# score_family()
# ==========================================================

def test_score_family_returns_metrics():

    result = score_family(
        [1, 2, 3],
        PerfectFamily,
    )


    assert result is not None

    assert result["Family"] is PerfectFamily

    assert "Predicted" in result

    assert "RRN" in result

    assert "NRMSE" in result

    assert "R2" in result



def test_score_family_rejects_failed_fit():

    result = score_family(
        [1, 2, 3],
        FailedFamily,
    )


    assert result is None



# ==========================================================
# choose_best_fit()
# ==========================================================

def test_choose_best_fit_selects_lowest_error():

    analysis = make_analysis()


    scores = [

        make_score(
            GeneralFamily,
            0.5,
        ),

        make_score(
            PerfectFamily,
            0.0,
        ),

    ]


    result = choose_best_fit(
        scores,
        analysis,
    )


    winner = (
        result["Best Fit"]["Winners"][0]
    )


    assert (
        winner["Family"].NAME
        ==
        "Perfect Family"
    )



def test_choose_best_fit_adds_complexity():

    analysis = make_analysis()


    scores = [

        make_score(
            ComplexFamily,
            0.1,
        )

    ]


    choose_best_fit(
        scores,
        analysis,
    )


    assert (
        scores[0]["Complexity"]
        ==
        10
    )


    assert (
        scores[0]["Ranking Score"]
        ==
        0.11
    )



# ==========================================================
# Tie Resolution
# ==========================================================

def test_tie_detected():

    analysis = make_analysis()


    scores = [

        make_score(
            GeneralFamily,
            0.0,
        ),

        make_score(
            SpecificFamily,
            0.0,
        ),

    ]


    choose_best_fit(
        scores,
        analysis,
    )


    events = [
        event["event"]
        for event in analysis.analysis_trace
    ]


    assert (
        "tie_detected"
        in events
    )



def test_specificity_resolves_tie():

    analysis = make_analysis()


    scores = [

        make_score(
            GeneralFamily,
            0.0,
        ),

        make_score(
            SpecificFamily,
            0.0,
        ),

    ]


    result = choose_best_fit(
        scores,
        analysis,
    )


    winner = (
        result["Best Fit"]["Winners"][0]
    )


    assert (
        winner["Family"].NAME
        ==
        "Specific Family"
    )



# ==========================================================
# Trace Validation
# ==========================================================

def test_ranking_trace_created():

    analysis = make_analysis()


    scores = [

        make_score(
            PerfectFamily,
            0.0,
        )

    ]


    choose_best_fit(
        scores,
        analysis,
    )


    events = [
        item["event"]
        for item in analysis.analysis_trace
    ]


    assert (
        "ranking_calculated"
        in events
    )


    assert (
        "family_ranked"
        in events
    )



def test_winner_selected_trace():

    analysis = make_analysis()


    scores = [

        make_score(
            PerfectFamily,
            0.0,
        )

    ]


    choose_best_fit(
        scores,
        analysis,
    )


    events = [
        item["event"]
        for item in analysis.analysis_trace
    ]


    assert (
        "winner_selected"
        in events
    )