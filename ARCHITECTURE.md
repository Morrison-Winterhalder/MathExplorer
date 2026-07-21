# MathExplorer Architecture

MathExplorer is a modular mathematical sequence recognition and analysis system.

The system is designed around the principle:

> **Recognize → Explain → Reason → Discover**

MathExplorer separates sequence recognition, family logic, hierarchy, scoring, confidence analysis, explanation generation, prediction, verification, transformations, tracing, and reporting into independent components.

This architecture allows new mathematical sequence families to be added without modifying the central analysis pipeline.

---

# High-Level Architecture

A sequence moves through a multi-stage analysis pipeline:

```text
Input Sequence
      |
      v
Sequence Analysis Object
      |
      v
Basic Information
      |
      v
Mathematical Properties
      |
      v
Transformations
      |
      v
Family Recognition
      |
      v
Parameter Fitting
      |
      v
Candidate Scoring
      |
      v
Family Ranking
      |
      v
Classification
      |
      v
Confidence Analysis
      |
      v
Explanation Generation
      |
      v
Prediction Generation
      |
      v
Verification
      |
      v
Report Generation
```

Throughout the process, MathExplorer records internal reasoning events in an **Analysis Trace**.

The trace allows the system to preserve the sequence of analytical decisions that produced the final result.

---

# Project Structure

```text
MathExplorer/

├── analyzers/
│
│   Core mathematical analysis and pipeline logic.
│
├── families/
│
│   Mathematical sequence family plugins and family infrastructure.
│
├── tests/
│
│   Unit, integration, regression, family, registry, and pipeline tests.
│
├── main.py
│
│   Entry point for running analyses.
│
└── README.md
```

The architecture is intentionally modular.

The core analyzers do not need to know the internal implementation of every mathematical family.

Instead, families expose a standardized interface that allows the pipeline to interact with them uniformly.

---

# Sequence Analysis Object

The central output of the analysis pipeline is the `SequenceAnalysis` object.

It acts as the structured state container for the entire analysis.

```text
SequenceAnalysis
│
├── Analysis Trace
├── Sequence Classification
├── Recognition Scores
├── Verification
├── Predictions
├── Basic Information
├── Properties
├── Transformations
├── Explanation
├── Developer Mind-Model
└── Confidence
```

The object provides both:

* structured dictionary-style access
* convenient property-based access

For example:

```python
analysis["Sequence Classification"]
analysis["Confidence"]
analysis["Predictions"]
```

and:

```python
analysis.family
analysis.family_name
analysis.parameters
analysis.formula
analysis.confidence_score
analysis.confidence_label
analysis.next_terms
analysis.verified
```

This provides a consistent interface for both internal pipeline stages and external reporting.

---

# Sequence Analysis Components

## Basic Information

Basic information describes fundamental properties of the input sequence.

Examples include:

* Sequence length
* Initial terms
* Numerical characteristics
* General structural information

---

## Properties

The properties system analyzes mathematical behavior such as:

* Monotonicity
* Boundedness
* Oscillation
* Periodicity

These properties are independent of family recognition.

A sequence can therefore be analyzed mathematically even when no specialized family recognizes it.

---

## Transformations

The transformation system analyzes derived structures of a sequence.

Examples include:

* First differences
* Higher-order differences
* Ratios
* Other mathematical transformations

Transformations can reveal structure that is not immediately visible in the original sequence.

---

## Classification

Classification stores the selected mathematical family and its associated information.

Typical classification data includes:

```text
Family
Parameters
Formula
Hierarchy
```

The classification is the final result of the recognition and ranking process.

---

## Recognition Scores

Recognition scores store the results of comparing candidate families.

This allows MathExplorer to preserve information about:

* Candidate families
* Fit quality
* Prediction error
* Residuals
* Complexity
* Relative ranking

The system does not simply ask:

> "Does this family fit?"

It also asks:

> "How well does this family fit compared with the alternatives?"

---

## Confidence

Confidence is a structured analysis of how strongly MathExplorer supports its classification.

Confidence can incorporate:

* Fit quality
* Competition between candidate families
* Sequence sample size
* Model complexity
* Classification ambiguity

Confidence is therefore not simply a raw error score.

A sequence can have an excellent fit but still have low confidence if multiple families explain it equally well.

---

## Explanation

The explanation system converts internal analytical results into a human-readable explanation.

Explanations can incorporate:

* The selected family
* The mathematical structure recognized
* The hierarchy of the family
* Recognition evidence
* Confidence factors
* Tie or ambiguity information
* The reason the selected family was preferred

The explanation system is separate from the recognition logic.

This means a family can recognize a sequence without needing to contain the complete logic for explaining the entire classification decision.

---

## Developer Mind-Model

The Developer Mind-Model contains structured information intended to expose how the analysis system arrived at its result.

It is separate from the normal user-facing explanation.

The purpose of the Developer Mind-Model is to support:

* Debugging
* Development
* Recognition analysis
* Internal reasoning inspection
* Understanding pipeline behavior

This allows MathExplorer to expose more detailed internal structure without requiring the normal output to contain every internal analytical step.

---

# Analysis Trace

The Analysis Trace records the sequence of important events during analysis.

Examples of trace events include:

```text
family_tested
family_fit
family_rejected
scores_updated
confidence_updated
explanation_started
explanation_generated
prediction_started
predictions_generated
verification_started
verification_completed
```

The trace is an internal chronological record of the analysis process.

It allows MathExplorer to answer questions such as:

* Which families were tested?
* Which families were rejected?
* Which family won?
* Why was a family selected?
* When was confidence calculated?
* When was the explanation generated?
* When were predictions created?
* Was the final classification verified?

The trace is also used by later pipeline stages to understand what occurred earlier in the analysis.

---

# Sequence Families

MathExplorer uses a plugin-based family architecture.

Each sequence family is a self-contained module responsible for defining its own mathematical behavior.

A family may provide:

```text
recognize()
    |
    v
fit()
    |
    v
evaluate()
    |
    v
formula()
    |
    v
complexity()
    |
    v
explain()
```

The core family contract allows MathExplorer to interact with fundamentally different types of sequences using a common interface.

Families may represent:

* Explicit formulas
* Polynomial structures
* Figurate sequences
* Combinatorial sequences
* Recursive sequences
* Self-referential sequences
* Digit-based processes
* Iterative transformations
* Other mathematical constructions

New families can be added without modifying the central recognition pipeline.

---

# Family Recognition Contract

A family determines whether it can explain a sequence.

Recognition results follow a three-state model:

```text
True
│
└── The sequence is recognized.

False
│
└── The sequence does not match.

None
│
└── There is insufficient information to determine recognition.
```

This distinction is important.

`False` means the available evidence contradicts the family.

`None` means the sequence may be compatible, but there is not enough information to make a reliable determination.

Recognized families may then attempt parameter fitting.

---

# Parameter Fitting

After successful recognition, a family attempts to recover the parameters necessary to reproduce the sequence.

Examples include:

```text
Arithmetic:
    Difference

Geometric:
    Ratio

Polynomial:
    Coefficients

Recursive:
    Seeds
    Recurrence Coefficients
```

Some families require no parameters.

For example, a fixed family such as a specific named sequence may simply return:

```python
{}
```

when recognized.

---

# Family Evaluation

The `evaluate()` function generates the value of a family at a given index.

This allows the same interface to support:

* Prediction
* Verification
* Reproduction testing
* Future-term generation

For example:

```python
family.evaluate(parameters, n)
```

generates the term at index `n`.

The pipeline does not need to know whether the family uses:

* A closed formula
* A recurrence
* An iterative process
* A combinatorial algorithm
* A digit transformation

The family itself owns that logic.

---

# Family Registry

The registry automatically discovers family modules inside the `families/` directory.

When MathExplorer starts, the registry:

1. Discovers available family modules.
2. Loads family metadata.
3. Validates family contracts.
4. Validates family names.
5. Validates hierarchy relationships.
6. Registers valid families.
7. Makes them available to the analysis pipeline.

No manual registration is required for individual family plugins.

This creates a plugin architecture in which adding a new family primarily requires adding the family module itself.

---

# Family Hierarchy System

MathExplorer organizes sequence families into a hierarchical mathematical taxonomy.

Each family may define a:

```python
PARENT = "Parent Family"
```

field.

The registry uses these relationships to construct a family hierarchy.

This allows MathExplorer to represent mathematical relationships between sequence families rather than treating every family as an isolated pattern.

Hierarchy information is also available to later stages such as:

* Explanation generation
* Classification reporting
* Family browsing
* Developer tools
* Future visualization systems

---

# Current Sequence Family Hierarchy

The current hierarchy is organized as follows:

```text
Sequence Families
│
├── Explicit
│   │
│   ├── Basic
│   │   ├── Constant
│   │   ├── Arithmetic
│   │   ├── Geometric
│   │   └── Polynomial
│   │       ├── Cubes
│   │       ├── Squares
│   │       ├── Fifth Powers
│   │       ├── Fourth Powers
│   │       └── Pronic Numbers
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
│       └── Factorials
│
└── Recursive
    │
    ├── Linear Recurrence
    │   ├── Fibonacci
    │   ├── Lucas Numbers
    │   ├── Pell Numbers
    │   ├── Jacobsthal Numbers
    │   ├── Tribonacci Numbers
    │   ├── Tetranacci Numbers
    │   ├── Padovan Numbers
    │   └── Perrin Numbers
    │
    ├── Collatz Stopping Times
    ├── Happy Numbers
    ├── Look-and-Say Numbers
    ├── Motzkin Numbers
    └── Van Eck Numbers
```

The hierarchy is extensible and can continue to grow as new mathematical families are added.

---

# Parent Families

Some hierarchy nodes exist primarily as organizational categories rather than directly recognizable sequence families.

Examples include:

```text
Explicit
Basic
Figurate
Polygonal
Centered Polygonal
Recursive
Linear Recurrence
```

These categories provide structure for the taxonomy.

Their purposes include:

* Organizing related families
* Representing mathematical relationships
* Supporting family browsing
* Providing hierarchical context for explanations
* Enabling future metadata inheritance
* Improving developer understanding of the family system

A parent family does not necessarily need to implement a direct recognition algorithm.

---

# Hierarchy Validation

The registry validates the hierarchy during startup.

It verifies that:

* Family names are unique.
* Declared parents exist.
* Parent-child relationships are valid.
* The hierarchy can be constructed consistently.

Invalid hierarchy relationships raise a `PluginError`.

For example:

```python
NAME = "Centered Square Numbers"
PARENT = "Centered Polygonal"
```

requires:

```python
NAME = "Centered Polygonal"
```

to exist.

---

# Recognition and Ranking

Multiple families may successfully describe the same sequence.

For example, a square sequence may also be mathematically describable as a polynomial.

Therefore, MathExplorer separates:

```text
Recognition
```

from:

```text
Classification
```

Recognition asks:

> Can this family explain the sequence?

Classification asks:

> Which recognized family is the most meaningful explanation?

This distinction is central to the architecture.

---

# Scoring System

MathExplorer ranks successful candidate families using multiple factors.

These include:

* Fit quality
* Prediction accuracy
* Residual error
* Family specificity
* Complexity
* Competition from alternative families
* Sequence sample size

A family that fits perfectly is not automatically guaranteed to win.

For example:

```text
Sequence:
1, 4, 9, 16, 25, ...
```

may be recognized as both:

```text
Squares
```

and:

```text
Polynomial
```

The scoring system should prefer the more mathematically specific explanation:

```text
Squares
```

over the broader:

```text
Polynomial
```

This allows MathExplorer to distinguish between:

> "This sequence can be represented by a polynomial."

and:

> "This sequence is specifically the sequence of square numbers."

---

# Complexity-Aware Recognition

Complexity is one of the factors used when comparing candidate families.

A more complex explanation should not automatically defeat a simpler one merely because it can fit the data.

At the same time, simplicity alone should not override mathematical specificity.

MathExplorer therefore combines:

```text
Fit
+
Prediction
+
Specificity
+
Complexity
+
Competition
```

to determine the strongest classification.

---

# Confidence System

Confidence is calculated separately from classification.

This is important because:

```text
Best Family ≠ Certain Family
```

A sequence can have a clear winning family with high confidence.

Alternatively, multiple families may fit equally well, producing an ambiguous result.

Confidence analysis considers factors such as:

* Fit quality
* Separation from competing families
* Sequence length
* Complexity

The confidence system can therefore distinguish between:

```text
Strong Classification
```

and:

```text
Weak Classification
```

even when both have the same nominal winning family.

---

# Explanation Engine

The explanation engine transforms structured analysis into a human-readable explanation.

It uses information from:

* Classification
* Family metadata
* Hierarchy
* Recognition results
* Confidence
* Analysis Trace
* Tie detection
* Tie resolution

The explanation engine can therefore explain not only:

> What family was selected?

but also:

> Why was this family selected over competing alternatives?

This separates mathematical recognition from reasoning about the recognition result.

---

# Prediction System

Once a family has been classified and fitted, MathExplorer can generate future terms.

The prediction pipeline:

```text
Classification
      |
      v
Parameters
      |
      v
Family Evaluation
      |
      v
Future Terms
```

The family-specific `evaluate()` method is used to generate future values.

This allows predictions to work consistently across:

* Explicit formulas
* Polynomial families
* Figurate families
* Recursive sequences
* Combinatorial sequences
* Iterative sequences
* Self-referential sequences

---

# Verification System

Predictions and classifications can be verified against known sequence terms.

The verification system evaluates the selected family and compares generated terms with the original input.

The final report can therefore indicate whether the classification reproduces the observed sequence.

Conceptually:

```text
Observed Sequence
        |
        v
Family Evaluation
        |
        v
Generated Sequence
        |
        v
Comparison
        |
        v
Verified / Not Verified
```

This provides an additional validation layer after recognition and classification.

---

# Formula and Formatting System

Mathematical formulas pass through shared formatting utilities.

The formatting system provides consistent mathematical representation across families and reports.

It handles tasks such as:

* Exponent formatting
* Operator spacing
* Mathematical notation normalization
* Recurrence formatting
* Formula representation

For example:

```text
a(n) = 2*3^(n-1)
```

may be formatted as:

```text
a(n) = 2·3⁽ⁿ⁻¹⁾
```

Families do not need to independently implement formatting logic.

---

# Testing Architecture

MathExplorer v3.0 uses a large automated test architecture.

The test suite validates the system at multiple levels.

```text
tests/
│
├── families/
│   ├── Family Contracts
│   ├── Family Metadata
│   ├── Family Recognition
│   ├── Family Rejection
│   ├── Family Predictions
│   ├── Fit/Evaluate Consistency
│   ├── Basic Families
│   ├── Combinatorial Families
│   ├── Figurate Families
│   ├── Linear Recurrence Families
│   └── Special Families
│
├── integration/
│
├── pipeline/
│
├── registry/
│
├── regression/
│
└── unit/
```

The suite tests:

* Family contracts
* Recognition
* Rejection
* Parameter fitting
* Evaluation
* Prediction
* Verification
* Metadata
* Hierarchy
* Registry loading
* Registry lookup
* Confidence
* Explanation
* Pipeline behavior
* Regression behavior
* Properties
* Transformations
* Recovery
* Statistics
* Trace
* Formatting
* Utilities

At the completion of the v3.0 development cycle:

```text
2,069 tests collected
2,031 passed
38 skipped
0 failed
```

The test suite therefore provides a comprehensive regression safety net for the completed v3.0 architecture.

---

# Design Principles

MathExplorer v3.0 is built around several architectural principles.

## 1. Modularity

Each mathematical family is independently implemented.

---

## 2. Extensibility

New families can be added without modifying the central recognition engine.

---

## 3. Separation of Concerns

Recognition, scoring, confidence, explanation, prediction, verification, and reporting are separate systems.

---

## 4. Hierarchical Mathematical Organization

Families are organized into a taxonomy that represents mathematical relationships between sequence types.

---

## 5. Evidence-Based Classification

Classification is based on multiple factors rather than a single fit score.

---

## 6. Explainability

MathExplorer preserves enough structured information to explain both:

```text
What was recognized
```

and:

```text
Why it was selected
```

---

## 7. Traceability

The Analysis Trace records the major stages and decisions of the pipeline.

---

## 8. Test-Driven Architecture

The architecture is validated continuously through unit, integration, regression, and family-level tests.

---

# Summary

MathExplorer v3.0 is a modular sequence analysis architecture that combines:

```text
Mathematical Recognition
        +
Family Plugins
        +
Hierarchical Taxonomy
        +
Candidate Scoring
        +
Confidence Analysis
        +
Explanation Generation
        +
Prediction
        +
Verification
        +
Analysis Trace
        +
Developer Mind-Model
        +
Automated Testing
```

The result is a system capable of more than identifying sequence patterns.

MathExplorer is designed to determine:

> **What mathematical structure does this sequence have?**

> **Where does that structure belong in the broader mathematical hierarchy?**

> **Why was that family selected over alternatives?**

> **How confident is the system in that classification?**

> **Can the recognized structure reproduce and predict the sequence?**

This architecture forms the foundation of MathExplorer v3.0.
