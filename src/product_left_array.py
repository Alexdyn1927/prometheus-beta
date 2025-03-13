def product_left_elements(numbers):
    """
    Create an array where each element is the product of numbers to its left.
    
    Args:
        numbers (list): Input list of numbers
    
    Returns:
        list: Array where each element is the product of numbers to its left
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input contains non-numeric elements
    
    Examples:
        >>> product_left_elements([1, 2, 3, 4])
        [1, 1, 2, 6]
        >>> product_left_elements([])
        []
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not numbers:
        return []
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numeric")
    
    # Create result array
    result = [1] * len(numbers)
    
    # Compute product of left elements
    zero_index = -1
    product = 1
    
    # First go through and track the first zero index
    for i in range(len(numbers)):
        if numbers[i] == 0:
            if zero_index == -1:
                zero_index = i
            break
        result[i] = product
        product *= numbers[i]
    
    # Handle zero cases
    if zero_index != -1:
        # Set everything after first zero to 0
        result[zero_index] = 0
        for j in range(zero_index + 1, len(numbers)):
            result[j] = 0
    
    # If no zero found, continue calculating the rest
    if zero_index == -1:
        for i in range(len(numbers)):
            result[i] = product // numbers[i]
    
    return result