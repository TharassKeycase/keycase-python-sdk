# Contributing to Keycase Agent SDK

Thank you for your interest in contributing to the Keycase Agent SDK!

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/TharassKeycase/keycase-python-sdk.git
   cd keycase-python-sdk
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks** (optional but recommended)
   ```bash
   pre-commit install
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=keycase_agent --cov-report=html

# Run specific test file
pytest tests/test_decorators.py -v
```

### Code Formatting

We use `black` for code formatting and `isort` for import sorting:

```bash
# Format code
black keycase_agent/

# Sort imports
isort keycase_agent/

# Check without modifying
black --check keycase_agent/
isort --check-only keycase_agent/
```

### Type Checking

```bash
mypy keycase_agent/
```

### Linting

```bash
flake8 keycase_agent/
```

## Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write tests for new functionality
   - Ensure all tests pass
   - Follow the existing code style

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

   We follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `test:` - Adding or updating tests
   - `refactor:` - Code refactoring
   - `chore:` - Maintenance tasks

4. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a Pull Request on GitHub.

## Code Style Guidelines

- Use type hints for all function parameters and return values
- Write docstrings for public functions and classes
- Keep functions focused and small
- Use descriptive variable names
- Follow PEP 8 guidelines

## Adding New Keywords (Examples)

When adding example keywords to the `examples/` directory:

1. Use `type="string"` for all parameters (other types are Phase 2)
2. Include docstrings explaining the keyword
3. Handle type conversion within the function body
4. Return a dictionary with named outputs

Example:
```python
@keyword("My Keyword")
@input_param("value", type="string", required=True, description="Input value")
@output_param("result", type="string", description="Output result")
def my_keyword(value: str) -> dict:
    """Description of what the keyword does."""
    # Process the value
    result = value.upper()
    return {"result": result}
```

## Reporting Issues

When reporting issues, please include:

- Python version (`python --version`)
- OS and version
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces

## Questions?

Open an issue on GitHub or contact us at support@keycase.io.
