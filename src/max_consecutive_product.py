def find_max_consecutive_product(arr):
    """
    Find the maximum product of any three consecutive elements in the array.

    Args:
        arr (list): A list of integers, can include positive, negative, and zero values.
    
    Returns:
        int or float: The maximum absolute product of three consecutive elements.
    
    Raises:
        ValueError: If the input array has fewer than 3 elements.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check if array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    # Track potential max products with different approaches
    possible_max_products = set()
    
    # Check first three elements
    possible_max_products.add(abs(arr[0] * arr[1] * arr[2]))
    
    # Iterate through the array to find maximum product
    for i in range(1, len(arr) - 2):
        # Calculate consecutive products
        # Regular consecutive multiplication
        possible_max_products.add(abs(arr[i] * arr[i+1] * arr[i+2]))
        # Consider potential sign variations
        possible_max_products.add(abs(arr[i] * arr[i+1]) * arr[i+2])
        possible_max_products.add(arr[i] * abs(arr[i+1] * arr[i+2]))
        possible_max_products.add(abs(arr[i]) * abs(arr[i+1]) * arr[i+2])
    
    # Return the maximum product found
    return max(possible_max_products)