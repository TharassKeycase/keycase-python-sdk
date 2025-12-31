# Keycase Agent SDK - Roadmap

This document outlines the development roadmap for the Keycase Agent SDK.

## Current Version: 0.1.0

### Supported Features

- WebSocket and Local execution modes
- `@keyword` decorator for registering keywords
- `@param`, `@input_param`, `@output_param` decorators for parameter metadata
- Parameter validation (name matching, required parameters)
- Automatic reconnection with exponential backoff
- Token refresh management
- Execution hooks (`@BeforeRun`, `@AfterRun`)

### Parameter Types

Currently, all parameters are treated as **string/text** values internally.
Type annotations are accepted for documentation purposes but not enforced at runtime.

| Type | Status | Notes |
|------|--------|-------|
| `string` | Supported | Default type, fully functional |
| `number` | Phase 2 | Accepted but treated as string |
| `integer` | Phase 2 | Accepted but treated as string |
| `boolean` | Phase 2 | Accepted but treated as string |
| `object` | Phase 2 | Accepted but treated as string |
| `array` | Phase 2 | Accepted but treated as string |

---

## Phase 2: Type System Enhancement

### Planned Features

- [ ] **Runtime type validation** - Validate parameter values match declared types
- [ ] **Automatic type conversion** - Convert strings to numbers, booleans, etc.
- [ ] **Type coercion** - Smart conversion with error handling
- [ ] **Schema validation** - Validate object/array structures
- [ ] **Custom type validators** - User-defined validation functions

### Example (Future)

```python
@keyword("Calculate")
@input_param("value", type="number", required=True)  # Will validate as number
@input_param("enabled", type="boolean")              # Will convert "true"/"false"
def calculate(value: float, enabled: bool) -> dict:
    # value will be guaranteed to be a float
    # enabled will be guaranteed to be a bool
    pass
```

---

## Phase 3: Advanced Features

### Planned Features

- [ ] **Async keyword support** - `async def` keywords
- [ ] **Parallel step execution** - Run independent steps concurrently
- [ ] **Conditional flows** - If/else branching in flows
- [ ] **Loop support** - Repeat steps with iteration
- [ ] **Sub-flows** - Nested flow execution
- [ ] **Built-in keywords library** - Common operations (HTTP, file, etc.)

---

## Phase 4: Developer Experience

### Planned Features

- [ ] **CLI tool** - `keycase init`, `keycase validate`, `keycase run`
- [ ] **Keyword scaffolding** - Generate keyword templates
- [ ] **Schema export** - Export keyword schemas as JSON/OpenAPI
- [ ] **VS Code extension** - Syntax highlighting, autocomplete
- [ ] **Documentation generator** - Auto-generate docs from keywords

---

## Contributing

We welcome contributions! If you'd like to help implement any of these features,
please open an issue or pull request on GitHub.

## Feedback

Have suggestions for the roadmap? Open an issue on GitHub or contact us.
