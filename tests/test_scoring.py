from analyzers.core.report import initialize_analysis
from analyzers.pipeline.scoring import update_scores


# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_scoring():

    sequence = [1,3,5,7,9]

    report = initialize_analysis(sequence)
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

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    winner_names = {winner["Family"].NAME for winner in best["Winners"]}

    assert "Geometric" in winner_names


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_scoring():

    sequence = [1,4,9,16,25]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Squares"

# ==========================================================
# Centered Square
# ==========================================================

def test_centered_square_scoring():

    sequence = [1,5,13,25,41]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1

    assert (
        best["Winners"][0]["Family"].NAME
        ==
        "Centered Square Numbers"
    )

# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_scoring():

    sequence = [1,1,2,3,5]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]


    winner_names = {winner["Family"].NAME for winner in best["Winners"]}

    assert "Fibonacci" in winner_names

# ==========================================================
# Tribonacci
# ==========================================================

def test_tribonacci_scoring():

    sequence = [0,0,1,1,2,4,7]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    winner_names = {
        winner["Family"].NAME
        for winner in best["Winners"]
    }

    assert "Tribonacci Numbers" in winner_names

# ==========================================================
# Tetranacci
# ==========================================================

def test_tetranacci_scoring():

    sequence = [0,0,0,1,1,2,4,8]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    winner_names = {
        winner["Family"].NAME
        for winner in best["Winners"]
    }

    assert "Tetranacci Numbers" in winner_names

# ==========================================================
# Padovan
# ==========================================================

def test_padovan_scoring():

    sequence = [1,1,1,2,2,3,4]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    winner_names = {
        winner["Family"].NAME
        for winner in best["Winners"]
    }

    assert "Padovan Numbers" in winner_names

# ==========================================================
# Perrin
# ==========================================================

def test_perrin_scoring():

    sequence = [3,0,2,3,2,5,5]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    winner_names = {
        winner["Family"].NAME
        for winner in best["Winners"]
    }

    assert "Perrin Numbers" in winner_names

# ==========================================================
# Ranking Exists
# ==========================================================

def test_ranking_exists():

    sequence = [1,3,5,7,9]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    ranking = report["Recognition Scores"]["Ranking"]

    assert len(ranking) >= 2


# ==========================================================
# Runner-Up Exists
# ==========================================================

def test_specific_family_beats_polynomial():

    sequence = [2,6,18,54,162]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Geometric"


# ==========================================================
# Separation
# ==========================================================

def test_separation():

    sequence = [2,6,18,54,162]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    separation = report["Recognition Scores"]["Best Fit"]["Separation"]

    assert 0 <= separation <= 1


# ==========================================================
# Specificity
# ==========================================================

def test_specificity_breaks_polynomial_tie():
    sequence = [1, 4, 9, 16, 25]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert len(best["Winners"]) == 1
    assert best["Winners"][0]["Family"].NAME == "Squares"

    assert best["Runner Up"].NAME == "Polynomial"

# ==========================================================
# Parent Families Do Not Win
# ==========================================================

def test_parent_family_not_selected():

    sequence = [0,0,1,1,2,4,7]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert (
        best["Winners"][0]["Family"].NAME
        !=
        "Linear Recurrence"
    )

# ==========================================================
# Unknown Sequence
# ==========================================================

def test_unknown_sequence():

    sequence = [7,2,19,-4,81]

    report = initialize_analysis(sequence)
    update_scores(sequence, report)

    best = report["Recognition Scores"]["Best Fit"]

    assert best is not None
    assert best["Winners"][0]["Family"].NAME == "Polynomial"