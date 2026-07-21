import pytest

from families.core import fibonacci
from families.core import lucas
from families.core import pell
from families.core import jacobsthal
from families.core import tribonacci
from families.core import tetranacci
from families.core import padovan
from families.core import perrin


FAMILIES = [
    fibonacci,
    lucas,
    pell,
    jacobsthal,
    tribonacci,
    tetranacci,
    padovan,
    perrin,
]


KNOWN_SEQUENCES = {
    "Fibonacci": [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    ],

    "Lucas Numbers": [
        2, 1, 3, 4, 7, 11, 18, 29, 47, 76
    ],

    "Pell Numbers": [
        0, 1, 2, 5, 12, 29, 70, 169, 408, 985
    ],

    "Jacobsthal Numbers": [
        0, 1, 1, 3, 5, 11, 21, 43, 85, 171
    ],

    "Tribonacci Numbers": [
        0, 0, 1, 1, 2, 4, 7, 13, 24, 44
    ],

    "Tetranacci Numbers": [
        0, 0, 0, 1, 1, 2, 4, 8, 15, 29
    ],

    "Padovan Numbers": [
        1, 1, 1, 2, 2, 3, 4, 5, 7, 9
    ],

    "Perrin Numbers": [
        3, 0, 2, 3, 2, 5, 5, 7, 10, 12
    ],
}


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_family_has_correct_parent(family):

    assert family.PARENT == "Linear Recurrence"


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_family_is_recursive(family):

    assert family.REPRESENTATION == "Recursive"


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_family_is_natural(family):

    assert family.NATURAL_FAMILY is True


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_family_fits_known_sequence(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    parameters = family.fit(sequence)

    assert parameters is not None


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_family_reproduces_known_sequence(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    parameters = family.fit(sequence)

    assert parameters is not None

    reproduced = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 1)
    ]

    assert reproduced == sequence


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_family_generates_future_terms(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    parameters = family.fit(sequence)

    assert parameters is not None

    next_terms = [
        family.evaluate(parameters, n)
        for n in range(
            len(sequence) + 1,
            len(sequence) + 4,
        )
    ]

    assert len(next_terms) == 3


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_predictions_are_deterministic(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    parameters = family.fit(sequence)

    assert parameters is not None

    first_prediction = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 4)
    ]

    second_prediction = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 4)
    ]

    assert first_prediction == second_prediction


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_sequences_are_non_negative(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    assert all(
        value >= 0
        for value in sequence
    )


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_monotonicity_matches_metadata(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    is_non_decreasing = all(
        sequence[i] >= sequence[i - 1]
        for i in range(1, len(sequence))
    )

    assert family.MONOTONIC == is_non_decreasing


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_has_recurrence_parameters(family):

    sequence = KNOWN_SEQUENCES[family.NAME]

    parameters = family.fit(sequence)

    assert parameters is not None

    assert "Seeds" in parameters
    assert "RecurrenceCoefficients" in parameters


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_formula_exists(family):

    assert family.formula(None) is not None


@pytest.mark.parametrize(
    "family",
    FAMILIES,
)
def test_linear_recurrence_explanation_exists(family):

    explanation = family.explain(None)

    assert explanation is not None
    assert len(explanation) > 0