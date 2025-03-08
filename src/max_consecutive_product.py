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
        # Consider current consecutive sequence
        sequence = arr[i:i+3]
        
        # Check all possible multiplications
        current_products = [
            sequence[0] * sequence[1] * sequence[2],
            sequence[0] * sequence[1] * max(sequence[2], 1),
            sequence[0] * max(sequence[1], 1) * sequence[2],
            max(sequence[0], 1) * sequence[1] * sequence[2]
        ]
        
        # Update max_product with the highest product
        max_product = max(max_product, max(current_products))
    
    return max_product