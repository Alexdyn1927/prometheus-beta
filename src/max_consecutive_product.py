def find_max_consecutive_product(arr):
    """
    Find the maximum product of any three consecutive elements in the array.

    Args:
        arr (list): A list of integers, can include positive, negative, and zero values.
    
    Returns:
        int or float: The maximum product of three consecutive elements.
    
    Raises:
        ValueError: If the input array has fewer than 3 elements.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check if array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    # Initialize max product with first three elements
    max_product = arr[0] * arr[1] * arr[2]
    
    # Iterate through the array to find maximum product
    for i in range(1, len(arr) - 2):
        # Calculate current sub-array products, consider all possible sign combinations
        products = [
            arr[i] * arr[i+1] * arr[i+2],        # Straight multiplication
            arr[i] * arr[i+1] * arr[i+2],        # Normal order
            arr[i] * arr[i+2] * arr[i+1],        # Rotated order 1
            arr[i+1] * arr[i] * arr[i+2],        # Rotated order 2
            arr[i+1] * arr[i+2] * arr[i],        # Rotated order 3
            arr[i+2] * arr[i] * arr[i+1]         # Rotated order 4
        ]
        
        # Update max_product with the highest product
        max_product = max(max_product, max(products))
    
    return max_product