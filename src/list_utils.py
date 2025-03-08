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
    
    # Use a list to track seen elements and their order
    unique_list = []
    seen = set()
    
    for item in input_list:
        # Ensure perfect match by using id for mixed types 
        # that might be considered equivalent
        item_id = id(item) if not isinstance(item, (int, float, str, bool)) else item
        
        # Only add item if it hasn't been seen before
        if item_id not in seen:
            seen.add(item_id)
            unique_list.append(item)
    
    return unique_list