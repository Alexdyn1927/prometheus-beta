def remove_duplicates(numbers):
    """
    Remove duplicate items from a list of integers while maintaining the original order.

    Args:
        numbers (list): A list of integers potentially containing duplicates.

    Returns:
        list: A new list with duplicates removed, preserving the first occurrence of each unique element.

    Raises:
        TypeError: If the input is not a list.

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1, 1])
        [1]
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for num in numbers:
        # Only add the number if it hasn't been seen before
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result