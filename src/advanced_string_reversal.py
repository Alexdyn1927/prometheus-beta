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
    
    # Split into tokens, but preserve the entire mixed string
    pattern = r'(\d+|\w+)'
    tokens = re.findall(pattern, input_string)
    
    # Process tokens
    processed_tokens = []
    for token in tokens:
        if is_palindrome(token):
            # Palindromes: left unchanged
            processed_tokens.append(token)
        elif is_word(token):
            # Words: strictly reversed
            processed_tokens.append(token[::-1])
        elif is_number(token):
            # Numbers: strictly reversed
            processed_tokens.append(token[::-1])
        else:
            processed_tokens.append(token)
    
    # Reconstruct the string, replacing extracted tokens
    def token_replacer(match):
        token = match.group(1)
        if processed_tokens:
            return processed_tokens.pop(0)
        return token
    
    return re.sub(pattern, token_replacer, input_string)