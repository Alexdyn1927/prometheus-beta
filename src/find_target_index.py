def find_target_index(numbers: list[int], target: int) -> int:
    """
    Find the index of the first occurrence of a target value in a list of integers.
    
    Args:
        numbers (list[int]): The input list of integers to search through.
        target (int): The target value to find in the list.
    
    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found in the list.
    
    Examples:
        >>> find_target_index([1, 2, 3, 4, 5], 3)
        2
        >>> find_target_index([1, 2, 3, 4, 5], 6)
        -1
        >>> find_target_index([], 1)
        -1
    """
    # Iterate through the list with enumeration to get both index and value
    for index, value in enumerate(numbers):
        if value == target:
            return index
    
    # Return -1 if target is not found
    return -1