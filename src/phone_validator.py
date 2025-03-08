import re

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate a phone number against three specific formats:
    1. (123) 456-7890
    2. 123-456-7890
    3. 123 456 7890

    Args:
        phone_number (str): The phone number to validate

    Returns:
        bool: True if the phone number matches one of the valid formats, False otherwise
    """
    # Regular expression to match the three specified phone number formats
    phone_patterns = [
        r'^\(\d{3}\)\s\d{3}-\d{4}$',     # (123) 456-7890
        r'^\d{3}-\d{3}-\d{4}$',           # 123-456-7890
        r'^\d{3}\s\d{3}\s\d{4}$'          # 123 456 7890
    ]
    
    # Remove any whitespace from the input
    cleaned_phone = phone_number.strip()
    
    # Check if the cleaned phone number matches any of the valid patterns
    return any(re.match(pattern, cleaned_phone) for pattern in phone_patterns)