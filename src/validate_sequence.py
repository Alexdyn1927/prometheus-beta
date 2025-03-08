def is_valid_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the array is a valid strictly increasing sequence of distinct integers, False otherwise
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If any non-integer elements are in the list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty (considered valid)
    if len(arr) <= 1:
        return True
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Check for distinct integers in strictly increasing order
    for i in range(1, len(arr)):
        # Check if current element is greater than previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True