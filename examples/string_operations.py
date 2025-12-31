"""String operation keywords - Example of text manipulation.

This module demonstrates keywords for common string operations,
showing how to use parameter annotations with different types.
"""

from keycase_agent import keyword, input_param, output_param


@keyword("String Concat")
@input_param("text1", type="string", required=True, description="First text")
@input_param("text2", type="string", required=True, description="Second text")
@input_param("separator", type="string", required=False, default=" ", description="Separator between texts")
@output_param("result", type="string", description="Concatenated string")
def string_concat(text1: str, text2: str, separator: str = " ") -> dict:
    """Concatenate two strings with an optional separator.

    Args:
        text1: First text
        text2: Second text
        separator: Separator between texts (default: space)

    Returns:
        Dictionary with 'result' containing concatenated string
    """
    result = f"{text1}{separator}{text2}"
    return {"result": result}


@keyword("String Upper")
@input_param("text", type="string", required=True, description="Text to convert")
@output_param("result", type="string", description="Uppercase text")
def string_upper(text: str) -> dict:
    """Convert text to uppercase.

    Args:
        text: Text to convert

    Returns:
        Dictionary with 'result' containing uppercase text
    """
    return {"result": str(text).upper()}


@keyword("String Lower")
@input_param("text", type="string", required=True, description="Text to convert")
@output_param("result", type="string", description="Lowercase text")
def string_lower(text: str) -> dict:
    """Convert text to lowercase.

    Args:
        text: Text to convert

    Returns:
        Dictionary with 'result' containing lowercase text
    """
    return {"result": str(text).lower()}


@keyword("String Length")
@input_param("text", type="string", required=True, description="Text to measure")
@output_param("length", type="string", description="Length of the text")
def string_length(text: str) -> dict:
    """Get the length of a string.

    Args:
        text: Text to measure

    Returns:
        Dictionary with 'length' containing the character count
    """
    return {"length": len(str(text))}


@keyword("String Contains")
@input_param("text", type="string", required=True, description="Text to search in")
@input_param("search", type="string", required=True, description="Text to search for")
@output_param("found", type="string", description="Whether search text was found (true/false)")
def string_contains(text: str, search: str) -> dict:
    """Check if a string contains another string.

    Args:
        text: Text to search in
        search: Text to search for

    Returns:
        Dictionary with 'found' boolean
    """
    return {"found": str(search) in str(text)}
