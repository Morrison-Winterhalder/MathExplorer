import pytest

from families.core.factorial import (
    NAME,
    recognize,
    fit,
    evaluate,
)


FACTORIAL_SEQUENCE = [
    1,
    2,
    6,
    24,
    120,
    720,
]


def test_factorials_family_fits_known_sequence():

    assert recognize(
        FACTORIAL_SEQUENCE
    ) is True

    assert fit(
        FACTORIAL_SEQUENCE
    ) is not None


def test_factorials_family_reproduces_known_sequence():

    parameters = fit(
        FACTORIAL_SEQUENCE
    )

    reproduced = [

        evaluate(
            parameters,
            n
        )

        for n in range(
            1,
            len(FACTORIAL_SEQUENCE) + 1
        )

    ]

    assert reproduced == FACTORIAL_SEQUENCE


def test_factorials_family_generates_future_terms():

    parameters = fit(
        FACTORIAL_SEQUENCE
    )

    future_terms = [

        evaluate(
            parameters,
            n
        )

        for n in range(
            len(FACTORIAL_SEQUENCE) + 1,
            len(FACTORIAL_SEQUENCE) + 4
        )

    ]

    assert future_terms == [
        5040,
        40320,
        362880,
    ]


def test_factorial_predictions_are_deterministic():

    parameters = fit(
        FACTORIAL_SEQUENCE
    )

    first = [

        evaluate(
            parameters,
            n
        )

        for n in range(
            1,
            10
        )

    ]

    second = [

        evaluate(
            parameters,
            n
        )

        for n in range(
            1,
            10
        )

    ]

    assert first == second


def test_factorial_sequence_is_positive():

    parameters = fit(
        FACTORIAL_SEQUENCE
    )

    generated = [

        evaluate(
            parameters,
            n
        )

        for n in range(
            1,
            10
        )

    ]

    assert all(
        value > 0
        for value in generated
    )


def test_factorial_sequence_is_strictly_increasing():

    parameters = fit(
        FACTORIAL_SEQUENCE
    )

    generated = [

        evaluate(
            parameters,
            n
        )

        for n in range(
            1,
            10
        )

    ]

    assert all(
        later > earlier

        for earlier, later

        in zip(
            generated,
            generated[1:]
        )

    )


def test_factorial_family_rejects_non_factorial_sequence():

    sequence = [
        1,
        2,
        6,
        25,
        120,
    ]

    assert recognize(
        sequence
    ) is False

    assert fit(
        sequence
    ) is None


def test_factorial_family_rejects_empty_sequence():

    assert recognize(
        []
    ) is None


def test_factorial_family_requires_minimum_sequence_length():

    short_sequence = [
        1,
        2,
        6,
    ]

    assert recognize(
        short_sequence
    ) is True


def test_factorial_family_name_is_correct():

    assert NAME == "Factorials"