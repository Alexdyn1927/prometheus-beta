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
    for i in range(1, len(numbers)):
        result[i] = result[i-1] * numbers[i-1]
    
    return result