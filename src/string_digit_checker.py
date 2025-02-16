def is_digit_string(input_string: str) -> bool:
    """
    Check if a given string contains only digits.
    
    Args:
        input_string (str): The string to check.
    
    Returns:
        bool: True if the string contains only digits, False otherwise.
    """
    # Handle None or empty string cases
    if input_string is None or len(input_string) == 0:
        return False
    
    # Use built-in method to check if all characters are digits
    return input_string.isdigit()