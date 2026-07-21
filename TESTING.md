# MathExplorer Testing Guide

This document describes the testing architecture used by MathExplorer and explains how sequence families, analysis pipelines, registries, metadata, confidence systems, and internal infrastructure are validated.

MathExplorer uses a comprehensive automated test suite to ensure that mathematical recognition remains correct while the architecture continues to expand.

The test suite currently contains:

**2,069 tests**

with:

* **2,031 passing tests**
* **38 skipped tests**

The complete suite currently executes in approximately two seconds.

---

# Running Tests

Run the complete test suite with:

```bash
pytest
```

A successful development change should leave the entire test suite passing unless a skipped test is intentionally excluded.

The full suite should be run before major changes are considered complete.

---

# Testing Philosophy

MathExplorer testing is built around several principles.

## Correct Recognition

A family should correctly recognize sequences that belong to it while rejecting unrelated sequences.

## Accurate Mathematical Behavior

Families must correctly:

* Fit recognized sequences.
* Generate their own terms.
* Recover formulas or recurrence descriptions.
* Predict future terms.
* Preserve mathematical properties declared in metadata.

## Stable Architecture

Changes to shared infrastructure should not break existing families or pipeline behavior.

## Regression Protection

Previously solved architectural problems should remain solved as the project evolves.

## Contract Consistency

Every sequence family must satisfy the common family interface and metadata contract.

---

# Test Organization

Tests are organized by responsibility.

```text
tests/
│
├── families/
│   ├── test_basic_families.py
│   ├── test_combinatorial_families.py
│   ├── test_family_contract.py
│   ├── test_family_fit_evaluate_consistency.py
│   ├── test_family_metadata.py
│   ├── test_family_predictions.py
│   ├── test_family_rejection.py
│   ├── test_figurate_families.py
│   ├── test_linear_recurrence_families.py
│   └── test_special_families.py
│
├── integration/
│   ├── test_basic_families.py
│   ├── test_conf.py
│   ├── test_failure_cases.py
│   ├── test_recursive_families.py
│   └── test_special_families.py
│
├── pipeline/
│   ├── test_classify.py
│   ├── test_confidence.py
│   ├── test_explain.py
│   ├── test_prediction.py
│   └── test_verification.py
│
├── registry/
│   ├── test_hierarchy.py
│   ├── test_loading.py
│   ├── test_lookup.py
│   └── test_metadata.py
│
├── regression/
│   ├── test_regression_confidence.py
│   ├── test_regression_explanation.py
│   ├── test_regression_hierarchy.py
│   ├── test_regression_pipeline.py
│   └── test_regression_recognition.py
│
└── unit/
    ├── confidence/
    │   ├── test_builder.py
    │   ├── test_evidence.py
    │   ├── test_factors.py
    │   ├── test_formatter.py
    │   └── test_scorer.py
    │
    ├── test_formatter.py
    ├── test_hierarchy.py
    ├── test_properties.py
    ├── test_recovery.py
    ├── test_scoring.py
    ├── test_statistics.py
    ├── test_trace.py
    ├── test_transformations.py
    └── test_utilities.py
```

---

# Family Tests

Family tests verify the mathematical behavior of individual sequence families.

Family tests are divided into specialized groups based on the mathematical structure of the families.

Examples include:

* Basic families
* Combinatorial families
* Figurate families
* Linear recurrence families
* Special families

Family tests verify properties such as:

* Recognition behavior
* Rejection behavior
* Parameter fitting
* Evaluation correctness
* Formula generation
* Prediction correctness
* Deterministic behavior
* Complexity behavior
* Mathematical metadata consistency

For example, a family test may verify:

```python
def test_square_recognition():
    assert recognize([1, 4, 9, 16]) is True
```

A family may also be tested against its mathematical properties:

```python
def test_sequence_is_non_decreasing():
    assert all(
        sequence[i] >= sequence[i - 1]
        for i in range(1, len(sequence))
    )
```

This allows the test suite to validate not only whether a family recognizes a sequence, but whether its implementation actually behaves consistently with its declared mathematical properties.

---

# Family Contract Tests

Every family must satisfy the common family contract.

Contract tests verify that family modules provide the required interface and metadata.

This includes:

* Required constants
* Required metadata
* Required functions
* Valid return behavior
* Compatible function signatures

A family must correctly implement the common interface used by the registry and analysis pipeline.

This prevents individual family implementations from silently diverging from the architecture.

---

# Fit and Evaluation Consistency Tests

These tests verify that a family can reproduce the sequence it recognizes.

The general relationship is:

```text
Sequence
    |
    v
recognize()
    |
    v
fit()
    |
    v
evaluate()
    |
    v
Original Terms
```

A recognized sequence should produce parameters that allow `evaluate()` to reproduce the original terms.

This protects against situations where:

* Recognition succeeds but fitting fails.
* Fitting succeeds but evaluation generates different terms.
* Prediction behavior differs from the original family definition.

---

# Family Prediction Tests

Prediction tests verify that recognized families can generate future terms correctly.

For example:

```text
Input:

[1, 3, 5, 7, 9]

Prediction:

[11, 13, 15, 17, 19]
```

Tests verify:

* Correct future terms.
* Deterministic predictions.
* Correct parameter usage.
* Compatibility between fitting and evaluation.

A family should not produce different predictions for the same sequence and parameters.

---

# Family Rejection Tests

Recognition must also correctly reject unrelated sequences.

These tests verify that families do not over-recognize arbitrary data.

For example, a family should not accept a sequence merely because:

* It has a similar growth pattern.
* It shares a few initial terms.
* It can be approximated by the same broad mathematical category.

This is especially important for highly specific families such as:

* Fibonacci
* Factorial
* Figurate families
* Special recursive processes
* Linear recurrence families

---

# Mathematical Property Tests

Family metadata declares mathematical properties such as:

* Monotonicity
* Boundedness
* Oscillation
* Periodicity
* Growth behavior

The test suite validates these properties against known sequences.

For example, if a family declares:

```python
MONOTONIC = True
```

the known sequence used by its tests must actually be non-decreasing.

This allows the test suite to catch metadata errors such as incorrectly labeling the Lucas sequence as monotonic when its initial terms are:

```text
[2, 1, 3, 4, 7, 11, ...]
```

The first decrease from `2` to `1` means the sequence is not non-decreasing.

---

# Integration Tests

Integration tests verify that families work correctly inside the full MathExplorer system.

These tests connect individual components together and verify complete workflows.

Examples include:

* Family recognition through the full analysis pipeline.
* Confidence calculation.
* Classification.
* Prediction.
* Verification.
* Explanation.
* Failure handling.

A family may work correctly in isolation but still fail when integrated with:

* The registry.
* The scoring system.
* The confidence system.
* The explanation engine.
* The prediction pipeline.

Integration tests protect against these failures.

---

# Pipeline Tests

Pipeline tests verify the major analysis stages.

These include:

## Classification

Tests verify that the correct family is selected from competing candidates.

## Confidence

Tests verify that confidence values and confidence factors behave correctly.

## Explanation

Tests verify that the system produces meaningful explanations for classification decisions.

## Prediction

Tests verify that the selected family produces future terms correctly.

## Verification

Tests verify that generated terms match the original sequence.

The pipeline is tested as a connected system rather than as a collection of unrelated functions.

---

# Registry Tests

Registry tests ensure that the family plugin system remains valid.

They verify:

* Family discovery.
* Family loading.
* Family name uniqueness.
* Required metadata.
* Required interfaces.
* Family lookup.
* Hierarchy relationships.

The registry also validates the family hierarchy.

For example:

```python
NAME = "Centered Square Numbers"
PARENT = "Centered Polygonal"
```

requires the corresponding parent family or hierarchy category to exist.

Invalid hierarchy relationships should be rejected rather than silently accepted.

Adding a new family should not require manually modifying registry code.

---

# Hierarchy Tests

Hierarchy tests verify the mathematical taxonomy used by MathExplorer.

They test:

* Parent-child relationships.
* Valid hierarchy construction.
* Family placement.
* Hierarchy lookup.
* Registry compatibility.
* Regression protection for previously established relationships.

The hierarchy is treated as part of the architecture rather than as informal documentation.

---

# Metadata Tests

Metadata tests verify that sequence family metadata remains internally consistent.

Metadata may describe:

* Category
* Parent
* Growth
* Domain
* Representation
* Formula type
* Recognition method
* Reliability
* Specificity
* Mathematical traits

The test suite ensures that this metadata is present and compatible with the family implementation.

---

# Scoring Tests

Scoring tests verify that MathExplorer chooses meaningful mathematical families when multiple families can describe a sequence.

The scoring system considers factors including:

* Fit quality
* Residual error
* Complexity
* Family competition
* Family specificity
* Sample size

For example, a square sequence should prefer:

```text
Square Numbers
```

over:

```text
Polynomial
```

when both describe the observed terms correctly.

The purpose of scoring is not merely to find a mathematically valid explanation.

It is to select the most meaningful explanation available.

---

# Confidence Tests

Confidence tests validate the confidence system.

They cover:

* Confidence factors.
* Fit quality.
* Competition between candidate families.
* Sample size.
* Complexity.
* Confidence scoring.
* Confidence formatting.
* Evidence construction.

Confidence is treated as structured evidence rather than as an arbitrary number.

---

# Regression Tests

Regression tests protect previously solved bugs and architectural behavior.

They verify that changes to the codebase do not reintroduce earlier failures.

Regression tests cover areas including:

* Confidence behavior.
* Explanation behavior.
* Hierarchy behavior.
* Pipeline behavior.
* Recognition behavior.

Whenever a significant bug is discovered and fixed, a regression test can preserve that fix permanently.

---

# Unit Tests

Unit tests validate individual pieces of internal infrastructure.

They cover systems including:

* Formatting
* Hierarchy logic
* Mathematical properties
* Formula recovery
* Scoring
* Statistics
* Analysis traces
* Transformations
* Utility functions

The confidence subsystem also has its own dedicated unit tests for:

* Evidence
* Factors
* Scoring
* Building
* Formatting

---

# Trace Tests

MathExplorer contains an internal analysis trace system.

Trace tests verify that internal analysis events are recorded correctly.

These tests help ensure that the system can preserve a structured record of the analysis process without breaking the main pipeline.

The trace system supports internal analysis observability and developer-oriented debugging.

---

# Formatting Tests

Formatting tests verify that mathematical output remains consistent.

They cover:

* Exponents
* Operators
* Parentheses
* Recursive notation
* Formula normalization
* Recurrence formatting

Examples:

```text
n^2
```

should become:

```text
n²
```

and:

```text
2 * 3^(n-1)
```

should become:

```text
2·3⁽ⁿ⁻¹⁾
```

Formatting tests ensure that mathematical output remains consistent across families and reports.

---

# Adding Tests for a New Family

Every new sequence family should include tests for the properties relevant to its mathematical structure.

At minimum, test:

## Recognition

Verify valid and invalid sequences.

## Fitting

Verify that valid sequences produce usable fitted parameters.

## Evaluation

Verify that fitted parameters reproduce known terms.

## Prediction

Verify future terms.

## Determinism

Verify that repeated analysis produces consistent results.

## Metadata

Verify that declared metadata matches the family behavior.

## Integration

Verify that the family works through the registry and analysis pipeline.

Specialized families may also require tests for:

* Monotonicity
* Boundedness
* Oscillation
* Periodicity
* Recurrence behavior
* Figurate structure
* Combinatorial properties
* Special mathematical transformations

---

# Before Submitting Changes

Before considering a feature complete:

1. Add or update appropriate tests.

2. Run the relevant targeted tests.

For example:

```bash
pytest tests/families/test_special_families.py
```

3. Run the complete test suite.

```bash
pytest
```

4. Verify that no unexpected tests fail.

5. Confirm that new behavior is covered by regression tests when appropriate.

6. Confirm that formulas, metadata, and formatting match existing conventions.

A complete change should leave the full suite passing.

---

# Current Test Status

The current MathExplorer test suite contains:

```text
2,069 collected tests
2,031 passed
38 skipped
0 failed
```

The full test suite completes in approximately:

```text
2.12 seconds
```

This test suite provides broad coverage across:

* Mathematical families
* Family contracts
* Recognition
* Rejection
* Fitting
* Evaluation
* Prediction
* Verification
* Classification
* Confidence
* Scoring
* Explanation
* Registry behavior
* Hierarchy behavior
* Metadata
* Formatting
* Regression protection
* Internal utilities

The passing suite represents the completion of the current v3.0 architectural foundation.

---

# Future Testing Expansion

Future testing improvements may include:

* Property-based testing.
* Randomized sequence generation.
* Performance benchmarks.
* Larger regression suites.
* Automated family generation tests.
* Fuzz testing of recognition behavior.
* Mathematical invariant testing.
* Visualization testing.
* User-interface testing.

The current testing architecture is designed to support these additions without requiring major restructuring of the existing test suite.
