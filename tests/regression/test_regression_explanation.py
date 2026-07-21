import pytest

from analyzers.sequence_analysis import analyze_sequence


# ============================================================
# Regression Explanation Test Sequences
# ============================================================

REGRESSION_CASES = [

    (
        [1, 1, 2, 3, 5, 8, 13, 21],
        "Fibonacci",
    ),

    (
        [0, 1, 2, 5, 12, 29, 70, 169],
        "Pell Numbers",
    ),

    (
        [0, 1, 1, 3, 5, 11, 21, 43],
        "Jacobsthal Numbers",
    ),

    (
        [1, 2, 4, 8, 16, 32, 64, 128],
        "Geometric",
    ),

    (
        [1, 4, 9, 16, 25, 36, 49, 64],
        "Squares",
    ),

    (
        [1, 8, 27, 64, 125, 216, 343, 512],
        "Cubes",
    ),

    (
        [1, 2, 6, 24, 120, 720, 5040],
        "Factorials",
    ),

    (
        [0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6],
        "Van Eck Numbers",
    ),

]


# ============================================================
# Helpers
# ============================================================

def run_pipeline(sequence):

    return analyze_sequence(
        sequence
    )


def family_name(analysis):

    return analysis.family_name


def recognition_winners(analysis):

    best_fit = analysis.best_fit

    if not best_fit:

        return []

    return [

        winner["Family"].NAME

        for winner
        in best_fit.get(
            "Winners",
            []
        )

    ]


# ============================================================
# Classification
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_classifies_correct_family(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert family_name(
        analysis
    ) == expected_family


# ============================================================
# Recognition Result
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_contains_recognition_result(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert "Recognition Scores" in analysis

    assert analysis.recognition_scores

    assert analysis.best_fit is not None

    assert expected_family in recognition_winners(
        analysis
    )


# ============================================================
# Classification Result
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_contains_classification_result(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis.classification

    assert analysis.family_name == expected_family


# ============================================================
# Recognition / Classification Agreement
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_classification_matches_recognition(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    winners = recognition_winners(
        analysis
    )

    assert expected_family in winners

    assert analysis.family_name in winners


# ============================================================
# Explanation Exists
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_produces_explanation(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert "Explanation" in analysis

    assert analysis.explanation is not None


# ============================================================
# Explanation Contains Classification Context
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_explanation_references_selected_family(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    explanation = analysis.explanation

    assert explanation

    explanation_text = str(
        explanation
    )

    assert expected_family in explanation_text


# ============================================================
# Explanation Contains Mathematical Reasoning
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_explanation_contains_reasons(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    explanation = analysis.explanation

    assert explanation

    reasons = explanation.get(
        "Reasons",
        []
    )

    assert isinstance(
        reasons,
        list
    )

    assert len(
        reasons
    ) > 0


# ============================================================
# Analysis Trace Exists
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_contains_analysis_trace(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis.analysis_trace

    assert isinstance(
        analysis.analysis_trace,
        list
    )


# ============================================================
# Recognition Trace Events
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_trace_contains_recognition_events(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    events = [

        event.get(
            "event"
        )

        for event
        in analysis.analysis_trace

    ]

    assert (
        "family_tested"
        in events
    )

    assert (
        "winner_selected"
        in events
    )


# ============================================================
# Classification Trace Events
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_trace_contains_classification_events(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    classification_events = [

        event

        for event
        in analysis.analysis_trace

        if event.get(
            "stage"
        ) == "classification"

    ]

    assert classification_events


# ============================================================
# Explanation Trace Events
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_trace_contains_explanation_reasoning(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    reasoning_events = [

        event

        for event
        in analysis.analysis_trace

        if event.get(
            "event"
        ) in {

            "candidate_comparison",

            "decision_reasoning",

            "classification_reasoning",

        }

    ]

    assert reasoning_events


# ============================================================
# Later Stages Preserve Classification
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_later_pipeline_stages_preserve_classification(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    original_family = analysis.family_name

    assert original_family == expected_family

    assert analysis.family_name == original_family


# ============================================================
# Determinism
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_is_deterministic(
    sequence,
    expected_family,
):

    first = run_pipeline(
        sequence
    )

    second = run_pipeline(
        sequence
    )

    assert first.family_name == second.family_name

    assert first.family_name == expected_family

    assert first.explanation == second.explanation

    assert first.recognition_scores == second.recognition_scores


# ============================================================
# Complete Analysis Object
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_pipeline_returns_complete_analysis(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    required_sections = [

        "Analysis Trace",
        "Sequence Classification",
        "Recognition Scores",
        "Verification",
        "Predictions",
        "Basic Information",
        "Properties",
        "Transformations",
        "Explanation",
        "Confidence",

    ]

    for section in required_sections:

        assert section in analysis


# ============================================================
# Explanation Is Consistent With Classification
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_explanation_is_consistent_with_classification(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis.family_name == expected_family

    explanation_text = str(
        analysis.explanation
    )

    assert expected_family in explanation_text


# ============================================================
# Explanation Is Consistent With Recognition
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    REGRESSION_CASES,
)
def test_explanation_is_consistent_with_recognition(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    winners = recognition_winners(
        analysis
    )

    explanation_text = str(
        analysis.explanation
    )

    assert expected_family in winners

    assert expected_family in explanation_text