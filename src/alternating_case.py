def to_alternating_case(input_string):
    """
    Convert a string to alternating case (swapping between upper and lower case).

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A new string with alternating case.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is an empty string, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(input_string)
    )