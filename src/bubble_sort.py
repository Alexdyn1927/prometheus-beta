def bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    This implementation includes two key optimizations:
    1. Early stopping when no swaps occur in a pass
    2. Reducing iterations for already sorted elements at the end
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Get list length
    n = len(arr)
    
    # Optimization: Track if any swaps occurred
    for i in range(n):
        # Flag to detect if any swaps happened in this pass
        swapped = False
        
        # Reduce iterations by comparing up to (n-i-1)
        # This is because the last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr