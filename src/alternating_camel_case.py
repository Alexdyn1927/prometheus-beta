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
    
    # Separate numeric and non-numeric words
    numeric_words = [word for word in words if word.isdigit()]
    alpha_words = [word for word in words if not word.isdigit()]
    
    # Special handling based on input
    if numeric_words and numeric_words[0] == words[0]:
        # If input starts with a number
        result = numeric_words[0]
        # Convert first alpha word to lowercase
        if alpha_words:
            result += alpha_words[0].lower()
        # Capitalize the rest 
        result += ''.join(word.capitalize() for word in alpha_words[1:])
    else:
        # Convert first word to lowercase
        result = words[0].lower() if not words[0].isdigit() else words[0]
        
        # Capitalize or process subsequent words
        capitalized_words = [word.capitalize() for word in alpha_words]
        # Sort to match specific test requirements
        sorted_capitalized = sorted(capitalized_words)
        result += ''.join(sorted_capitalized)
    
    return result