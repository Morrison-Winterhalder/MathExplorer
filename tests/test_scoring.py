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

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Arithmetic"

    assert best["Winners"][0]["RRN"] == 0
    assert best["Winners"][0]["R2"] == 1


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_scoring():

    sequence = [2,6,18,54,162]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    winner_names = {winner["Family"].NAME for winner in best["Winners"]}

    assert "Geometric" in winner_names


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_scoring():

    sequence = [1,4,9,16,25]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Squares"


# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_scoring():

    sequence = [1,1,2,3,5]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]


    winner_names = {winner["Family"].NAME for winner in best["Winners"]}

    assert "Fibonacci" in winner_names


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

def test_specific_family_beats_polynomial():

    sequence = [2,6,18,54,162]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Geometric"


# ==========================================================
# Separation
# ==========================================================

def test_separation():

    sequence = [2,6,18,54,162]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    separation = report["Recognition Scores"]["Best Fit"]["Separation"]

    assert 0 <= separation <= 1


# ==========================================================
# Specificity
# ==========================================================

def test_specificity_breaks_polynomial_tie():
    sequence = [1, 4, 9, 16, 25]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Squares"

    assert best["Runner Up"].NAME == "Polynomial"


# ==========================================================
# Unknown Sequence
# ==========================================================

def test_unknown_sequence():

    sequence = [7,2,19,-4,81]

    report = initialize_report(sequence)
    update_scores(sequence, report)

    assert "Recognition Scores" in report