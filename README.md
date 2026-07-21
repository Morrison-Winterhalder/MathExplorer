# MathExplorer

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Version](https://img.shields.io/badge/version-v3.0-green)
![Tests](https://img.shields.io/badge/tests-2031_passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

MathExplorer is a Python framework for recognizing, verifying, predicting, and explaining mathematical sequences.

Given a sequence of numbers, MathExplorer identifies the most likely generating family, recovers its parameters, verifies the result, predicts future terms, and produces structured analysis reports containing mathematical and architectural metadata.

The system is built around a modular, plugin-based family architecture with automatic family discovery, hierarchical mathematical taxonomy, complexity-aware ranking, confidence analysis, prediction, verification, and structured explanations.

**Current Release: v3.0**

---

## What's New in v3.0

MathExplorer v3.0 completes the transition to a hierarchical, metadata-driven sequence recognition architecture.

Highlights include:

* A complete hierarchical taxonomy for sequence families.
* Parent-child relationships between mathematical families.
* Automatic family discovery through the family registry.
* Registry validation for family interfaces and hierarchy relationships.
* Expanded mathematical metadata for sequence families.
* A significantly expanded sequence family library.
* Support for Basic, Combinatorial, Figurate, Special, Recursive, and Linear Recurrence family categories.
* Expanded support for polygonal and centered polygonal numbers.
* Expanded support for combinatorial sequences.
* Expanded support for recursive and self-referential sequences.
* Expanded support for linear recurrence families.
* Improved family-specific testing.
* Comprehensive integration and regression testing.
* Improved mathematical property validation.
* Expanded formula and recurrence formatting utilities.
* Improved consistency between recognition, fitting, evaluation, prediction, and metadata.
* Over 2,000 automated tests covering the complete system.

The v3.0 architecture establishes MathExplorer as a validated mathematical sequence recognition framework rather than a flat collection of independent pattern recognizers.

---

## Project Philosophy

MathExplorer was created to explore a simple question:

> *If a human mathematician looked at a sequence, what would they recognize first?*

Rather than searching for *any* function that reproduces a sequence, MathExplorer attempts to identify the **simplest and most meaningful mathematical family** that explains it.

To accomplish this, the library combines:

* Mathematical family recognition
* Parameter recovery
* Evaluation
* Prediction
* Verification
* Residual analysis
* Complexity-aware ranking
* Family specificity
* Confidence estimation
* Hierarchical mathematical organization
* Structured explanations

This allows meaningful mathematical families such as triangular numbers, factorials, Fibonacci numbers, and polygonal numbers to be preferred over overly general solutions when multiple explanations are possible.

The long-term goal of MathExplorer is to become a modular framework for mathematical sequence analysis that is both educational and extensible.

---

## Features

* Automatic sequence recognition
* Parameter recovery
* Formula generation
* Recursive relation support
* Sequence evaluation
* Future-term prediction
* Prediction verification
* Residual analysis
* Confidence scoring
* Complexity-aware family ranking
* Family specificity scoring
* Human-readable reports
* Structured explanations
* Mathematical family metadata
* Hierarchical family organization
* Parent-child family relationships
* Automatic family discovery
* Plugin validation
* Registry integrity validation
* Modular sequence family architecture
* Deterministic analysis behavior
* Comprehensive automated test suite
* Regression testing across the full architecture

---

## Sequence Family Hierarchy

MathExplorer organizes mathematical sequence families into a hierarchical taxonomy.

```text
Sequence Families
│
├── Explicit
│   │
│   ├── Basic
│   │   ├── Constant Numbers
│   │   ├── Arithmetic Numbers
│   │   ├── Geometric Numbers
│   │   └── Polynomial Numbers
│   │
│   ├── Figurate
│   │   │
│   │   ├── Polygonal
│   │   │   ├── Triangular Numbers
│   │   │   ├── Square Numbers
│   │   │   ├── Pentagonal Numbers
│   │   │   ├── Hexagonal Numbers
│   │   │   ├── Heptagonal Numbers
│   │   │   ├── Octagonal Numbers
│   │   │   ├── Nonagonal Numbers
│   │   │   └── Decagonal Numbers
│   │   │
│   │   └── Centered Polygonal
│   │       ├── Centered Triangular Numbers
│   │       ├── Centered Square Numbers
│   │       ├── Centered Pentagonal Numbers
│   │       └── Centered Hexagonal Numbers
│   │
│   └── Special
│       ├── Factorial Numbers
│       └── Pronic Numbers
│
├── Combinatorial
│   ├── Catalan Numbers
│   ├── Bell Numbers
│   ├── Derangement Numbers
│   └── Partition Numbers
│
└── Recursive
    │
    └── Linear Recurrence
        ├── Fibonacci Numbers
        ├── Lucas Numbers
        ├── Pell Numbers
        ├── Jacobsthal Numbers
        ├── Tribonacci Numbers
        ├── Tetranacci Numbers
        ├── Padovan Numbers
        └── Perrin Numbers
```

Additional recursive and self-referential families are also supported, including:

* Collatz Stopping Times
* Happy Numbers
* Look-and-Say Numbers
* Motzkin Numbers
* Van Eck Numbers

The hierarchy is validated by the family registry.

---

## Supported Sequence Families

### Basic Families

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

### Combinatorial Families

* Catalan
* Bell
* Derangement
* Partition

### Recursive Families

* Collatz Stopping Times
* Happy Numbers
* Look-and-Say
* Motzkin
* Van Eck

### Linear Recurrence Families

* Fibonacci
* Lucas
* Pell
* Jacobsthal
* Tribonacci
* Tetranacci
* Padovan
* Perrin

### Special Families

* Factorial
* Pronic

---

## Installation

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

## Quick Example

```python
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.display import print_report

sequence = [1, 3, 5, 7, 9]

report = analyze_sequence(sequence)

print_report(report)
```

Example output:

```text
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

MathExplorer automatically discovers sequence family modules placed inside the `families/` directory.

A family should define the required interface and metadata.

Example:

```python
NAME = "Example Family"
DESCRIPTION = "Description of the mathematical family."
REPRESENTATION = "Explicit"
CATEGORY = "Basic"
SPECIFICITY = 50
PARENT = "Basic"

recognize(sequence)
fit(sequence)
evaluate(parameters, n)
formula(parameters)
complexity(parameters)
explain(parameters)
```

Additional metadata should be included where appropriate:

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

Once the file is added, the registry automatically:

* Discovers the family.
* Validates the plugin interface.
* Validates its metadata.
* Validates its hierarchy relationship.
* Loads the family.
* Makes it available to the recognition pipeline.
* Includes it in scoring and prediction.

No manual registration is required.

For detailed instructions, see:

```text
families/creating_families.md
```

---

## Creating Extensions

MathExplorer uses automatic family discovery rather than manual family registration.

To add a new sequence family:

1. Determine the appropriate mathematical category.
2. Identify the correct parent family.
3. Create a new family module.
4. Implement the required family interface.
5. Add mathematical metadata.
6. Add family-level tests.
7. Run focused tests.
8. Run the complete test suite.

No additional registry configuration should be necessary.

---

## Recognition Pipeline

MathExplorer analyzes sequences through several stages:

```text
Input Sequence
      |
      v
Family Recognition
      |
      v
Parameter Fitting
      |
      v
Prediction Generation
      |
      v
Residual Analysis
      |
      v
Complexity-Aware Ranking
      |
      v
Confidence Analysis
      |
      v
Classification
      |
      v
Formula Recovery
      |
      v
Verification
      |
      v
Explanation
      |
      v
Report Generation
```

Each sequence family implements a common interface allowing new mathematical families to be added without modifying the central recognition engine.

---

## Family Recognition

Families determine whether they can explain a sequence.

Recognition results follow the system's family recognition conventions and may distinguish between:

* A recognized sequence.
* A rejected sequence.
* A sequence requiring more information.

Recognized families may then attempt parameter fitting.

---

## Family Ranking

Multiple families may successfully explain the same sequence.

MathExplorer ranks candidate families using mathematical evidence including:

* Prediction accuracy
* Residual error
* Complexity
* Family specificity
* Competition against alternative families
* Available sequence length

This allows a more meaningful mathematical family to beat an overly general explanation.

For example, a square sequence should prefer:

```text
Square Numbers
a(n) = n²
```

over a more general polynomial family when both perfectly reproduce the observed terms.

---

## Family Registry

The family registry automatically discovers and validates family modules.

The registry is responsible for:

1. Discovering family modules.
2. Loading valid plugins.
3. Validating required interfaces.
4. Validating family metadata.
5. Validating parent-child hierarchy relationships.
6. Rejecting invalid plugins.
7. Making valid families available to the analysis pipeline.

This allows the family system to grow without requiring central registration changes.

---

## Testing

MathExplorer includes a comprehensive automated test suite.

Run all tests with:

```bash
pytest
```

Current verified test suite:

```text
2031 passed, 38 skipped
```

Tests cover:

### Family Tests

* Recognition
* Rejection
* Fitting
* Evaluation
* Fit/evaluation consistency
* Predictions
* Mathematical properties
* Metadata

### Registry Tests

* Family discovery
* Plugin loading
* Plugin validation
* Hierarchy validation
* Family lookup
* Metadata behavior

### Pipeline Tests

* Classification
* Confidence
* Explanation
* Prediction
* Verification
* Formula recovery
* Scoring

### Regression Tests

* Recognition behavior
* Pipeline behavior
* Hierarchy behavior
* Explanation behavior
* Confidence behavior
* Prediction behavior

### Unit Tests

* Formatting
* Scoring
* Confidence factors
* Statistics
* Recovery
* Transformations
* Utilities
* Analysis trace

---

## Project Structure

```text
MathExplorer/
│
├── analyzers/
│   ├── sequence_analysis.py
│   ├── confidence_engine/
│   ├── core/
│   └── ...
│
├── families/
│   ├── core/
│   ├── basic/
│   ├── combinatorial/
│   ├── figurate/
│   ├── special/
│   ├── recursive/
│   └── ...
│
├── tests/
│   ├── families/
│   ├── integration/
│   ├── pipeline/
│   ├── registry/
│   ├── regression/
│   ├── unit/
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Project Status

MathExplorer v3.0 has completed its core family architecture and validation milestone.

The project currently has:

* A modular family plugin system.
* Automatic family discovery.
* A validated mathematical hierarchy.
* Comprehensive family metadata.
* Complexity-aware family ranking.
* Confidence analysis.
* Prediction and verification.
* Structured explanations.
* Analysis tracing.
* Over 2,000 automated tests.

Current verified test state:

```text
2031 passed, 38 skipped
```

---

## Roadmap

Future development may include:

* Additional mathematical sequence families.
* Expanded mathematical metadata.
* More advanced family relationships.
* Improved symbolic reasoning.
* Expanded visualization tools.
* User-facing mathematical exploration interfaces.
* OEIS integration.
* Export formats.
* Mathematical discovery features.

The core v3.0 architecture is now established, providing a stable foundation for future mathematical exploration and discovery.

---

## About the Author

MathExplorer was created by **Morrison Winterhalder** as an independent software and mathematics project.

The project began as an exploration of mathematical pattern recognition and has grown into a modular framework for identifying, verifying, and predicting numerical sequences.

It combines ideas from:

* Mathematics
* Software engineering
* Algorithm design
* Mathematical classification
* Pattern recognition

with an emphasis on clean architecture, extensibility, explainability, and reproducible testing.

Development continues with the goal of expanding MathExplorer's mathematical capabilities while maintaining a reliable and well-tested codebase.

---

## License

This project is licensed under the MIT License.
