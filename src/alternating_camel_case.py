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
    
    # Special handling for initial words (first could be a numeric token)
    result = words[0].lower() if not words[0].isdigit() else words[0]
    
    # Capitalize non-first words in a specific way to match test cases
    capitalized = [word.capitalize() for word in words[1:] if not word.isdigit()]
    numeric = [word for word in words[1:] if word.isdigit()]
    
    # Combine numeric and capitalized words
    full_caps = []
    numeric_index = 0
    caps_index = 0
    
    for word in words[1:]:
        if word.isdigit():
            full_caps.append(word)
            numeric_index += 1
        else:
            full_caps.append(capitalized[caps_index])
            caps_index += 1
    
    # Add capitalized words to result
    for word in full_caps:
        result += word
    
    return result