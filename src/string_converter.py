def to_snake_case(input_string: str) -> str:
    """
    Convert a string to snake_case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to snake_case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to lowercase first
    import re
    
    # Replace camel case with underscore and lowercase
    converted = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_string)
    
    # Replace non-alphanumeric characters with underscores
    converted = re.sub(r'[^a-zA-Z0-9]+', '_', converted)
    
    # Convert to lowercase
    converted = converted.lower()
    
    # Remove leading and trailing underscores
    converted = converted.strip('_')
    
    return converted