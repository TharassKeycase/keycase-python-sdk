#!/usr/bin/env python
"""
Example of using KeyCase ExecutionManager as a library for local execution.
"""

import json
from keycase_agent import ExecutionManager, load_keywords


def main():
    # Load keywords from the examples directory
    load_keywords('examples')
    
    # Create a simple execution plan
    execution_plan = {
        "version": 1,
        "name": "Simple Calculator Test",
        "runId": 123,
        "keywordInstances": [
            {
                "id": 1,
                "name": "add_numbers",
                "keywordName": "calculator_postman",
                "keywordId": 1,
                "params": [
                    {
                        "id": 1,
                        "name": "num1",
                        "direction": "INPUT",
                        "type": "TEXT",
                        "isMandatory": False,
                        "value": "5"
                    },
                    {
                        "id": 2,
                        "name": "num2",
                        "direction": "INPUT",
                        "type": "TEXT",
                        "isMandatory": False,
                        "value": "3"
                    },
                    {
                        "id": 3,
                        "name": "return_sum",
                        "direction": "OUTPUT",
                        "type": "TEXT",
                        "isMandatory": False,
                        "value": ""
                    }
                ]
            },
            {
                "id": 2,
                "name": "validate_sum",
                "keywordName": "calc_validation",
                "keywordId": 2,
                "params": [
                    {
                        "id": 4,
                        "name": "incoming_sum",
                        "direction": "INPUT",
                        "type": "TEXT",
                        "isMandatory": True,
                        "value": ""
                    },
                    {
                        "id": 5,
                        "name": "validation",
                        "direction": "INPUT",
                        "type": "TEXT",
                        "isMandatory": False,
                        "value": "8"
                    }
                ]
            }
        ],
        "flows": [
            {
                "id": 1,
                "flowId": 1,
                "sequenceOrder": 1,
                "runMode": "default",
                "name": "Calculate and Validate",
                "description": "Add two numbers and validate the result",
                "steps": [
                    {
                        "id": 1,
                        "instanceId": 1,
                        "sequenceOrder": 0
                    },
                    {
                        "id": 2,
                        "instanceId": 2,
                        "sequenceOrder": 1
                    }
                ],
                "connections": [
                    {
                        "id": 1,
                        "fromStepId": 1,
                        "toStepId": 2,
                        "fromParamId": 3,
                        "toParamId": 4
                    }
                ]
            }
        ]
    }
    
    # Create ExecutionManager in local mode
    manager = ExecutionManager(mode='local')
    
    # Execute the plan
    print("Executing plan locally...")
    results = manager.execute_local(
        execution_plan,
        project_id="example",
        run_id="test-run-1"
    )
    
    # Print results
    print("\nExecution Results:")
    print(json.dumps(results, indent=2))
    
    # Check if execution was successful
    if results and 'result' in results:
        flow_results = results['result'].get('flowResults', [])
        if flow_results:
            status = flow_results[0].get('status')
            if status == 'PASSED':
                print("\n[SUCCESS] Execution completed successfully!")
            else:
                print(f"\n[FAILED] Execution failed with status: {status}")
                if flow_results[0].get('message'):
                    print(f"  Error: {flow_results[0]['message']}")


if __name__ == "__main__":
    main()