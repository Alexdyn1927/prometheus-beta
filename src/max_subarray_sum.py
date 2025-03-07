def find_max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This function uses Kadane's algorithm to efficiently find the maximum subarray sum.
    It works with arrays containing positive and negative integers.
    
    Args:
        arr (list): A list of integers to search for the maximum subarray sum.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> find_max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4])
        10
        >>> find_max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm for maximum subarray sum
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if the current max is larger
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far