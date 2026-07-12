# MathExplorer

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Version](https://img.shields.io/badge/version-v2.5-green)
![Tests](https://img.shields.io/badge/tests-165_passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

MathExplorer is a Python framework for recognizing, verifying, predicting, and explaining mathematical sequences.

Given a sequence of numbers, MathExplorer identifies the most likely generating family, recovers its parameters, verifies the result, predicts future terms, and produces structured analysis reports containing mathematical and architectural metadata.

Current Release: **v2.5**

---

## What's New in v2.5

MathExplorer v2.5 expands the internal family architecture and introduces a metadata-driven sequence recognition system.

Highlights include:

* Expanded mathematical metadata for every sequence family.
* Family hierarchy support through parent-child relationships.
* Improved formula formatting and mathematical notation.
* Enhanced exponent and operator normalization.
* Improved modular family organization.
* Metadata integration into sequence classification reports.
* Expanded support for polynomial, figurate, power, and recursive families.
* Improved internal consistency and family validation.

This release establishes the foundation for future documentation, UI improvements, and explanation systems planned for the v3.x series.


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
* Modular sequence family architecture
* Family hierarchy organization
* Metadata-driven sequence descriptions
* Extensible plugin-style family system
* Comprehensive automated test suite

---

## Supported Sequence Families

### Elementary

* Constant
* Arithmetic
* Geometric
* Polynomial

### Power Families

* Squares
* Cubes
* Fourth Powers
* Fifth Powers

### Figurate Numbers

* Triangular
* Square
* Pentagonal
* Hexagonal
* Heptagonal
* Octagonal
* Nonagonal
* Decagonal

### Centered Figurate Numbers

* Centered Triangular
* Centered Square
* Centered Pentagonal
* Centered Hexagonal

### Recursive Families

* Fibonacci
* Lucas
* Pell
* Jacobsthal
* Tribonacci
* Tetranacci
* Padovan
* Perrin

### Other

* Factorial
* Pronic

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

## Adding a New Sequence Family

MathExplorer automatically discovers sequence families placed inside
`families/`.

Every family must define:

```python
NAME
DESCRIPTION
REPRESENTATION
CATEGORY
SPECIFICITY
PARENT

# Mathematical Metadata

DOMAIN
GROWTH
FORMULA_TYPE
RELIABILITY

# Family Interface

recognize(sequence)
fit(sequence)
evaluate(parameters, n)
formula(parameters)
complexity(parameters)
```

Once the file is added, the registry will automatically:

- discover the family
- validate its interface
- include it in recognition
- include it in scoring
- include it in prediction

Please read the `families/creating_families.md` file for more information.

No additional registration is required.

---

## Creating Extensions

MathExplorer uses automatic family discovery.

To add a new sequence family:

1. Create a new file inside `families/`
2. Implement the required family interface
3. Add the required metadata
4. Run the test suite

No manual registration is required.

---

## Recognition Pipeline

MathExplorer analyzes sequences through several stages:

1. Family recognition
2. Parameter fitting
3. Prediction generation
4. Residual calculation
5. Complexity-aware ranking
6. Classification selection
7. Formula recovery
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

* Documentation expansion
* Registry cleanup
* Additional sequence families
* UI improvements
* Explanation engine improvements
* Closed-form detection
* Symbolic simplification
* Better confidence calibration
* Expanded visualization tools
* OEIS search integration
* Export formats

---

## Goals for v3.0:

Theme:
Making mathematics explorable.

Goals:

1. Improve the user experience.
2. Explain every decision transparently.
3. Visualize mathematical relationships.
4. Make the project easy to discover.
5. Build an experience people want to share.

---

## About the Author

MathExplorer was created by **Morrison Winterhalder** as an independent software and mathematics project.

The project began as an exploration of mathematical pattern recognition and has grown into a modular framework for identifying, verifying, and predicting numerical sequences. It combines ideas from mathematics, software engineering, and algorithm design with an emphasis on clean architecture, extensibility, and reproducible testing.

Development continues with the goal of expanding the library's mathematical capabilities while maintaining a reliable, well-tested codebase.

---

## License

This project is licensed under the MIT License.

