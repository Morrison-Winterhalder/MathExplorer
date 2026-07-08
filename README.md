# MathExplorer

MathExplorer is an extensible mathematical sequence analysis engine designed to identify, reconstruct, verify, and predict numerical sequences through modular algorithms, implemented as a python library.

Given a sequence of numbers, MathExplorer identifies its family, recovers its formula when possible, verifies the reconstruction, and predicts future terms.

---

## Features

- Automatic sequence classification
- Formula recovery
- Sequence verification
- Future term prediction
- Confidence scoring
- Modular architecture
- Automated regression tests

---

## Supported Sequence Families

### Algebraic
- Constant
- Arithmetic
- Geometric
- Polynomial

### Figurate Numbers
- Triangular
- Pentagonal

### Linear Recurrences
- Fibonacci
- Lucas
- Pell
- Jacobsthal

### Growth
- Factorial

---

## Example

Input:

```python
sequence = [1, 3, 6, 10, 15, 21]
```

Output:

```
Type: Triangular
Formula: a(n) = n(n+1)/2
Verified: Yes
Next Terms: [28, 36, 45, 55, 66]
```

---

## Project Structure

```
MathExplorer/
│
├── analyzers/
│   ├── core/
│   ├── pipeline/
│   └── families/
│
├── tests/
├── reports/
├── conjectures/
└── main.py
```

---

## Running Tests

Run the complete regression suite:

```bash
python -m tests.run_tests
```

Current test coverage includes:

- Classification
- Formula Recovery
- Verification
- Prediction

---

## Current Version

Version: **1.5**

MathExplorer currently supports eleven mathematical sequence families and is built around a modular pipeline architecture designed for future expansion.

---

## Planned Features (v2.0)

- Additional sequence families
- Composite sequence recognition
- OEIS-style similarity search
- Improved confidence heuristics
- Symbolic recurrence discovery
- Plugin system for custom families

---

## Author

Morrison Winterhalder

Built as an exploration of mathematics, algorithms, and sequence recognition.
