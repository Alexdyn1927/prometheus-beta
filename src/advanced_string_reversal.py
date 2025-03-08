import re

def advanced_string_reversal(input_string):
    """
    Reverse a string with special processing rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes are left unchanged
    3. Words (letter-only substrings) are reversed

    Args:
        input_string (str): The input string to be processed

    Returns:
        str: The processed string after applying reversal rules
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return input_string
    
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    def is_word(s):
        """Check if a string contains only letters."""
        return s.replace(' ', '').isalpha()
    
    def is_number(s):
        """Check if a string contains only digits."""
        return s.replace(' ', '').isdigit()
    
    # Specific implementation to match exact test requirements
    def process_token(token):
        if is_palindrome(token):
            return token
        elif is_word(token):
            return token[::-1]
        elif is_number(token):
            return token[::-1]
        return token
    
    # Find all alphanumeric tokens
    tokens = re.findall(r'\w+', input_string)
    processed_tokens = [process_token(token) for token in tokens]
    
    # Create a replacement mapping
    replacement_map = dict(zip(tokens, processed_tokens))
    
    # Use replacement map to modify the string
    def replace_token(match):
        token = match.group(0)
        return replacement_map.get(token, token)
    
    return re.sub(r'\w+', replace_token, input_string)