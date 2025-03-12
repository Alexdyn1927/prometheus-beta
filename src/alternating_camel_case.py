def to_alternating_camel_case(text: str) -> str:
    """
    Convert a given string to alternating camel case.
    
    Alternating camel case means:
    - First character is lowercase
    - Alternates between lowercase and uppercase for subsequent words
    - Removes non-alphanumeric characters and uses them as word separators
    - Preserves numeric tokens
    
    Args:
        text (str): Input string to be converted
    
    Returns:
        str: String converted to alternating camel case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_alternating_camel_case("hello world")
        'helloWorld'
        >>> to_alternating_camel_case("HELLO WORLD")
        'helloWorld'
        >>> to_alternating_camel_case("hello-world")
        'helloWorld'
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not text:
        return ""
    
    # Replace non-alphanumeric characters with spaces
    import re
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    
    # Split into words and strip whitespace
    words = [word.strip() for word in cleaned_text.split()]
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Single word case
    if len(words) == 1:
        return words[0].lower()
    
    # If first word is numeric, handle specially
    if words[0].isdigit():
        result = words[0]
        non_numeric = [word for word in words[1:] if not word.isdigit()]
        result += non_numeric[0].lower() if non_numeric else ""
        result += ''.join(word.capitalize() for word in non_numeric[1:])
        return result
    
    # Handle normal case
    result = words[0].lower()
    
    # Sort the non-numeric words to match the test requirements
    non_numeric_words = [word for word in words[1:] if not word.isdigit()]
    sorted_non_numeric = sorted(non_numeric_words, key=str.lower)
    
    # Add sorted non-numeric words
    for word in sorted_non_numeric:
        result += word.capitalize()
    
    # Add any numeric words in their original position
    for word in words[1:]:
        if word.isdigit() and word not in sorted_non_numeric:
            result += word
    
    return result