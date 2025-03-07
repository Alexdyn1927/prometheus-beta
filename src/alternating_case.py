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
        'HeLlO wOrLd'
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
    
    # Iterate through characters keeping track of letter index
    result = []
    letter_index = 0
    
    for char in text:
        if char.isalpha():
            # Alternate case for letters
            result.append(char.upper() if letter_index % 2 == 0 else char.lower())
            letter_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)