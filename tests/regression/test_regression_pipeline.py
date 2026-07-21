import pytest

from analyzers.sequence_analysis import analyze_sequence


# ============================================================
# Regression Sequences
# ============================================================

SEQUENCES = [
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
        [2, 4, 8, 16, 32, 64],
        "Geometric",
    ),

    (
        [1, 4, 9, 16, 25, 36, 49],
        "Squares",
    ),

    (
        [1, 8, 27, 64, 125, 216],
        "Cubes",
    ),

    (
        [1, 2, 6, 24, 120, 720],
        "Factorials",
    ),

    (
        [0, 0, 1, 0, 2, 0, 2, 2, 1, 6],
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


def get_family_name(analysis):

    return analysis.family_name


# ============================================================
# Classification
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_pipeline_classifies_correct_family(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert get_family_name(
        analysis
    ) == expected_family


# ============================================================
# Recognition
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_pipeline_contains_recognition_result(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis.recognition_scores

    assert "Scores" in (
        analysis.recognition_scores
    )

    assert "Ranking" in (
        analysis.recognition_scores
    )

    assert "Best Fit" in (
        analysis.recognition_scores
    )


@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_pipeline_contains_classification_result(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis.classification

    assert "Family" in (
        analysis.classification
    )

    assert (
        analysis.family_name
        == expected_family
    )


@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_pipeline_classification_matches_recognition(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    best_fit = (
        analysis.recognition_scores
        .get("Best Fit")
    )

    assert best_fit is not None

    winners = (
        best_fit
        .get("Winners", [])
    )

    assert winners

    winner_names = [
        winner["Family"].NAME
        for winner in winners
    ]

    assert (
        expected_family
        in winner_names
    )


# ============================================================
# Explanation
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_pipeline_contains_explanation(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis.explanation is not None

    assert isinstance(
        analysis.explanation,
        dict,
    )


# ============================================================
# Determinism
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
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

    assert (
        first.family_name
        == second.family_name
    )

    assert (
        first.family_name
        == expected_family
    )

    assert (
        first.recognition_scores
        == second.recognition_scores
    )


# ============================================================
# Complete Analysis
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_pipeline_returns_complete_analysis(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    assert analysis is not None

    assert hasattr(
        analysis,
        "sequence",
    )

    assert hasattr(
        analysis,
        "classification",
    )

    assert hasattr(
        analysis,
        "recognition_scores",
    )

    assert hasattr(
        analysis,
        "explanation",
    )

    assert hasattr(
        analysis,
        "analysis_trace",
    )

    assert hasattr(
        analysis,
        "verification",
    )

    assert hasattr(
        analysis,
        "predictions",
    )

    assert hasattr(
        analysis,
        "confidence_data",
    )


# ============================================================
# Later Pipeline Stages Preserve Classification
# ============================================================

@pytest.mark.parametrize(
    "sequence, expected_family",
    SEQUENCES,
)
def test_later_pipeline_stages_preserve_classification(
    sequence,
    expected_family,
):

    analysis = run_pipeline(
        sequence
    )

    original_family = (
        analysis.family_name
    )

    assert (
        original_family
        == expected_family
    )

    assert (
        analysis.family_name
        == expected_family
    )

    assert (
        analysis.classification
        is not None
    )