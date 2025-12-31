# Local Execution Mode

The KeyCase Agent now supports local execution of test plans without requiring WebSocket connections. This allows you to:

1. Run execution plans directly from JSON files
2. Use the ExecutionManager as a standalone library
3. Test keyword implementations locally
4. Integrate with other tools and frameworks

## Quick Start

### Command Line Usage

Run an execution plan from a JSON file:

```bash
python run_local.py keycase_agent/test-data/execution-plan-sample-report.json
```

Options:
- `--project-id`: Project ID (default: "local")
- `--run-id`: Run ID (auto-generated if not provided)
- `--keywords-dir`: Path to keywords directory (default: keycase_agent/keywords)
- `--verbose`: Enable verbose logging

### Library Usage

```python
from keycase_agent import ExecutionManager, load_keywords

# Load keywords
load_keywords('keycase_agent/keywords')

# Create manager in local mode
manager = ExecutionManager(mode='local')

# Execute plan (can be dict or JSON string)
results = manager.execute_local(
    execution_plan,
    project_id="my-project",
    run_id="run-123"
)

# Process results
print(results)
```

## ExecutionManager Modes

The ExecutionManager now supports two modes:

### WebSocket Mode (default)
```python
# For use with WebSocket connections
manager = ExecutionManager(
    send_result_callback=my_callback,
    update_status_callback=my_status_callback,
    mode='websocket'
)
```

### Local Mode
```python
# For standalone/local execution
manager = ExecutionManager(mode='local')
```

## Creating Keywords

Keywords are Python functions decorated with `@keyword`. The decorator supports optional custom naming:

### Using Function Name (Default)
```python
from keycase_agent.decorators import keyword

@keyword
def my_keyword(param1=None, param2=None):
    """Keyword registered as 'my_keyword'."""
    result = param1 + param2
    return {"output": result}
```

### Using Custom User-Friendly Name
```python
@keyword("User Friendly Name")
def technical_function_name(param1=None, param2=None):
    """Keyword registered as 'User Friendly Name'."""
    # Technical implementation
    return {"output": result}
```

### Decorator Usage Patterns
- `@keyword` - Uses function name as keyword name
- `@keyword()` - Same as `@keyword`, uses function name
- `@keyword("CustomName")` - Uses custom name for the keyword

This allows you to:
- Keep technical function names for code clarity
- Provide user-friendly keyword names in execution plans
- Maintain backward compatibility with existing keywords

Place keyword files in the `keycase_agent/keywords/` directory and they will be auto-loaded.

## Execution Plan Format

Execution plans are JSON files with the following structure:

```json
{
  "version": 1,
  "name": "Test Plan Name",
  "runId": 123,
  "keywordInstances": [
    {
      "id": 1,
      "keywordName": "my_keyword",
      "params": [
        {
          "id": 1,
          "name": "param1",
          "direction": "INPUT",
          "value": "test"
        },
        {
          "id": 2,
          "name": "output",
          "direction": "OUTPUT"
        }
      ]
    }
  ],
  "flows": [
    {
      "id": 1,
      "name": "Test Flow",
      "steps": [
        {
          "id": 1,
          "instanceId": 1,
          "sequenceOrder": 0
        }
      ],
      "connections": []
    }
  ]
}
```

## Example Scripts

- `run_local.py`: Command-line tool for running execution plans
- `example_local_usage.py`: Example of using ExecutionManager as a library

## Output

Results are returned as a dictionary containing:
- `project_id`: The project ID
- `run_id`: The run ID
- `result`: Execution results including:
  - `startDateTime`: Execution start time
  - `endDateTime`: Execution end time
  - `flowResults`: Array of flow execution results with status (PASSED/FAILED/ABORTED)

Results are also saved to a JSON file named `{input_file}_results.json`.