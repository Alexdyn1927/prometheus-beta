import re

def to_kebab_case(input_string):
    """
    Convert a given string to kebab-case.
    
    Kebab case is a naming convention where words are lowercase and separated by hyphens.
    
    Args:
        input_string (str): The input string to convert to kebab case.
    
    Returns:
        str: The input string converted to kebab case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("snake_case_string")
        'snake-case-string'
        >>> to_kebab_case("camelCaseString")
        'camel-case-string'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace various separators with spaces first
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Use regex to split camel case and handle consecutive uppercase
    # This breaks the string at points where a lowercase letter is followed by an uppercase letter
    # or where multiple uppercase letters exist
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', normalized)
    
    # Convert to lowercase and join with hyphens
    return '-'.join(word.lower() for word in words).strip('-')