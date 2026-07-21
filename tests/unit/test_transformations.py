from analyzers.core.transformations import (
    first_differences,
    nth_differences,
    first_ratios,
    subtract_sequences,
)


# ==========================================================
# first_differences()
# ==========================================================

def test_first_differences_basic():
    assert first_differences([1, 4, 9, 16]) == [3, 5, 7]


def test_first_differences_constant():
    assert first_differences([7, 7, 7, 7]) == [0, 0, 0]


def test_first_differences_negative():
    assert first_differences([-5, -2, 2, 7]) == [3, 4, 5]


def test_first_differences_single():
    assert first_differences([42]) == []


def test_first_differences_empty():
    assert first_differences([]) == []


# ==========================================================
# nth_differences()
# ==========================================================

def test_second_differences():
    sequence = [1, 4, 9, 16, 25]
    assert nth_differences(sequence, 2) == [2, 2, 2]


def test_third_differences():
    sequence = [1, 8, 27, 64, 125]
    assert nth_differences(sequence, 3) == [6, 6]


def test_zero_order_difference():
    sequence = [5, 10, 15]
    assert nth_differences(sequence, 0) == sequence


def test_nth_difference_single():
    assert nth_differences([5], 3) == []


def test_nth_difference_empty():
    assert nth_differences([], 4) == []


# ==========================================================
# first_ratios()
# ==========================================================

def test_first_ratios_geometric():
    assert first_ratios([2, 4, 8, 16]) == [2, 2, 2]


def test_first_ratios_fractional():
    assert first_ratios([8, 4, 2, 1]) == [0.5, 0.5, 0.5]


def test_first_ratios_negative():
    assert first_ratios([-2, 4, -8, 16]) == [-2, -2, -2]


def test_first_ratios_zero_division():
    assert first_ratios([0, 5, 10]) == [None, 2]


def test_first_ratios_single():
    assert first_ratios([3]) == []


def test_first_ratios_empty():
    assert first_ratios([]) == []


# ==========================================================
# subtract_sequences()
# ==========================================================

def test_subtract_sequences_basic():
    assert subtract_sequences(
        [5, 7, 9],
        [1, 2, 3]
    ) == [4, 5, 6]


def test_subtract_sequences_zero():
    assert subtract_sequences(
        [4, 5, 6],
        [4, 5, 6]
    ) == [0, 0, 0]


def test_subtract_sequences_negative():
    assert subtract_sequences(
        [1, -2, 3],
        [-1, -4, 2]
    ) == [2, 2, 1]


def test_subtract_sequences_float():
    assert subtract_sequences(
        [2.5, 4.5],
        [1.5, 2.0]
    ) == [1.0, 2.5]