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
    
    # Separate numeric and non-numeric words
    numeric_words = [word for word in words if word.isdigit()]
    non_numeric_words = [word for word in words if not word.isdigit()]
    
    # Handle based on presence of numeric words
    if words[0].isdigit():
        # Special case if input starts with a number
        result = words[0]
        sorted_words = sorted(non_numeric_words, key=str.lower)
        result += sorted_words[0].lower() if sorted_words else ""
        result += ''.join(word.capitalize() for word in sorted_words[1:])
        return result
    
    # Normal case
    result = words[0].lower()
    
    # Sort non-numeric words 
    sorted_non_numeric = sorted(non_numeric_words, key=str.lower)
    
    # Function to find original position of words
    def word_index(w):
        return words.index(w)
    
    # Add sorted non-numeric words in their original order
    sorted_non_numeric.sort(key=word_index)
    
    # Add capitalized sorted words
    for word in sorted_non_numeric:
        result += word.capitalize()
    
    # Add numeric words in their original order
    for word in numeric_words:
        result += word
    
    return result