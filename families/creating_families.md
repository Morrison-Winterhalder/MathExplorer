# Creating a Sequence Family

MathExplorer uses a **plugin architecture** for sequence families.

Every Python file placed inside the `families/` directory is automatically discovered and validated when the program starts. If the plugin satisfies the required interface, it immediately becomes available to the recognition engine, scoring engine, prediction engine, and report generator.

No manual registration is required.

---

# Required Metadata

Every family must define the following module-level constants.

| Name             | Purpose                                                               |
| ---------------- | --------------------------------------------------------------------- |
| `NAME`           | Human-readable name of the family.                                    |
| `DESCRIPTION`    | Short description of the sequence type.                               |
| `REPRESENTATION` | How the sequence is represented (e.g. `"Explicit"` or `"Recursive"`). |

Example:

```python
NAME = "Arithmetic"
DESCRIPTION = "Constant first differences."
REPRESENTATION = "Explicit"
```

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

# Minimal Example

```python
NAME = "Squares"
DESCRIPTION = "Perfect square numbers."
REPRESENTATION = "Explicit"


def recognize(sequence):
    return True


def fit(sequence):
    return {}


def evaluate(parameters, n):
    return n ** 2


def formula(parameters):
    return "a(n) = n²"


def complexity(parameters):
    return 2
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
