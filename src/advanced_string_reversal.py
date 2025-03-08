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
        return s.isalpha()
    
    def is_number(s):
        """Check if a string contains only digits."""
        return s.isdigit()
    
    def reverse_substring(s):
        """Reverse a substring based on its characteristics."""
        # If it's a palindrome, return as-is
        if is_palindrome(s):
            return s
        
        # If it's a word, reverse the individual word
        if is_word(s):
            return s[::-1]
        
        # If it contains digits, convert to string and reverse
        if is_number(s):
            return s[::-1]
        
        # Default: return as-is
        return s
    
    # Split the string into substrings while preserving separators
    def custom_split(s):
        parts = []
        current_part = ""
        last_type = None
        
        for char in s:
            current_type = 'word' if char.isalpha() else ('digit' if char.isdigit() else 'other')
            
            # If the type changes, add the current part to parts
            if last_type is not None and current_type != last_type:
                if current_part:
                    parts.append(current_part)
                current_part = ""
            
            # Add the character to the current part
            current_part += char
            last_type = current_type
        
        # Add the last part
        if current_part:
            parts.append(current_part)
        
        return parts
    
    # Split the string
    substrings = custom_split(input_string)
    
    # Process each substring
    processed_substrings = [reverse_substring(substr) for substr in substrings]
    
    # Reconstruct the string
    return ''.join(processed_substrings)