def find_min_max_difference(number_string: str) -> int:
    """
    Calculate the difference between the largest and smallest numbers in a comma-separated string of integers.

    Args:
        number_string (str): A string of comma-separated integers.

    Returns:
        int: The difference between the largest and smallest numbers.

    Raises:
        ValueError: If the input string is empty or contains non-integer values.
    """
    # Check for empty string
    if not number_string:
        raise ValueError("Input string cannot be empty")

    # Split the string and convert to integers
    try:
        numbers = [int(num.strip()) for num in number_string.split(',')]
    except ValueError:
        raise ValueError("Input must be a comma-separated string of integers")

    # Check if the list is empty after parsing
    if not numbers:
        raise ValueError("No valid numbers found in the input string")

    # Find and return the difference between max and min
    return max(numbers) - min(numbers)