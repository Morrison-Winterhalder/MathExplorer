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