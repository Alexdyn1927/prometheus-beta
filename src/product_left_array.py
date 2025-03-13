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
    
    # Special case handling
    if 0 in numbers:
        zero_index = numbers.index(0)
        result[zero_index] = 0
        for i in range(zero_index + 1, len(numbers)):
            result[i] = 0
        return result
    
    # Compute product of left elements 
    def signed_product(nums, index):
        """Compute signed product of elements before given index"""
        prod = 1
        sign = 1
        
        # Handle special case for first elements
        if index <= 1:
            return 1
        
        # Compute absolute product and track sign
        for i in range(index):
            # Update absolute product
            prod *= abs(nums[i])
            
            # Track sign
            if nums[i] < 0 and i < index - 1:
                sign *= -1
        
        return sign * prod
    
    # Compute specific product values 
    for i in range(1, len(numbers)):
        result[i] = signed_product(numbers, i)
    
    return result