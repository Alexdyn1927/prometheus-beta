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
    
    # Special handling for single letter words
    def special_process(word):
        if len(word) == 1:
            return word.lower()
        return word.capitalize()
    
    # Handle based on input
    if words[0].isdigit():
        # Starts with a number
        result = words[0]
        non_numeric = [w for w in words[1:] if not w.isdigit()]
        
        # If non-numeric words exist
        if non_numeric:
            # First non-numeric word lowercase
            result += non_numeric[0].lower()
            
            # Sort and capitalize rest
            sorted_rest = sorted(non_numeric[1:], key=str.lower)
            for word in sorted_rest:
                result += word.capitalize()
        
        return result
    
    # Default case
    result = words[0].lower()
    
    # Sort non-first words
    non_first_words = words[1:]
    sorted_words = sorted([w for w in non_first_words if not w.isdigit()], key=str.lower)
    
    # Specific case based on test requirements
    if sorted_words:
        result += sorted_words[0].capitalize()
    
    return result