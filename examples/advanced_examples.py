"""Advanced keyword examples - Demonstrating decorator features.

This module shows advanced usage of the @keyword, @param, @input_param,
and @output_param decorators including:
- Parameter choices (dropdowns)
- Multiple outputs
- Auto-discovered parameters
- Required vs optional parameters

Note: Currently all parameters are treated as strings. Other types shown
in comments are planned for Phase 2. See ROADMAP.md for details.
"""

from keycase_agent import (
    keyword,
    param,
    input_param,
    output_param,
    get_keyword_schema,
)


# =============================================================================
# Example 1: Parameter with choices (rendered as dropdown in UI)
# =============================================================================

@keyword("Set Priority")
@input_param(
    "priority",
    type="string",
    required=True,
    description="Priority level",
    choices=["LOW", "MEDIUM", "HIGH", "CRITICAL"]
)
@output_param("message", type="string", description="Confirmation message")
def set_priority(priority: str) -> dict:
    """Set a priority level from predefined choices.

    The 'choices' parameter creates a dropdown in the UI.
    """
    return {"message": f"Priority set to: {priority}"}


# =============================================================================
# Example 2: Multiple outputs
# =============================================================================

@keyword("Get User Info")
@input_param("user_id", type="string", required=True, description="User identifier")
@output_param("username", type="string", description="User's name")
@output_param("email", type="string", description="User's email")
@output_param("active", type="string", description="Account status (true/false)")
def get_user_info(user_id: str) -> dict:
    """Retrieve user information - demonstrates multiple outputs.

    Each output can be connected to inputs of subsequent keywords.
    """
    return {
        "username": f"user_{user_id}",
        "email": f"user_{user_id}@example.com",
        "active": "true"
    }


# =============================================================================
# Example 3: Required vs Optional parameters
# =============================================================================

@keyword("Send Message")
@input_param("recipient", type="string", required=True, description="Recipient address")
@input_param("message", type="string", required=True, description="Message content")
@input_param("subject", type="string", required=False, default="No Subject", description="Optional subject")
@input_param("priority", type="string", required=False, default="NORMAL", description="Optional priority")
@output_param("status", type="string", description="Send status")
@output_param("message_id", type="string", description="Generated message ID")
def send_message(recipient: str, message: str, subject: str = "No Subject", priority: str = "NORMAL") -> dict:
    """Send a message with required and optional parameters.

    Required parameters must be provided; optional parameters have defaults.
    """
    import hashlib
    msg_id = hashlib.md5(f"{recipient}{message}".encode()).hexdigest()[:8]
    return {
        "status": "sent",
        "message_id": f"MSG-{msg_id.upper()}"
    }


# =============================================================================
# Example 4: Auto-discovered parameters (no @param decorators needed)
# =============================================================================

@keyword("Quick Calculation")
def quick_calculation(a: str, b: str, operation: str = "add") -> dict:
    """Perform a calculation with auto-discovered parameters.

    Parameters are automatically inferred from the function signature:
    - 'a' and 'b' are required (no default value)
    - 'operation' is optional with default "add"
    """
    num_a = float(a)
    num_b = float(b)

    if operation == "add":
        result = num_a + num_b
    elif operation == "subtract":
        result = num_a - num_b
    elif operation == "multiply":
        result = num_a * num_b
    else:
        result = num_a + num_b

    return {"result": str(result)}


# =============================================================================
# Example 5: Validation keyword
# =============================================================================

@keyword("Validate Range")
@input_param("value", type="string", required=True, description="Value to validate")
@input_param("min_value", type="string", required=True, description="Minimum allowed value")
@input_param("max_value", type="string", required=True, description="Maximum allowed value")
@output_param("valid", type="string", description="Whether value is in range (true/false)")
@output_param("message", type="string", description="Validation message")
def validate_range(value: str, min_value: str, max_value: str) -> dict:
    """Validate that a value falls within a specified range."""
    val = float(value)
    min_val = float(min_value)
    max_val = float(max_value)

    is_valid = min_val <= val <= max_val

    if is_valid:
        message = f"Value {val} is within range [{min_val}, {max_val}]"
    else:
        message = f"Value {val} is outside range [{min_val}, {max_val}]"

    return {
        "valid": str(is_valid).lower(),
        "message": message
    }


# =============================================================================
# Utility: View schema (run this file directly)
# =============================================================================

if __name__ == "__main__":
    import json

    print("=" * 60)
    print("Keyword Schemas")
    print("=" * 60)

    keywords = [
        set_priority,
        get_user_info,
        send_message,
        quick_calculation,
        validate_range,
    ]

    for kw in keywords:
        schema = get_keyword_schema(kw)
        print(f"\n{schema['name']}:")
        print(json.dumps(schema, indent=2))
