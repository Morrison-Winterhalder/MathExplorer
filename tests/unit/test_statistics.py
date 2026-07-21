from analyzers.core.statistics import (
    normalized_rmse,
    r_squared,
    relative_residual_norm,
)


# ==========================================================
# normalized_rmse()
# ==========================================================

def test_normalized_rmse_exact_match():
    assert normalized_rmse(
        [1, 2, 3],
        [1, 2, 3]
    ) == 0.0


def test_normalized_rmse_basic_error():
    result = normalized_rmse(
        [1, 2, 4],
        [1, 2, 3]
    )

    assert round(result, 6) == round(
        (1 / 3) ** 0.5 / 3,
        6
    )


def test_normalized_rmse_empty():
    assert normalized_rmse([], []) == 0.0


def test_normalized_rmse_length_mismatch():
    try:
        normalized_rmse(
            [1, 2],
            [1]
        )
        assert False
    except ValueError:
        assert True


def test_normalized_rmse_zero_expected():
    assert normalized_rmse(
        [3,4],
        [0,0]
    ) == (12.5 ** 0.5)


def test_normalized_rmse_zero_perfect():
    assert normalized_rmse(
        [0, 0],
        [0, 0]
    ) == 0.0


# ==========================================================
# r_squared()
# ==========================================================

def test_r_squared_perfect_fit():
    assert r_squared(
        [1, 2, 3],
        [1, 2, 3]
    ) == 1.0


def test_r_squared_imperfect_fit():
    result = r_squared(
        [1, 2, 3],
        [1, 2, 4]
    )

    assert round(result, 6) == round(
        1 - (1 / 2),
        6
    )


def test_r_squared_empty():
    assert r_squared([], []) == 1.0


def test_r_squared_length_mismatch():
    try:
        r_squared(
            [1, 2],
            [1]
        )
        assert False
    except ValueError:
        assert True


def test_r_squared_constant_perfect():
    assert r_squared(
        [5, 5, 5],
        [5, 5, 5]
    ) == 1.0


def test_r_squared_constant_bad():
    assert r_squared(
        [5, 5, 5],
        [4, 4, 4]
    ) == 0.0


def test_r_squared_negative_clamped():
    result = r_squared(
        [1, 2, 3],
        [100, 100, 100]
    )

    assert result == 0.0


# ==========================================================
# relative_residual_norm()
# ==========================================================

def test_rrn_exact_match():
    assert relative_residual_norm(
        [1, 2, 3],
        [1, 2, 3]
    ) == 0.0


def test_rrn_basic_error():
    result = relative_residual_norm(
        [1, 2, 3],
        [1, 2, 4]
    )

    assert round(result, 6) == round(
        1 / (14 ** 0.5),
        6
    )


def test_rrn_length_mismatch():
    assert relative_residual_norm(
        [1, 2],
        [1]
    ) is None


def test_rrn_zero_exact():
    assert relative_residual_norm(
        [0, 0],
        [0, 0]
    ) == 0


def test_rrn_zero_actual_error():
    assert relative_residual_norm(
        [0, 0],
        [1, 2]
    ) is None