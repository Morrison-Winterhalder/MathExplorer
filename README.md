# MathExplorer

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Version](https://img.shields.io/badge/version-v2.0-green)
![Tests](https://img.shields.io/badge/tests-83%20passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

MathExplorer is a Python library for recognizing, verifying, and predicting mathematical sequences.

Given a sequence of numbers, MathExplorer attempts to determine the most likely generating family, recover its parameters, verify the result, predict future terms, and report its findings with a confidence score.

Current Release: **v2.0**

---

## Project Philosophy

MathExplorer was created to explore a simple question:

> *If a human mathematician looked at a sequence, what would they recognize first?*

Rather than searching for *any* function that reproduces a sequence, MathExplorer attempts to identify the **simplest and most meaningful mathematical family** that explains it.

To accomplish this, the library combines parameter recovery, verification, complexity-aware ranking, and confidence estimation into a single recognition pipeline. This allows well-known sequence families such as triangular numbers or the Fibonacci sequence to be preferred over more general interpolating functions when both fit perfectly.

The long-term goal of MathExplorer is to become a modular framework for mathematical sequence analysis that is both educational and extensible, making it easy to add new sequence families while maintaining a consistent recognition engine.

---

## Features

* Automatic sequence recognition
* Parameter recovery
* Formula generation
* Verification against the original sequence
* Prediction of future terms
* Confidence scoring
* Complexity-aware family ranking
* Human-readable reports
* Comprehensive automated test suite

---

## Supported Sequence Families

### Elementary

* Constant
* Arithmetic
* Geometric
* Polynomial

### Figurate

* Triangular
* Pentagonal

### Recursive

* Fibonacci
* Lucas
* Pell
* Jacobsthal

### Other

* Factorial

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<username>/MathExplorer.git
cd MathExplorer
```

Install any required dependencies:

```bash
pip install -r requirements.txt
```

---

## Quick Example

```python
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.display import print_report

sequence = [1, 3, 5, 7, 9]

report = analyze_sequence(sequence)

print_report(report)
```

Example output:

```
Sequence Classification
-----------------------
Family          : Arithmetic
Formula         : a(n) = 2n - 1
Confidence      : 49.4% (Low)

Predictions
-----------
Next Terms      : [11, 13, 15, 17, 19]
```

---

## Recognition Pipeline

MathExplorer analyzes sequences using several stages:

1. Family fitting
2. Parameter recovery
3. Error scoring
4. Complexity-aware ranking
5. Confidence estimation
6. Verification
7. Prediction
8. Report generation

Each supported family implements a common interface consisting of:

* fit()
* evaluate()
* complexity()
* formula()

allowing new sequence families to be added with minimal changes to the recognition engine.

---

## Testing

MathExplorer includes a comprehensive automated test suite.

Run all tests with:

```bash
pytest
```

Current test suite:

* Family tests
* Recovery tests
* Prediction tests
* Confidence tests
* Scoring tests
* Verification tests

---

## Project Structure

```
MathExplorer/
│
├── analyzers/
├── families/
├── tests/
├── main.py
└── README.md
```

---

## Roadmap

Planned future work includes:

* Additional recursive sequence families
* Closed-form detection
* Symbolic simplification
* Better confidence calibration
* Expanded prediction capabilities
* Visualization tools
* OEIS integration
* Export formats

---

## About the Author

MathExplorer was created by **Morrison Winterhalder** as an independent software and mathematics project.

The project began as an exploration of mathematical pattern recognition and has grown into a modular framework for identifying, verifying, and predicting numerical sequences. It combines ideas from mathematics, software engineering, and algorithm design with an emphasis on clean architecture, extensibility, and reproducible testing.

Development continues with the goal of expanding the library's mathematical capabilities while maintaining a reliable, well-tested codebase.

---

## License

This project is licensed under the MIT License.

