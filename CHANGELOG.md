# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-12

### Added
- Initial release of Mighty Networks Python SDK
- Complete coverage of all 137 API endpoints
- Support for 18 resource categories:
  - Spaces (19 endpoints)
  - Members (19 endpoints)
  - Posts (15 endpoints)
  - Events (12 endpoints)
  - Plans (13 endpoints)
  - Custom Fields (16 endpoints)
  - Comments (3 endpoints)
  - Tags (6 endpoints)
  - Subscriptions (3 endpoints)
  - Purchases (3 endpoints)
  - Polls (6 endpoints)
  - Invites (5 endpoints)
  - Collections (7 endpoints)
  - Badges (6 endpoints)
  - Assets (1 endpoint)
  - Abuse Reports (1 endpoint)
- Bearer token authentication
- Comprehensive error handling with specific exception classes
- Full type hints for better IDE support
- Pagination support for list endpoints
- Detailed documentation and examples
- Unit tests with pytest
- Code quality tools (black, flake8, mypy)

### Features
- Production-ready client with timeout and retry configuration
- Automatic error handling and response parsing
- Data models for common API objects
- Batch operation examples
- Pagination helper examples
- Comprehensive error handling examples

### Documentation
- Complete README with usage examples
- API reference documentation
- Quick start guide
- Advanced usage examples
- Contributing guidelines

## [Unreleased]

### Planned
- Async support with aiohttp
- Webhook support
- Rate limiting with automatic retry
- Response caching
- CLI tool for common operations
- Additional helper methods for complex workflows
