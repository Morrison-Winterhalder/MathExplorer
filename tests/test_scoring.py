from analyzers.core.report import initialize_report
from analyzers.pipeline.scoring import update_scores


# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_scoring():

    sequence = [1,3,5,7,9]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert best["Winner"] == "Arithmetic"
    assert best["Winner Score"]["RRN"] == 0
    assert best["Winner Score"]["R2"] == 1


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_scoring():

    sequence = [2,6,18,54,162]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert best["Winner"] == "Geometric"


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_scoring():

    sequence = [1,4,9,16,25]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert best["Winner"] == "Polynomial"


# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_scoring():

    sequence = [1,1,2,3,5]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert best["Winner"] == "Fibonacci"


# ==========================================================
# Ranking Exists
# ==========================================================

def test_ranking_exists():

    sequence = [1,3,5,7,9]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    ranking = report["Recognition Scores"]["Ranking"]

    assert len(ranking) >= 2


# ==========================================================
# Runner-Up Exists
# ==========================================================

def test_runner_up_exists():

    sequence = [1,3,5,7,9]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert best["Runner Up"] is not None


# ==========================================================
# Separation
# ==========================================================

def test_separation():

    sequence = [1,3,5,7,9]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    separation = report["Recognition Scores"]["Best Fit"]["Separation"]

    assert 0 <= separation <= 1


# ==========================================================
# Unknown Sequence
# ==========================================================

def test_unknown_sequence():

    sequence = [7,2,19,-4,81]

    report = initialize_report(sequence)

    update_scores(sequence, report)

    assert "Recognition Scores" in report