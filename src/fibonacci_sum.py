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
    fib_seq = [0, 1]
    
    # Generate Fibonacci sequence
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    # Return sum of first n Fibonacci numbers
    return sum(fib_seq[:n])