def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.

    Args:
        n (int): A positive integer representing the number of Fibonacci terms to sum.

    Returns:
        int: The sum of the first n numbers in the Fibonacci sequence.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    # Handle special cases
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize Fibonacci sequence and sum
    fib_prev, fib_curr = 0, 1
    total_sum = fib_prev + fib_curr

    # Generate Fibonacci sequence and calculate sum
    for _ in range(3, n + 1):
        fib_next = fib_prev + fib_curr
        total_sum += fib_next
        fib_prev, fib_curr = fib_curr, fib_next

    return total_sum