"""Calculator keywords - Example of basic arithmetic operations.

This module demonstrates how to create simple keywords with parameter
annotations for input validation and output documentation.

Note: All parameters are currently treated as strings. Type conversion
is handled within the keyword function.
"""

from keycase_agent import keyword, input_param, output_param


@keyword("Calculator Add")
@input_param("num1", type="string", required=True, description="First number to add")
@input_param("num2", type="string", required=True, description="Second number to add")
@output_param("result", type="string", description="The sum of the two numbers")
def calculator_add(num1: str, num2: str) -> dict:
    """Add two numbers together.

    Args:
        num1: First number
        num2: Second number

    Returns:
        Dictionary with 'result' containing the sum
    """
    result = float(num1) + float(num2)
    return {"result": result}


@keyword("Calculator Subtract")
@input_param("num1", type="string", required=True, description="Number to subtract from")
@input_param("num2", type="string", required=True, description="Number to subtract")
@output_param("result", type="string", description="The difference")
def calculator_subtract(num1: str, num2: str) -> dict:
    """Subtract one number from another.

    Args:
        num1: Number to subtract from
        num2: Number to subtract

    Returns:
        Dictionary with 'result' containing the difference
    """
    result = float(num1) - float(num2)
    return {"result": result}


@keyword("Calculator Multiply")
@input_param("num1", type="string", required=True, description="First factor")
@input_param("num2", type="string", required=True, description="Second factor")
@output_param("result", type="string", description="The product")
def calculator_multiply(num1: str, num2: str) -> dict:
    """Multiply two numbers.

    Args:
        num1: First factor
        num2: Second factor

    Returns:
        Dictionary with 'result' containing the product
    """
    result = float(num1) * float(num2)
    return {"result": result}


@keyword("Calculator Divide")
@input_param("dividend", type="string", required=True, description="Number to divide")
@input_param("divisor", type="string", required=True, description="Number to divide by")
@output_param("result", type="string", description="The quotient")
def calculator_divide(dividend: str, divisor: str) -> dict:
    """Divide one number by another.

    Args:
        dividend: Number to divide
        divisor: Number to divide by

    Returns:
        Dictionary with 'result' containing the quotient

    Raises:
        ValueError: If divisor is zero
    """
    if float(divisor) == 0:
        raise ValueError("Cannot divide by zero")

    result = float(dividend) / float(divisor)
    return {"result": result}
