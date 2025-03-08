def sum_positive_even_numbers(numbers):
    """
    Calculate the sum of all positive even numbers in the given list.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: The sum of all positive even numbers in the list.
             Returns 0 if no positive even numbers are found.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.

    Examples:
        >>> sum_positive_even_numbers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_positive_even_numbers([-1, -2, 1, 3, 4, 6])
        10
        >>> sum_positive_even_numbers([1, 3, 5])
        0
    """
    # Check for None input
    if numbers is None:
        raise TypeError("Input must be a list of integers")

    # Validate input is a list and contains only integers
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")

    # Filter for positive even numbers and sum them
    return sum(num for num in numbers if num > 0 and num % 2 == 0)