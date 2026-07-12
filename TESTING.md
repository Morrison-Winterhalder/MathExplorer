# MathExplorer Testing Guide

This document describes the testing architecture used by MathExplorer and explains how new features and sequence families should be validated.

MathExplorer uses automated testing to ensure that sequence recognition, formula recovery, prediction, formatting, and internal architecture remain reliable as the project expands.

---

# Running Tests

Run the complete test suite with:

```bash
pytest
```

A successful development change should leave the entire test suite passing.

---

# Testing Philosophy

MathExplorer tests are designed around several principles:

## Correct Recognition

A family should correctly identify sequences that belong to it while rejecting unrelated sequences.

## Accurate Recovery

Recognized sequences should recover the correct parameters and formula.

## Reliable Prediction

Generated future terms should match the expected sequence.

## Stable Architecture

Changes to the internal system should not break existing families or analysis behavior.

---

# Test Organization

Tests are organized by responsibility.

```
tests/

├── test_families.py
├── test_registry.py
├── test_recovery.py
├── test_prediction.py
├── test_scoring.py
├── test_confidence.py
├── test_verification.py
└── test_formatter.py
```

---

# Family Tests

Family tests verify that individual sequence families behave correctly.

A family test should verify:

- Recognition behavior
- Parameter fitting
- Formula generation
- Evaluation correctness
- Complexity behavior

Example:

```python
def test_square_recognition():
    assert recognize([1, 4, 9, 16]) is True
```

---

# Recovery Tests

Recovery tests verify that MathExplorer can recover the correct mathematical formula.

Examples:

```
[1, 4, 9, 16]

Expected:

a(n) = n²
```

or:

```
[2, 6, 18, 54]

Expected:

a(n) = 2·3⁽ⁿ⁻¹⁾
```

These tests ensure that recognition leads to meaningful mathematical output.

---

# Prediction Tests

Prediction tests verify that recognized families can generate future terms.

A sequence should produce the correct continuation after analysis.

Example:

```
Input:

[1, 3, 5, 7, 9]

Prediction:

[11, 13, 15, 17, 19]
```

---

# Scoring Tests

Scoring tests verify that MathExplorer chooses meaningful families when multiple families fit a sequence.

The scoring system considers:

- Accuracy
- Residual error
- Complexity
- Family specificity

Example:

A square sequence should prefer:

```
Square Numbers
```

over:

```
Polynomial
```

when both describe the sequence correctly.

---

# Registry Tests

Registry tests ensure that the family plugin system remains valid.

They verify:

- All families are discovered.
- Family names are unique.
- Required metadata exists.
- Required functions exist.
- Family lookup works correctly.

Adding a new family should not require modifying registry code.

---

# Formatting Tests

Formatting tests verify that mathematical output remains consistent.

They cover:

- Exponents
- Operators
- Parentheses
- Recursive notation
- Formula normalization

Examples:

```
n^2
```

should become:

```
n²
```

and:

```
2 * 3^(n-1)
```

should become:

```
2·3⁽ⁿ⁻¹⁾
```

---

# Adding Tests for a New Family

Every new sequence family should include tests for:

## Recognition

Verify valid and invalid sequences.

## Recovery

Verify the correct formula is generated.

## Prediction

Verify future terms.

## Scoring

Verify the family can compete correctly against broader families.

## Formatting

Verify the displayed formula is correct.

---

# Before Submitting Changes

Before considering a feature complete:

1. Run the full test suite.

```bash
pytest
```

2. Verify no existing tests fail.

3. Add tests for new functionality.

4. Confirm formulas and formatting match existing conventions.

---

# Future Testing Expansion

Future testing improvements may include:

- Property-based testing
- Randomized sequence generation
- Performance benchmarks
- Larger regression suites
- Automated family metadata validation