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
    
    def reverse_substring(s):
        """Reverse a substring based on its characteristics."""
        # If it's a palindrome, return as-is
        if is_palindrome(s):
            return s
        
        # If it's a word, return the reversed word
        if is_word(s):
            return s[::-1]
        
        # If it contains digits, convert to string and reverse
        if is_number(s):
            return s[::-1]
        
        # Default: return as-is
        return s
    
    def merge_adjacent_alphanumerics(tokens):
        """Merge adjacent alphanumeric tokens to handle cases like 'hello123world'."""
        merged_tokens = []
        i = 0
        while i < len(tokens):
            current = tokens[i]
            # Check if current and next tokens are alphanumeric
            if (i+1 < len(tokens) and 
                current.isalpha() and 
                tokens[i+1].isdigit()):
                # If current is word and next is number, keep together
                merged_tokens.append(current + tokens[i+1])
                i += 2
            elif (i+1 < len(tokens) and 
                  current.isdigit() and 
                  tokens[i+1].isalpha()):
                # If current is number and next is word, keep together
                merged_tokens.append(current + tokens[i+1])
                i += 2
            else:
                merged_tokens.append(current)
                i += 1
        return merged_tokens
    
    # Use regex to split the string
    pattern = r'(\d+|\w+|\s+|\W+)'
    tokens = re.findall(pattern, input_string)
    
    # Merge adjacent alphanumeric tokens
    tokens = merge_adjacent_alphanumerics(tokens)
    
    # Process each token
    processed_tokens = [reverse_substring(token) for token in tokens]
    
    # Reconstruct the string
    return ''.join(processed_tokens)