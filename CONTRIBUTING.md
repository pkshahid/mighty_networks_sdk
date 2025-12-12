# Contributing to Mighty Networks Python SDK

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/mighty-networks-sdk.git
   cd mighty-networks-sdk
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

We follow PEP 8 style guidelines. Use these tools:

```bash
# Format code
black mighty_networks_sdk/

# Check linting
flake8 mighty_networks_sdk/

# Type checking
mypy mighty_networks_sdk/
```

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use pytest for testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=mighty_networks_sdk
```

### Documentation

- Add docstrings to all public methods
- Update README.md if adding new features
- Include usage examples

### Commit Messages

Follow conventional commits:

- `feat: Add new feature`
- `fix: Fix bug`
- `docs: Update documentation`
- `test: Add tests`
- `refactor: Refactor code`

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit pull request

## Code Review

- Be respectful and constructive
- Address all feedback
- Keep PRs focused and small

## Questions?

Open an issue or start a discussion!
