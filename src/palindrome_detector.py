def contains_palindrome_word(input_string: str) -> bool:
    """
    Determine if the input string contains a palindrome word.
    
    A palindrome word is a word that reads the same backward as forward, 
    ignoring case and considering only alphanumeric characters.
    
    Args:
        input_string (str): A string containing words, numbers, and special characters
    
    Returns:
        bool: True if the string contains a palindrome word, False otherwise
    
    Examples:
        >>> contains_palindrome_word("Hello radar world")
        True
        >>> contains_palindrome_word("Not a palindrome")
        False
    """
    # Split the input string into words, removing special characters
    import re
    
    # Use regex to split words and remove non-alphanumeric characters
    words = re.findall(r'\b[a-zA-Z]+\b', input_string)
    
    # Check each word for palindrome property
    for word in words:
        # Convert to lowercase for case-insensitive comparison
        clean_word = word.lower()
        
        # Compare the word with its reverse
        if clean_word == clean_word[::-1]:
            return True
    
    return False