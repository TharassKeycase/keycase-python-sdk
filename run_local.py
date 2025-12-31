#!/usr/bin/env python
"""
Standalone script to run KeyCase execution plans locally without WebSocket.

Usage:
    python run_local.py <execution_plan.json>
    
Example:
    python run_local.py keycase_agent/test-data/execution-plan-sample-report.json
"""

import json
import sys
import argparse
import logging
from pathlib import Path

from keycase_agent.execution_manager import ExecutionManager
from keycase_agent.loader import load_keywords

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_execution_plan(file_path):
    """Load execution plan from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def print_results(results):
    """Pretty print execution results."""
    print("\n" + "="*60)
    print("EXECUTION RESULTS")
    print("="*60)
    
    if 'result' in results:
        result = results['result']
        print(f"Run ID: {result.get('runId', 'N/A')}")
        print(f"Status: {'SUCCESS' if not any(f.get('status') == 'FAILED' for f in result.get('flowResults', [])) else 'FAILED'}")
        print(f"Start Time: {result.get('startDateTime', 'N/A')}")
        print(f"End Time: {result.get('endDateTime', 'N/A')}")
        
        print("\nFlow Results:")
        print("-"*40)
        for flow in result.get('flowResults', []):
            status_icon = "[PASS]" if flow.get('status') == 'PASSED' else "[FAIL]"
            print(f"{status_icon} Flow: {flow.get('name')} - {flow.get('status')}")
            if flow.get('message'):
                print(f"  Message: {flow.get('message')}")
            if flow.get('failedOnStepId'):
                print(f"  Failed on step: {flow.get('failedOnStepId')}")
    
    print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Run KeyCase execution plans locally'
    )
    parser.add_argument(
        'plan_file',
        help='Path to execution plan JSON file'
    )
    parser.add_argument(
        '--project-id',
        default='local',
        help='Project ID (default: local)'
    )
    parser.add_argument(
        '--run-id',
        help='Run ID (auto-generated if not provided)'
    )
    parser.add_argument(
        '--keywords-dir',
        default='examples',
        help='Path to keywords directory (default: examples)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Check if file exists
    plan_path = Path(args.plan_file)
    if not plan_path.exists():
        print(f"Error: File not found: {args.plan_file}")
        sys.exit(1)
    
    try:
        # Load keywords
        logger.info(f"Loading keywords from {args.keywords_dir}")
        load_keywords(args.keywords_dir)
        
        # Load execution plan
        logger.info(f"Loading execution plan from {args.plan_file}")
        execution_plan = load_execution_plan(args.plan_file)
        
        # Create execution manager in local mode
        logger.info("Creating ExecutionManager in local mode")
        manager = ExecutionManager(mode='local')
        
        # Execute the plan
        print(f"\nExecuting plan: {execution_plan.get('name', 'Unnamed')}")
        print(f"Run ID: {execution_plan.get('runId', args.run_id or 'auto-generated')}")
        print("-"*40)
        
        # Use runId from plan if available, otherwise use provided or auto-generate
        run_id = args.run_id or execution_plan.get('runId')
        
        results = manager.execute_local(
            execution_plan,
            project_id=args.project_id,
            run_id=run_id
        )
        
        # Print results
        print_results(results)
        
        # Save results to file
        output_file = plan_path.stem + '_results.json'
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to: {output_file}")
        
    except Exception as e:
        logger.error(f"Execution failed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()