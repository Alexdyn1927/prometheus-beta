def to_alternating_case(text: str) -> str:
    """
    Convert a string to alternating sentence case.
    
    Args:
        text (str): The input string to be converted.
    
    Returns:
        str: A string with alternating capitalization.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_case("hello world")
        'Hello wOrLd'
        >>> to_alternating_case("")
        ''
        >>> to_alternating_case("a")
        'A'
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return text
    
    # Convert to alternating case
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(text)
    )