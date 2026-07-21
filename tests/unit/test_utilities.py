import pytest

from analyzers.core.utilities import (
    pretty,
    integer_nth_root,
)


# ==========================================================
# pretty()
# ==========================================================

def test_pretty_integer():
    assert pretty(5) == "5"


def test_pretty_negative_integer():
    assert pretty(-12) == "-12"


def test_pretty_integer_float():
    assert pretty(5.0) == "5"


def test_pretty_decimal():
    assert pretty(3.1415926) == "3.1416"


def test_pretty_decimal_trailing_zero():
    assert pretty(2.5000) == "2.5"


def test_pretty_small_decimal():
    assert pretty(0.125) == "0.125"


def test_pretty_list():
    assert pretty([1, 2.5, 3]) == "[1, 2.5, 3]"


def test_pretty_nested_list():
    assert pretty([[1, 2], [3, 4]]) == "[[1, 2], [3, 4]]"


def test_pretty_tuple():
    assert pretty((1, 2.5, 3)) == "(1, 2.5, 3)"


def test_pretty_nested_tuple():
    assert pretty(((1, 2), (3, 4))) == "((1, 2), (3, 4))"


def test_pretty_mixed():
    assert pretty([1, (2, 3.5)]) == "[1, (2, 3.5)]"


def test_pretty_string():
    assert pretty("MathExplorer") == "MathExplorer"


# ==========================================================
# integer_nth_root()
# ==========================================================

def test_square_root():
    assert integer_nth_root(49, 2) == 7


def test_cube_root():
    assert integer_nth_root(125, 3) == 5


def test_fourth_root():
    assert integer_nth_root(81, 4) == 3


def test_negative_cube_root():
    assert integer_nth_root(-125, 3) == -5


def test_negative_even_root():
    assert integer_nth_root(-16, 2) is None


def test_nonperfect_square():
    assert integer_nth_root(15, 2) == 4


def test_nonperfect_cube():
    assert integer_nth_root(30, 3) == 3


def test_zero_root():
    assert integer_nth_root(0, 2) == 0


def test_invalid_power():
    with pytest.raises(ValueError):
        integer_nth_root(25, 0)