# MathExplorer Development Guide

This document describes how to set up, run, test, and contribute to MathExplorer.

MathExplorer is a modular, plugin-based mathematical sequence recognition system. Development is organized around independent sequence family modules, a validated family hierarchy, automated registry discovery, and a comprehensive test suite.

---

# Development Setup

Clone the repository:

```bash
git clone https://github.com/<username>/MathExplorer.git
cd MathExplorer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running MathExplorer

Run the main program:

```bash
python main.py
```

A sequence can then be analyzed through the MathExplorer analysis pipeline.

The pipeline processes sequences through recognition, fitting, prediction, scoring, classification, explanation, verification, and reporting stages.

---

# Running Tests

Run the complete test suite:

```bash
pytest
```

The full test suite currently contains over 2,000 automated tests covering the family system, analysis pipeline, registry, hierarchy, confidence system, prediction, verification, formatting, and regression behavior.

The current verified test state is:

```text
2031 passed, 38 skipped
```

All tests should pass before changes are considered complete.

---

# Development Workflow

The recommended development workflow is:

1. Understand the relevant architecture or family hierarchy.
2. Make the required changes.
3. Add or update automated tests.
4. Run focused tests during development.
5. Run the complete test suite.
6. Verify mathematical behavior and output formatting.
7. Review metadata and hierarchy relationships.
8. Commit the changes.

For example, during family development, focused tests may be run with:

```bash
pytest tests/families/test_<family_category>.py
```

The complete suite should be run before finalizing a change:

```bash
pytest
```

---

# Adding a Sequence Family

To add a new mathematical family:

1. Determine where the family belongs in the hierarchy.
2. Create a new Python module inside the appropriate directory under:

```text
families/
```

3. Implement the required family interface.
4. Add the required mathematical metadata.
5. Define the appropriate parent family using `PARENT`.
6. Add family-specific tests.
7. Verify that the family is discovered and loaded by the registry.
8. Run the complete test suite.

For detailed family creation instructions, see:

```text
families/creating_families.md
```

---

# Family Plugin Architecture

Sequence families are implemented as independent plugins.

A family module is responsible for its own mathematical behavior, including:

* Sequence recognition
* Parameter fitting
* Term evaluation
* Formula generation
* Complexity reporting
* Explanations
* Mathematical metadata

The standard family interface includes:

```python
recognize(sequence)
fit(sequence)
evaluate(parameters, n)
formula(parameters)
complexity(parameters)
explain(parameters)
```

Not every family requires parameters, but every family must follow the conventions required by the family registry and validation system.

New family modules should not require modifications to the central recognition engine.

---

# Family Metadata

Every family should define metadata consistently with existing family modules.

Typical metadata includes:

```python
NAME
DESCRIPTION
REPRESENTATION
CATEGORY
SPECIFICITY
PARENT
NATURAL_FAMILY
```

Mathematical metadata may include:

```python
OEIS
ALIASES
CLOSED_FORM
EVALUATION_METHOD
FAMILY_TYPE
TAGS
TRAITS
RELATED
DOMAIN
GROWTH
MONOTONIC
BOUNDED
OSCILLATING
PERIODIC
FORMULA_TYPE
REQUIRES_PARAMETERS
PARAMETER_NAMES
MIN_TERMS
RECOGNITION_METHOD
RELIABILITY
```

Metadata is not merely descriptive. It is validated by the test suite and provides information used by classification, explanation, hierarchy, and future tooling.

---

# Family Hierarchy

MathExplorer organizes families using a hierarchical taxonomy.

A family may declare its parent using:

```python
PARENT = "Parent Family"
```

For example:

```python
NAME = "Fibonacci"
PARENT = "Linear Recurrence"
```

The parent must exist in the registry.

The hierarchy allows related mathematical families to be organized structurally rather than treated as unrelated plugins.

The registry validates:

* Parent existence
* Family name uniqueness
* Hierarchy relationships
* Valid family loading
* Plugin integrity

Invalid hierarchy relationships should cause validation failures rather than silently producing an incorrect taxonomy.

---

# Family Categories

The current architecture includes hierarchical categories such as:

* `Sequence Families`
* `Explicit`
* `Basic`
* `Figurate`
* `Polygonal`
* `Centered Polygonal`
* `Special`
* `Combinatorial`
* `Recursive`
* `Linear Recurrence`

Some hierarchy nodes are organizational categories rather than direct sequence recognizers.

These categories provide structure for:

* Family organization
* Registry validation
* Family browsing
* Mathematical relationships
* Classification context
* Explanation systems
* Future interface features

---

# Registry System

The family registry automatically discovers family modules.

The registry is responsible for:

1. Discovering family modules.
2. Loading available plugins.
3. Validating required interfaces.
4. Validating metadata.
5. Validating hierarchy relationships.
6. Rejecting invalid plugins.
7. Making valid families available to the analysis pipeline.

Manual registration should not be required
