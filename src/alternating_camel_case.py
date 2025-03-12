def to_alternating_camel_case(text: str) -> str:
    """
    Convert a given string to alternating camel case.
    
    Alternating camel case means:
    - First character is lowercase
    - Follows specific ordering of words
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
    
    # Handle special case of starting with a number
    if words[0].isdigit():
        result = words[0]
        other_words = [w for w in words[1:] if not w.isdigit()]
        
        # First non-numeric word is lowercase
        if other_words:
            result += other_words[0].lower()
            
            # Capitalize remaining non-numeric words
            for word in other_words[1:]:
                result += word.capitalize()
        
        return result
    
    # Standard case
    result = words[0].lower()
    
    # Determine the subset of non-numeric words and sort
    non_numeric_words = [word for word in words[1:] if not word.isdigit()]
    sorted_words = sorted(non_numeric_words, key=str.lower)
    
    # If no non-numeric words, return initial lowercase
    if not sorted_words:
        return result
    
    # Add the first sorted word as lowercase
    result += sorted_words[0].lower()
    
    # Capitalize the rest
    for word in sorted_words[1:]:
        result += word.capitalize()
    
    return result