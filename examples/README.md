# Keycase Agent SDK - Examples

This folder contains example keyword implementations demonstrating how to use the Keycase Agent SDK.

## Files

| File | Description |
|------|-------------|
| `calculator.py` | Basic arithmetic operations (add, subtract, multiply, divide) |
| `string_operations.py` | String manipulation keywords (concat, upper, lower, etc.) |
| `advanced_examples.py` | Advanced features: choices, multiple outputs, auto-discovery |

## Usage

Load these examples in your code:

```python
from keycase_agent import load_keywords

# Load all examples
load_keywords('examples')
```

## Creating Your Own Keywords

1. Create a new Python file in your keywords folder
2. Import the decorators:
   ```python
   from keycase_agent import keyword, input_param, output_param
   ```
3. Define your keyword:
   ```python
   @keyword("My Keyword")
   @input_param("name", type="string", required=True, description="Your name")
   @output_param("greeting", type="string", description="Greeting message")
   def my_keyword(name: str) -> dict:
       return {"greeting": f"Hello, {name}!"}
   ```
4. Load your keywords folder:
   ```python
   load_keywords('path/to/your/keywords')
   ```

## Parameter Types

| Type | Status | Description |
|------|--------|-------------|
| `string` | **Supported** | Text values (default) |
| `number` | Phase 2 | Floating point numbers |
| `integer` | Phase 2 | Whole numbers |
| `boolean` | Phase 2 | True/False values |
| `object` | Phase 2 | JSON objects/dictionaries |
| `array` | Phase 2 | Lists |

> **Note:** Currently all parameters are treated as strings internally.
> Other types are accepted for documentation purposes and will be fully
> supported in a future release. See [ROADMAP.md](../ROADMAP.md) for details.

## Learn More

- [Main README](../README.md) - Complete documentation
- [ROADMAP.md](../ROADMAP.md) - Future development plans
