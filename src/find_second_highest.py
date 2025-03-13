def find_second_highest(nums):
    """
    Find the second highest value in a sorted list of integers.

    Args:
        nums (list): A sorted list of integers.

    Returns:
        int or None: The second highest value in the list, 
                     or None if the list has fewer than 2 unique elements.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Check for invalid input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if len(nums) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Remove duplicates while preserving order (which should be sorted)
    unique_nums = list(dict.fromkeys(nums))
    
    # Check if there are at least 2 unique elements
    if len(unique_nums) < 2:
        return None
    
    # Return the second to last element (second highest)
    return unique_nums[-2]