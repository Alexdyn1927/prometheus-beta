def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.

    Args:
        strings (list): A list of strings to compare.

    Returns:
        str: The longest common suffix. If no common suffix exists,
             returns an empty string.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the input list is empty.
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit suffix checks
    shortest = min(strings, key=len)
    
    # Check suffixes from longest possible to shortest
    for i in range(len(shortest), 0, -1):
        # Take suffix of current length from the end of the shortest string
        current_suffix = shortest[-i:]
        
        # Check if this suffix is common to all strings
        if all(s.endswith(current_suffix) for s in strings):
            return current_suffix
    
    # If no common suffix found
    return ""