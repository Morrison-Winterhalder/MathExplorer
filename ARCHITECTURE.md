# MathExplorer Architecture

MathExplorer is built around a modular sequence recognition architecture.

The system separates mathematical recognition, family logic, scoring, reporting, and presentation into independent components. This allows new sequence families to be added without modifying the core recognition engine.

---

# High-Level Pipeline

A sequence is analyzed through the following stages:
Input Sequence
    |
    v
Sequence Analysis
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
Classification
    |
    v
Formula Recovery
    |
    v
Report Generation


---

# Project Structure

MathExplorer/

├── analyzers/
│
│ Core analysis pipeline and recognition logic.
│
├── families/
│
│ Individual sequence family plugins.
│
├── tests/
│
│ Automated validation and regression tests.
│
├── main.py
│
│ Entry point for running analyses.
│
└── README.md


---

# Sequence Families

MathExplorer uses a plugin-based family architecture.

Each sequence family is a self-contained module responsible for:

- Recognizing sequences
- Recovering parameters
- Generating terms
- Producing formulas
- Reporting complexity
- Providing explanations

Example:

Arithmetic Family

recognize()
|
fit()
|
evaluate()
|
formula()
|
complexity()
|
explain()


New families can be added without changing the recognition engine.

---

# Family Registry

The registry automatically discovers family modules inside the `families/` directory.

When MathExplorer starts, the registry:

1. Finds available family modules.
2. Validates their interfaces.
3. Loads valid families.
4. Makes them available to the analysis pipeline.

No manual registration is required.

---

# Family Hierarchy System

MathExplorer organizes sequence families into a hierarchical taxonomy.

Each family may define a `PARENT` field pointing to another family category. The registry validates these relationships and uses them to construct family trees.

This allows MathExplorer to represent mathematical relationships between sequence families rather than treating every family as an isolated pattern.

---

## Current Sequence Family Hierarchy

```
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
│   │   │   └── Hexagonal Numbers
│   │   │
│   │   └── Centered Polygonal
│   │       ├── Centered Triangular Numbers
│   │       ├── Centered Square Numbers
│   │       ├── Centered Pentagonal Numbers
│   │       └── Centered Hexagonal Numbers
│   │
│   └── Special
│       └── Factorial Numbers
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

---

## Parent Families

Some families exist primarily as organizational categories rather than recognizable sequence types.

Examples:

- `Figurate`
- `Polygonal`
- `Centered Polygonal`
- `Linear Recurrence`

These families provide structure for the taxonomy but do not directly recognize sequences.

Their purpose is to:

- organize related families
- provide future metadata inheritance
- support family browsing
- enable hierarchical explanations
- improve developer understanding

---

## Hierarchy Validation

The registry verifies that:

- every declared parent exists
- family names are unique
- family relationships are valid

Invalid hierarchies raise a `PluginError` during startup.

Example:

```python
NAME = "Centered Square Numbers"
PARENT = "Centered Polygonal"
```

requires a family named:

```python
NAME = "Centered Polygonal"
```

to exist.

---

## Future Hierarchy Expansion

The hierarchy system is designed to support future features including:

- inherited metadata
- family category filtering
- improved explanations
- graphical family exploration
- UI navigation

---

# Recognition System

Each family attempts to determine whether it can explain a sequence.

Families return:

- `True` if the pattern is recognized.
- `False` if the pattern does not match.
- `None` if there is insufficient information.

Recognized families then attempt parameter fitting.

---

# Scoring System

Multiple families may successfully describe the same sequence.

MathExplorer ranks successful families using:

- Prediction accuracy
- Residual error
- Complexity
- Family specificity

This allows more meaningful families to beat overly general solutions.

Example:

A square sequence should prefer:

"Square Numbers"
a(n) = n²

over:

"Polnomial"


even though both may perfectly fit the same terms.

---

# Metadata System

Each family contains mathematical metadata describing:

- Mathematical category
- Hierarchy
- Growth behavior
- Recognition method
- Reliability
- Formula type
- Parameters

Metadata is attached to classification reports and provides the foundation for future documentation, UI features, and explanation systems.

---

# Formatting System

Formula output passes through shared formatting utilities.

These handle:

- Exponent formatting
- Operator spacing
- Mathematical notation normalization

Example:

a(n) = 2*3^(n-1)

becomes:

a(n) = 2·3⁽ⁿ⁻¹⁾


---

# Testing Architecture

MathExplorer uses automated tests to verify:

- Family recognition
- Formula recovery
- Prediction accuracy
- Scoring behavior
- Registry integrity
- Formatting consistency

Every new family should include corresponding tests.