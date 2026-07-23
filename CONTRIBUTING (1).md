# Contributing to phytrade

Thank you for your interest in contributing to **phytrade**! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Pull Requests](#pull-requests)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Release Process](#release-process)

---

## Getting Started

- Ensure you have a [GitHub account](https://github.com/signup).
- Fork the repository on GitHub.
- Clone your fork locally:
  ```bash
  git clone https://github.com/YOUR_USERNAME/phytrade.git
  cd phytrade
  ```

## Development Setup

### Prerequisites

- Python 3.9+
- pip

### Install in Development Mode

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with development dependencies
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Run Linters

```bash
# Format code
black phytrade tests

# Check style
flake8 phytrade tests

# Type checking (if applicable)
mypy phytrade
```

---

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check the [existing issues](https://github.com/ksaad20/phytrade/issues) to avoid duplicates.

When filing a bug report, please include:

- **Clear title** and description
- **Steps to reproduce** the issue
- **Expected behavior** vs. actual behavior
- **Environment details**: Python version, OS, phytrade version
- **Minimal code example** that reproduces the issue

Use the [Bug Report template](https://github.com/ksaad20/phytrade/issues/new?template=bug_report.md) if available.

### Suggesting Features

Feature requests are welcome! Please provide:

- **Clear use case** — what problem does this solve?
- **Proposed API or interface** (if applicable)
- **Potential alternatives** you've considered

Use the [Feature Request template](https://github.com/ksaad20/phytrade/issues/new?template=feature_request.md) if available.

### Pull Requests

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our [Coding Standards](#coding-standards).

3. **Add tests** for any new functionality.

4. **Update documentation** (README, docstrings, etc.) if needed.

5. **Run tests and linters** locally:
   ```bash
   pytest
   black --check phytrade tests
   ```

6. **Commit** with a clear message (see [Commit Messages](#commit-messages)).

7. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request** against `ksaad20/phytrade:main`.

   In your PR description, include:
   - What changes were made
   - Why they were made
   - Any breaking changes
   - Link to related issue(s) (e.g., `Fixes #123`)

---

## Coding Standards

- **PEP 8** style guide
- **Black** for code formatting (line length: 88)
- **Type hints** encouraged for public APIs
- **Docstrings** in Google or NumPy style
- **Tests** required for new features

### Example Function

```python
def calculate_profit(entry_price: float, exit_price: float, quantity: int) -> float:
    """Calculate trading profit/loss.

    Args:
        entry_price: Price at which the position was entered.
        exit_price: Price at which the position was exited.
        quantity: Number of units traded.

    Returns:
        Net profit (positive) or loss (negative).

    Example:
        >>> calculate_profit(100.0, 110.0, 10)
        100.0
    """
    return (exit_price - entry_price) * quantity
```

---

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

| Type | Use for |
|------|---------|
| `feat` | New features |
| `fix` | Bug fixes |
| `docs` | Documentation changes |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Adding or updating tests |
| `chore` | Maintenance, dependencies |

**Examples:**

```
feat(indicators): add RSI momentum indicator

fix(data): handle missing OHLCV values gracefully

docs(readme): update installation instructions for conda
```

---

## Release Process

Releases are managed by maintainers:

1. Version bump in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a Git tag: `git tag vX.Y.Z`
4. Push tag: `git push origin vX.Y.Z`
5. GitHub Actions publishes to PyPI automatically

---

## Questions?

- Open a [Discussion](https://github.com/ksaad20/phytrade/discussions)
- Or email the maintainer at [your-email@example.com]

---

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

Thank you for contributing! 🚀
