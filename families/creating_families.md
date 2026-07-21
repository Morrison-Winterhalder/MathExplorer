# Creating a Sequence Family

MathExplorer uses a **plugin architecture** for mathematical sequence families.

Every Python family module placed inside the `families/` directory is automatically discovered and validated when the program starts. If the module satisfies the required family contract, it becomes available to the recognition engine, scoring system, prediction system, verification system, explanation system, and report generator.

No manual registration is required.

---

# Family Architecture

A sequence family is responsible for defining its own mathematical behavior.

The core engine does not need to know how a family works internally. Instead, it interacts with every family through a common interface.

The general family lifecycle is:

```text
Family Module
    |
    v
Registry Discovery
    |
    v
Contract Validation
    |
    v
Hierarchy Validation
    |
    v
Recognition
    |
    v
Parameter Fitting
    |
    v
Evaluation
    |
    v
Prediction
    |
    v
Verification
    |
    v
Scoring
    |
    v
Classification
    |
    v
Explanation
```

This allows new mathematical families to be added without modifying the central recognition engine.

---

# Metadata

Every family must define metadata describing its mathematical identity, hierarchy, behavior, evaluation method, and recognition properties.

Metadata is used by:

* The family registry.
* The recognition engine.
* The scoring system.
* Classification reports.
* The explanation system.
* Automated validation.
* Documentation.
* Future visualization and UI systems.

---

# Required Metadata

| Name             | Purpose                                                           |
| ---------------- | ----------------------------------------------------------------- |
| `NAME`           | Unique human-readable family name.                                |
| `DESCRIPTION`    | Short description of the family.                                  |
| `REPRESENTATION` | How the sequence is mathematically represented.                   |
| `CATEGORY`       | Mathematical category of the family.                              |
| `SPECIFICITY`    | How specifically the family describes a sequence.                 |
| `PARENT`         | Parent family or hierarchy category.                              |
| `NATURAL_FAMILY` | Whether the module represents a recognizable mathematical family. |

Example:

```python
NAME = "Arithmetic Numbers"
DESCRIPTION = "Sequences with constant first differences."
REPRESENTATION = "Explicit"

CATEGORY = "Basic"
SPECIFICITY = 20
PARENT = "Polynomial"
NATURAL_FAMILY = True
```

The `PARENT` field connects the family to MathExplorer's hierarchical taxonomy.

---

# Mathematical Metadata

| Name          | Purpose                                 |
| ------------- | --------------------------------------- |
| `OEIS`        | Associated OEIS identifier, if known.   |
| `ALIASES`     | Alternative names for the family.       |
| `DOMAIN`      | Mathematical domain of the sequence.    |
| `GROWTH`      | General growth behavior.                |
| `MONOTONIC`   | Whether the sequence is non-decreasing. |
| `BOUNDED`     | Whether the sequence is bounded.        |
| `OSCILLATING` | Whether the sequence oscillates.        |
| `PERIODIC`    | Whether the sequence is periodic.       |

Example:

```python
DOMAIN = "Integers"
GROWTH = "Quadratic"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False
```

These properties should describe the actual mathematical behavior of the family.

For example, a sequence beginning with:

```text
[2, 1, 3, 4, 7, 11, ...]
```

should not be marked as non-decreasing because the first transition decreases from `2` to `1`.

Family metadata is validated through automated tests.

---

# Structural Metadata

Families may also define structural metadata describing how the sequence is constructed.

Example:

```python
TRAITS = {
    "construction": "linear_recurrence",
    "order": 2,
    "growth": "exponential",
}
```

Traits may describe concepts such as:

* Construction method.
* Recurrence order.
* Polygon side count.
* Growth type.
* Digit-based construction.
* Factorial construction.
* Self-reference.
* Combinatorial structure.

Tags may also be used to describe broader mathematical relationships:

```python
TAGS = (
    "Recursive",
    "Recurrence",
)
```

This metadata provides additional context for classification, explanation, documentation, and future exploration tools.

---

# Related Families

Families may define related mathematical families:

```python
RELATED = [
    "Fibonacci Numbers",
    "Lucas Numbers",
]
```

Related families are useful for:

* Mathematical navigation.
* Documentation.
* Explanation.
* Future visualization.
* Family exploration interfaces.

Related families do not determine recognition behavior.

---

# Evaluation Metadata

| Name                  | Purpose                                              |
| --------------------- | ---------------------------------------------------- |
| `FORMULA_TYPE`        | Type of mathematical representation.                 |
| `REQUIRES_PARAMETERS` | Whether fitting produces parameters.                 |
| `PARAMETER_NAMES`     | Names of required parameters.                        |
| `CLOSED_FORM`         | Whether the family has a closed-form representation. |
| `EVALUATION_METHOD`   | How terms are generated.                             |

Example:

```python
FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = True

PARAMETER_NAMES = (
    "Difference",
    "Intercept",
)

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"
```

Recursive families may instead use:

```python
CLOSED_FORM = True
EVALUATION_METHOD = "Recurrence"
```

or:

```python
CLOSED_FORM = False
EVALUATION_METHOD = "Recursive Generation"
```

The metadata should accurately describe how the family is implemented.

---

# Recognition Metadata

| Name                 | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| `MIN_TERMS`          | Minimum number of terms needed for reliable recognition. |
| `RECOGNITION_METHOD` | Mathematical method used for recognition.                |
| `RELIABILITY`        | Reliability classification of the recognition method.    |

Example:

```python
MIN_TERMS = 3
RECOGNITION_METHOD = "Constant First Differences"
RELIABILITY = "Exact"
```

Recognition metadata describes the method used by the family rather than the confidence of a particular classification.

---

# Required Functions

Every family plugin must implement the following functions.

---

## `recognize(sequence)`

Determines whether a sequence belongs to the family.

Returns:

* `True` — the sequence is recognized.
* `False` — the sequence is definitively rejected.
* `None` — there is insufficient information to determine recognition.

Example:

```python
def recognize(sequence):
    if len(sequence) < 3:
        return None

    ...
```

Families should avoid accepting sequences that merely resemble their pattern.

Recognition should be based on the mathematical definition of the family.

---

## `fit(sequence)`

Recovers the parameters that define the sequence.

Returns:

* A parameter object, usually a dictionary.
* `None` if the sequence is not recognized.

Example:

```python
def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Difference": 3,
        "Intercept": 1,
    }
```

A family with no parameters may return:

```python
return {}
```

---

## `evaluate(parameters, n)`

Generates the n-th term of the sequence.

MathExplorer generally uses one-based mathematical indexing:

```text
n = 1
```

represents the first term unless the family explicitly defines another convention.

Example:

```python
def evaluate(parameters, n):
    return 2 * n + 1
```

The evaluation function must be consistent with the parameters returned by `fit()`.

---

## `formula(parameters)`

Returns a human-readable mathematical representation for reports and explanations.

Example:

```python
def formula(parameters):
    return format_formula("2n + 1")
```

The formula should be display-ready and should use shared formatting utilities whenever appropriate.

---

## `complexity(parameters)`

Returns an integer describing the structural complexity of the family.

Typical values include:

| Complexity | Meaning                                                                         |
| ---------- | ------------------------------------------------------------------------------- |
| `0`        | Constant or extremely simple structure.                                         |
| `1`        | Basic arithmetic or geometric structure.                                        |
| `2`        | Polynomial, figurate, or simple recurrence structure.                           |
| `3+`       | Higher-order, iterative, self-referential, or otherwise more complex structure. |

Complexity contributes to the ranking of competing candidate families.

It should not be used as the sole basis for recognition.

---

## `explain(parameters)`

Returns a list of human-readable explanations describing why the family was recognized.

Example:

```python
def explain(parameters):
    return [
        "The sequence has constant first differences.",
        "The common difference is 3.",
    ]
```

Explanations should describe actual mathematical evidence rather than simply repeating the family name.

---

# Minimal Example

```python
NAME = "Arithmetic Numbers"
DESCRIPTION = "Sequences with constant first differences."
REPRESENTATION = "Explicit"

CATEGORY = "Basic"
SPECIFICITY = 20
PARENT = "Polynomial"
NATURAL_FAMILY = True

DOMAIN = "Integers"
GROWTH = "Linear"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = True

PARAMETER_NAMES = (
    "Difference",
    "Intercept",
)

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

MIN_TERMS = 3
RECOGNITION_METHOD = "Constant First Differences"
RELIABILITY = "Exact"


def recognize(sequence):
    ...


def fit(sequence):
    ...


def evaluate(parameters, n):
    ...


def formula(parameters):
    ...


def complexity(parameters):
    return 1


def explain(parameters):
    return [
        "The sequence has constant first differences."
    ]
```

---

# Automatic Discovery

When a new family file is added to the `families/` directory, MathExplorer automatically:

* Discovers the module.
* Validates the family contract.
* Validates required metadata.
* Validates hierarchy relationships.
* Loads the family.
* Makes it available to recognition.
* Makes it available to scoring.
* Makes it available to prediction.
* Makes it available to verification.
* Makes it available to explanation.
* Makes it available to reporting.

No additional configuration or manual registration is required.

---

# Family Hierarchy

The `PARENT` field places a family within MathExplorer's mathematical taxonomy.

Example:

```python
NAME = "Centered Square Numbers"
PARENT = "Centered Polygonal"
```

The registry validates that the parent relationship is valid.

Parent relationships are used to:

* Organize related mathematical families.
* Build family trees.
* Support hierarchical explanations.
* Enable family browsing.
* Provide future metadata inheritance.
* Improve developer understanding of mathematical relationships.

A family may be a recognizable sequence family or a structural hierarchy category.

---

# Validation

At startup, the registry validates every discovered family.

Validation includes:

## Required Interface

The family must define:

```text
NAME
DESCRIPTION
REPRESENTATION
recognize
fit
evaluate
formula
complexity
```

## Required Metadata

The family must define the metadata required by the family contract.

## Unique Names

Every family `NAME` must be unique.

## Hierarchy Validity

Every declared `PARENT` must refer to a valid family or hierarchy category.

## Mathematical Consistency

Family behavior should remain consistent with its declared metadata.

For example:

```python
MONOTONIC = True
```

should correspond to a non-decreasing known sequence.

If a family violates the required contract, the registry raises an informative error identifying the invalid or missing components.

---

# Testing Requirements

Every new family should include tests appropriate to its mathematical structure.

At minimum, tests should cover:

* Recognition.
* Rejection.
* Parameter recovery.
* Evaluation.
* Formula generation.
* Prediction.
* Determinism.
* Metadata consistency.
* Integration with the registry.

Specialized families may additionally require tests for:

* Monotonicity.
* Boundedness.
* Oscillation.
* Periodicity.
* Recurrence behavior.
* Figurate structure.
* Combinatorial properties.
* Special transformations.

Example:

```python
def test_square_recognition():
    assert recognize([1, 4, 9, 16]) is True
```

A new family should also be included in the appropriate family-level and integration-level test suites.

---

# Common Mistakes

## Incorrect Indexing

MathExplorer generally uses one-based sequence indexing.

If the mathematical definition begins with a different convention, the family must implement that convention consistently across:

* `recognize()`
* `fit()`
* `evaluate()`
* `formula()`
* Tests

---

## Missing Metadata

A family cannot be considered complete without the metadata required by the family contract.

Metadata should accurately describe the family rather than simply satisfying the interface.

---

## Duplicate Names

`NAME` values must be unique because the registry uses them for:

* Family lookup.
* Classification.
* Hierarchy relationships.
* Reports.

---

## Incorrect Formulas

The `formula()` function should return a display-ready mathematical representation.

Use shared formatting utilities when appropriate.

For example:

```python
return format_formula("n^2")
```

rather than manually duplicating formatting logic.

---

## Incorrect Parent Relationships

`PARENT` must refer to a valid family or hierarchy category.

For example:

```python
PARENT = "Linear Recurrence"
```

requires `"Linear Recurrence"` to be a valid hierarchy node.

Incorrect parent relationships can prevent the registry from constructing a valid hierarchy.

---

## Inconsistent Metadata

Metadata should describe the actual family behavior.

For example, do not declare:

```python
MONOTONIC = True
```

if the known sequence begins:

```text
[2, 1, 3, 4, ...]
```

because the sequence decreases from its first term to its second term.

The automated test suite is designed to detect these inconsistencies.

---

# Before Submitting a New Family

Before considering a new family complete:

1. Create the family module.
2. Implement the required metadata.
3. Implement the required functions.
4. Set the correct hierarchy parent.
5. Add the family to appropriate tests.
6. Run targeted tests.
7. Run the full test suite.

Run the complete test suite with:

```bash
pytest
```

The full test suite should pass before the new family is considered complete.
