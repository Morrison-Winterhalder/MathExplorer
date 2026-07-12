# Creating a Sequence Family

MathExplorer uses a **plugin architecture** for sequence families.

Every Python file placed inside the `families/` directory is automatically discovered and validated when the program starts. If the plugin satisfies the required interface, it immediately becomes available to the recognition engine, scoring engine, prediction engine, and report generator.

No manual registration is required.

---

# Metadata

Every family must define metadata describing its mathematical identity, hierarchy, behavior, and recognition properties.

Metadata is used by the recognition engine, scoring system, reports, documentation, and future UI systems.

## Required Metadata

| Name | Purpose |
| --- | --- |
| `NAME` | Human-readable family name. |
| `DESCRIPTION` | Short description of the family. |
| `REPRESENTATION` | How the sequence is represented. |
| `CATEGORY` | Broad mathematical category. |
| `SPECIFICITY` | How specifically this family describes a sequence. |
| `PARENT` | Parent family in the hierarchy. |

Example:

```python
NAME = "Arithmetic"
DESCRIPTION = "Constant first differences."
REPRESENTATION = "Explicit"

CATEGORY = "Arithmetic"
SPECIFICITY = 20
PARENT = "Polynomial"
```

## Mathematical Metadata

| Name | Purpose |
| --- | --- |
| `OEIS` | Associated OEIS identifier if known. |
| `ALIASES` | Alternative names for the family. |
| `DOMAIN` | Mathematical domain of the sequence. |
| `GROWTH` | General growth behavior. |
| `MONOTONIC` | Whether the sequence is monotonic. |
| `BOUNDED` | Whether the sequence is bounded. |
| `OSCILLATING` | Whether the sequence oscillates. |
| `PERIODIC` | Whether the sequence is periodic. |

## Evaluation Metadata

| Name | Purpose |
| --- | --- |
| `FORMULA_TYPE` | Type of formula used. |
| `REQUIRES_PARAMETERS` | Whether fitting produces parameters. |
| `PARAMETER_NAMES` | Names of required parameters. |
| `CLOSED_FORM` | Whether a closed form exists. |
| `EVALUATION_METHOD` | How terms are generated. |

## Recognition Metadata

| Name | Purpose |
| --- | --- |
| `MIN_TERMS` | Minimum terms needed for recognition. |
| `RECOGNITION_METHOD` | Pattern used for recognition. |
| `RELIABILITY` | Confidence in the recognition method. |

---

# Required Functions

Every family plugin must implement the following functions.

## `recognize(sequence)`

Determines whether a sequence belongs to this family.

Returns:

* `True` — sequence belongs to this family.
* `False` — sequence does not belong.
* `None` — insufficient information to determine.

---

## `fit(sequence)`

Recovers the parameters that define the sequence.

Returns:

* parameter object (usually a dictionary)
* `None` if the sequence is not recognized.

---

## `evaluate(parameters, n)`

Generates the **n-th term** from the fitted parameters.

---

## `formula(parameters)`

Returns a human-readable formula for displaying in reports.

Example:

```text
a(n) = 2n + 3
```

---

## `complexity(parameters)`

Returns an integer describing the structural complexity of the family.

Typical values:

| Complexity | Meaning                               |
| ---------- | ------------------------------------- |
| `0`        | Constant                              |
| `1`        | Linear / Arithmetic / Geometric       |
| `2`        | Recursive families, figurate numbers  |
| `3+`       | Higher-order or more complex families |

Complexity is used only to break ties between equally accurate recognitions.

---

## `explain(parameters)`

Returns a list of human-readable explanations describing why the family was recognized.

Example:

```python
[
    "The sequence has constant first differences.",
    "The common difference is 3."
]
```

----

# Minimal Example

```python
NAME = "Arithmetic"
DESCRIPTION = "Constant first differences."
REPRESENTATION = "Explicit"

CATEGORY = "Arithmetic"
SPECIFICITY = 20
PARENT = "Polynomial"

DOMAIN = "Integers"
GROWTH = "Linear"

MONOTONIC = None
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

When a new file is added to the `families/` directory, MathExplorer will automatically:

* discover the module
* validate the required metadata
* validate the required functions
* load the family
* include it in recognition
* include it in scoring
* include it in prediction
* include it in reporting

No additional configuration or registration is necessary.

---

# Validation

At startup, the registry verifies that every family plugin defines:

* `NAME`
* `DESCRIPTION`
* `REPRESENTATION`
* `recognize`
* `fit`
* `evaluate`
* `formula`
* `complexity`

If any required attribute is missing, MathExplorer raises an informative `ImportError` identifying the missing components.

---

# Testing Requirements

Every new family should include tests covering:

* Recognition
* Parameter recovery
* Formula recovery
* Prediction
* Scoring behavior
* Formatting output

Run the full suite with:

```bash
pytest
```

---

# Common Mistakes

## Incorrect indexing

MathExplorer sequences use n starting at 1 unless the family explicitly defines another convention.

## Missing metadata

Every family must define required metadata before it can load.

## Duplicate names

`NAME` values must be unique because they are used by the registry.

## Incorrect formulas

The formula function should return a display-ready mathematical representation and should use the shared formatter when appropriate.

## Incorrect parent relationships

`PARENT` must refer to an existing family or be `None`.