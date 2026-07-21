# Changelog

## v1.0 - Initial Release

### Added
- Constant sequence detection
- Arithmetic sequence detection
- Geometric sequence detection
- Polynomial sequence detection
- Polynomial recovery
- Formula verification
- Prediction engine
- Confidence scoring
- Pretty-number formatting

### Changed
- Complete architectural refactor
- Modular pipeline design
- Modular recovery and classification systems

------------------------

## Version 1.5

### Added

- Triangular sequence recognition
- Pentagonal sequence recognition
- Fibonacci sequence recognition
- Lucas sequence recognition
- Pell sequence recognition
- Jacobsthal sequence recognition
- Factorial sequence recognition

### Improved

- Refactored classification into handler architecture
- Refactored recovery into handler architecture
- Refactored prediction into handler architecture
- Refactored verification into handler architecture
- Added generic linear recurrence evaluator
- Improved report formatting
- Improved project modularity

### Testing

- Added automated regression test suite
- Added classification tests
- Added recovery tests
- Added verification tests
- Added prediction tests

### Result

MathExplorer v1.5 now supports **11 mathematical sequence families** through a modular analysis pipeline capable of classification, formula recovery, verification, and prediction.

------------------------

## v2.1.0 — Plugin Foundation

### Added
- Automatic plugin discovery
- Plugin validation
- Family metadata
- Formula interface
- Hexagonal numbers

### Changed
- Refactored all sequence families
- Simplified recognition engine
- Improved confidence scoring
- Improved reporting

### Quality
- 83 automated tests passing

------------------------

## v2.2.0

### New Features
------------
- Automatic plugin discovery
- Plugin validation
- New CATEGORY metadata
- New SPECIFICITY metadata
- Recognition now prefers more specific families
- Added figurate-number plugin category

### New Families
------------
- Squares
- Cubes
- Fourth Powers
- Fifth Powers
- Hexagonal
- Centered Triangular
- Centered Square
- Centered Pentagonal
- Centered Hexagonal

### Improvements
------------
- Cleaner recognition ranking
- Improved runner-up logic
- Improved plugin architecture

### Bug Fixes
---------
- Runner-up determination after specificity
- Registry validation
- Display fixes

------------------------

## v2.3 — Event-Driven Analysis Pipeline

### Added

* Introduced the **Analysis Trace**, providing a complete event log of the analysis pipeline.
* Added modular **event renderers** for developer output.
* Added **Reasoning Summary** to the Developer Mind-Model.
* Added **Analysis Complete** section to indicate successful pipeline execution.
* Added detailed prediction rendering with indexed generated terms.
* Added verification events documenting sequence regeneration.

### Changed

* Refactored the Developer Mind-Model to render entirely from the Analysis Trace.
* Separated execution logic from presentation logic through dedicated renderer modules.
* Improved confidence reporting with clearer breakdowns of scoring components.
* Improved formula recovery presentation.
* Improved prediction and verification output formatting.
* Simplified classification presentation while preserving hierarchy information.

### Fixed

* Corrected polynomial formula formatting (e.g. `n²` instead of `1n²`).
* Standardized symbolic formatting across recovered formulas.
* Fixed verification pipeline integration with prediction generation.
* Updated the test suite to reflect the event-driven architecture.

### Testing

* 112 automated tests passing.
* Full Developer Mind-Model rendering verified.
* End-to-end pipeline validation completed.

------------------------

## v2.5

### Added

- Metadata system for sequence families
- Family hierarchy support
- Improved mathematical formatting
- Expanded power and figurate sequence support
- Metadata integration into classification reports

### Changed

- Sequence families now contain richer self-describing information
- Formula output uses normalized mathematical notation
- Family recognition pipeline carries metadata

### Fixed

- Negative root recognition errors
- Recursive formula recovery issues
- Family registry collisions

------------------------

# v3.0.0

## Added

* Completed the v3.0 sequence family architecture.
* Added a hierarchical taxonomy for sequence families and mathematical categories.
* Added parent-child relationships between sequence families.
* Added family registry validation for hierarchy integrity.
* Added automatic family discovery and plugin loading.
* Added comprehensive mathematical metadata to sequence family modules, including:

  * OEIS references
  * Aliases
  * Family relationships
  * Growth behavior
  * Construction methods
  * Domain information
  * Recognition methods
  * Reliability
  * Formula types
  * Tags and traits
* Added support for organizational hierarchy families such as:

  * `Sequence Families`
  * `Explicit`
  * `Basic`
  * `Figurate`
  * `Polygonal`
  * `Centered Polygonal`
  * `Special`
  * `Recursive`
  * `Linear Recurrence`
* Added new sequence family implementations across:

  * Basic families
  * Combinatorial families
  * Figurate families
  * Special families
  * Recursive families
  * Linear recurrence families
* Added comprehensive family-level testing covering recognition, fitting, evaluation, prediction, metadata, hierarchy, rejection, and mathematical properties.
* Added regression coverage for the full analysis pipeline and family hierarchy.
* Expanded the test suite to over 2,000 automated tests.

## Changed

* Refactored sequence families into a modular plugin architecture.
* Changed family organization from a flat collection of sequence recognizers into a hierarchical mathematical taxonomy.
* Changed family registration from manual registration to automatic discovery.
* Standardized family interfaces around:

  * `recognize()`
  * `fit()`
  * `evaluate()`
  * `formula()`
  * `complexity()`
  * `explain()`
* Expanded family metadata to support mathematical classification and hierarchical relationships.
* Improved scoring to account for:

  * Prediction accuracy
  * Residual error
  * Complexity
  * Family specificity
* Expanded shared formatting utilities for mathematical formulas and recurrence relations.
* Updated the architecture to separate family logic, recognition, scoring, reporting, and presentation into independent components.
* Expanded automated validation across the family system, registry, analysis pipeline, confidence system, prediction system, verification system, explanation system, and regression suite.

## Fixed

* Fixed family registry validation for missing and invalid parent relationships.
* Fixed family discovery and plugin validation issues.
* Fixed recognition and evaluation inconsistencies across sequence families.
* Fixed prediction and fitting inconsistencies across family implementations.
* Fixed incorrect family metadata for mathematical properties such as monotonicity, boundedness, oscillation, and periodicity.
* Fixed incorrect indexing and recurrence behavior in multiple sequence families.
* Fixed formula and recurrence formatting inconsistencies.
* Fixed hierarchy relationships across family categories.
* Fixed regression issues across the recognition, scoring, explanation, prediction, verification, and reporting pipeline.
* Verified the complete test suite with:

**2,031 passed, 38 skipped**
