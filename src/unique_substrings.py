def find_unique_substrings(input_string):
    """
    Find all unique substrings within the given input string.

    Args:
        input_string (str): The input string to find substrings from.

    Returns:
        list: A list of unique substrings, including empty string and full string.

    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty list
    if not input_string:
        return []
    
    # Use a set to store unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(input_string) + 1):
        for end in range(start, len(input_string) + 1):
            unique_substrings.add(input_string[start:end])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))