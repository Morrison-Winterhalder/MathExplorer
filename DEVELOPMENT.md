# MathExplorer Development Guide

This document describes how to set up, run, and contribute to MathExplorer.

---

# Development Setup

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

# Running MathExplorer

Run the main program:

```bash
python main.py
```

A sequence can then be analyzed through the sequence analysis pipeline.

---

# Running Tests

Run the complete test suite:

```bash
pytest
```

Tests should pass before making changes to the project.

---

# Development Workflow

Typical development steps:

1. Make changes.
2. Add or update tests.
3. Run the test suite.
4. Verify output formatting.
5. Commit changes.

---

# Adding a Sequence Family

To add a new mathematical family:

1. Create a new Python file inside:

```text
families/
```

2. Implement the required family interface.

3. Add required metadata.

4. Add tests.

5. Run the full test suite.

For detailed family instructions, see:

```text
families/creating_families.md
```

---

# Code Organization

## analyzers/

Contains the sequence recognition and analysis pipeline.

Responsibilities include:

- Recognition
- Scoring
- Classification
- Formula recovery
- Reporting

---

## families/

Contains all sequence family plugins.

Each family defines its own:

- Recognition rules
- Evaluation logic
- Formula generation
- Metadata

---

## tests/

Contains automated verification.

Tests are organized around:

- Recognition
- Recovery
- Prediction
- Scoring
- Formatting
- Registry behavior

---

# Development Principles

MathExplorer follows several design principles.

## Modularity

Sequence families should remain independent from the core engine.

Each family should contain its own recognition logic, evaluation methods, and metadata.

---

## Extensibility

Adding new mathematical patterns should require minimal changes to the core system.

New families should be added through the existing plugin architecture.

---

## Explainability

The system should provide meaningful reasoning behind classifications.

Family metadata and explanations are designed to support future explanation systems.

---

## Reliability

Changes should be validated through automated testing.

All new functionality should include appropriate tests.

---

# Style Guidelines

When adding code:

- Prefer clear mathematical naming.
- Keep family logic inside family modules.
- Avoid unnecessary changes to shared infrastructure.
- Add tests for new functionality.
- Use existing formatting utilities.
- Maintain consistency with existing metadata conventions.

---

# Future Development

Major future development areas include:

- Expanded sequence families
- Improved explanation systems
- UI improvements
- Visualization tools
- Advanced metadata usage