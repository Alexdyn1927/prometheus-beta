def remove_duplicates(input_list):
    """
    Remove duplicates from a given list while preserving the original order.

    Args:
        input_list (list): The input list that may contain duplicate elements.

    Returns:
        list: A new list with duplicate elements removed, maintaining the 
              order of first occurrence of each unique element.

    Raises:
        TypeError: If the input is not a list.

    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates(['a', 'b', 'a', 'c', 'b'])
        ['a', 'b', 'c']
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    unique_list = []
    
    for item in input_list:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list