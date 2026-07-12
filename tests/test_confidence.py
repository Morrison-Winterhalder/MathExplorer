from analyzers.pipeline.confidence import calculate_confidence


# ==========================================================
# Perfect Fit
# ==========================================================

def test_perfect_confidence():

    result = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=20,
        complexity=2
    )

    assert 80 <= result["Score"] <= 100


# ==========================================================
# Tie
# ==========================================================

def test_tie_confidence():

    result = calculate_confidence(
        winner_error=0,
        runner_up_error=0,
        sequence_length=20,
        complexity=2
    )

    assert result["Competition Penalty"] == 20


# ==========================================================
# No Runner-Up
# ==========================================================

def test_single_family_confidence():

    result = calculate_confidence(
        winner_error=0,
        runner_up_error=float("inf"),
        sequence_length=20,
        complexity=2
    )

    assert result["Score"] > 80


# ==========================================================
# Complexity Penalty
# ==========================================================

def test_complexity_penalty():

    simple = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=20,
        complexity=2
    )

    complicated = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=20,
        complexity=8
    )

    assert complicated["Score"] < simple["Score"]


# ==========================================================
# More Evidence
# ==========================================================

def test_sequence_length_bonus():

    short = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=5,
        complexity=2
    )

    long = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=100,
        complexity=2
    )

    assert long["Score"] > short["Score"]


# ==========================================================
# Worse Fit
# ==========================================================

def test_fit_penalty():

    perfect = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=20,
        complexity=2
    )

    noisy = calculate_confidence(
        winner_error=0.3,
        runner_up_error=1,
        sequence_length=20,
        complexity=2
    )

    assert noisy["Score"] < perfect["Score"]

# ==========================================================
# Keeping Scores In Bounds
# ==========================================================

def test_confidence_bounds():

    result = calculate_confidence(
        winner_error=0,
        runner_up_error=100,
        sequence_length=1000,
        complexity=0
    )

    assert 0 <= result["Score"] <= 100

# ==========================================================
# Negative / Impossible Inputs
# ==========================================================

def test_high_complexity_does_not_break_confidence():

    result = calculate_confidence(
        winner_error=0,
        runner_up_error=1,
        sequence_length=20,
        complexity=100
    )

    assert 0 <= result["Score"] <= 100

# ==========================================================
# Complexity
# ==========================================================

def test_complexity_breaks_equal_fit():

    simple = calculate_confidence(
        winner_error=0,
        runner_up_error=0,
        sequence_length=20,
        complexity=2
    )

    complex = calculate_confidence(
        winner_error=0,
        runner_up_error=0,
        sequence_length=20,
        complexity=8
    )

    assert complex["Score"] < simple["Score"]