def longest_subarray_diff(A, k):
    """
    Find the length of the longest subarray where the absolute difference 
    between adjacent elements is greater than or equal to k.

    Args:
        A (list): Input array of integers
        k (int): Minimum absolute difference between adjacent elements

    Returns:
        int: Length of the longest valid subarray
    
    Raises:
        ValueError: If input array is empty or k is negative
    """
    # Validate input
    if not A:
        raise ValueError("Input array cannot be empty")
    if k < 0:
        raise ValueError("k must be non-negative")
    
    # If array has only one element, return 1
    if len(A) == 1:
        return 1
    
    # Initialize variables for sliding window
    max_length = 1
    start = 0
    
    # Iterate through the array
    for end in range(1, len(A)):
        # If the condition is violated, move the start pointer
        while start < end and abs(A[end] - A[end-1]) < k:
            start = end
        
        # Update maximum length
        current_length = end - start + 1
        max_length = max(max_length, current_length)
    
    return max_length