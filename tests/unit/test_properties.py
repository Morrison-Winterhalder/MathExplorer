from analyzers.core.properties import (
    is_increasing,
    is_decreasing,
    is_unique,
    determine_monotonic,
)


# ==========================================================
# is_increasing()
# ==========================================================

def test_increasing_sequence():

    assert is_increasing(
        [1, 2, 3, 4]
    ) is True



def test_not_increasing_when_decreasing():

    assert is_increasing(
        [4, 3, 2, 1]
    ) is False



def test_not_increasing_with_equal_values():

    assert is_increasing(
        [1, 2, 2, 3]
    ) is False



def test_increasing_single_term():

    assert is_increasing(
        [5]
    ) is None



# ==========================================================
# is_decreasing()
# ==========================================================

def test_decreasing_sequence():

    assert is_decreasing(
        [5, 4, 3, 2]
    ) is True



def test_not_decreasing_when_increasing():

    assert is_decreasing(
        [1, 2, 3]
    ) is False



def test_not_decreasing_with_equal_values():

    assert is_decreasing(
        [5, 4, 4, 2]
    ) is False



def test_decreasing_single_term():

    assert is_decreasing(
        [5]
    ) is None



# ==========================================================
# is_unique()
# ==========================================================

def test_unique_sequence():

    assert is_unique(
        [1, 2, 3, 4]
    ) is True



def test_non_unique_sequence():

    assert is_unique(
        [1, 2, 2, 3]
    ) is False



def test_unique_single_term():

    assert is_unique(
        [7]
    ) is None



# ==========================================================
# determine_monotonic()
# ==========================================================

def test_determine_increasing():

    assert determine_monotonic(
        [1, 2, 3, 4]
    ) == "Increasing"



def test_determine_decreasing():

    assert determine_monotonic(
        [4, 3, 2, 1]
    ) == "Decreasing"



def test_determine_constant():

    assert determine_monotonic(
        [5, 5, 5, 5]
    ) == "Constant"



def test_determine_not_monotonic():

    assert determine_monotonic(
        [1, 3, 2, 4]
    ) == "Not Monotonic"



def test_determine_two_term_increasing():

    assert determine_monotonic(
        [1, 2]
    ) == "Increasing"



def test_determine_two_term_decreasing():

    assert determine_monotonic(
        [2, 1]
    ) == "Decreasing"