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
    
    # Convert to lowercase first
    normalized = input_string.lower()
    
    # Replace various separators with hyphens
    normalized = normalized.replace('_', '-').replace(' ', '-')
    
    # Handle camelCase or PascalCase
    # Use regex-like replacement to insert hyphens before capital letters
    chars = []
    for i, char in enumerate(normalized):
        if i > 0 and char.isalpha() and char.isupper():
            chars.append('-')
        chars.append(char.lower())
    
    # Remove consecutive hyphens and trim any leading/trailing hyphens
    result = ''.join(chars).replace('--', '-').strip('-')
    
    return result