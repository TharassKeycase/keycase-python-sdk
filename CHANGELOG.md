# Changelog

All notable changes to the Keycase Agent SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

## [0.1.0b1] - 2024-12-10

### Added
- Initial release of Keycase Agent SDK
- `@keyword` decorator for registering automation keywords
- `@param`, `@input_param`, `@output_param` decorators for parameter metadata
- Parameter validation (name matching, required parameters)
- WebSocket-based connection to Keycase server
- Local execution mode for standalone testing
- Automatic reconnection with exponential backoff
- Token refresh management
- Execution hooks (`@BeforeRun`, `@AfterRun`)
- `get_keyword_schema()` and `get_all_keyword_schemas()` for schema generation
- Support for parameter choices (dropdown rendering)
- Comprehensive type hints throughout the codebase
- Example keywords (calculator, string operations, advanced features)

### Notes
- Parameter types (number, integer, boolean, object, array) are accepted but treated as strings
- Full type validation planned for Phase 2 (see ROADMAP.md)

[Unreleased]: https://github.com/TharassKeycase/keycase-python-sdk/compare/v0.1.0b1...HEAD
[0.1.0b1]: https://github.com/TharassKeycase/keycase-python-sdk/releases/tag/v0.1.0b1
