"""
Extended Fibonacci Sequence Generator

This module provides a function to generate Fibonacci sequence values 
for both positive and negative indices, supporting integer and float inputs.
"""

def extended_fibonacci(n):
    """
    Generate the nth term of the extended Fibonacci sequence.
    
    The extended Fibonacci sequence supports:
    - Positive and negative indices
    - Integer and float inputs
    
    Args:
        n (int or float): The index of the Fibonacci sequence to calculate
    
    Returns:
        float: The nth term of the extended Fibonacci sequence
    
    Raises:
        TypeError: If input is not a number
    """
    # Validate input type
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    
    # Handle integer inputs first
    if isinstance(n, int):
        # For non-negative indices, use standard Fibonacci logic
        if n >= 0:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            
            # Iterative approach for positive indices
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        
        # For negative indices, use the extended Fibonacci property
        else:
            # Alternate sign for negative indices
            sign = (-1) ** (abs(n) + 1)
            return sign * extended_fibonacci(abs(n))
    
    # Handle float inputs with interpolation
    else:
        # Get floor and ceiling of float index
        floor_n = int(n)
        ceil_n = int(n) + 1 if n > 0 else int(n) - 1
        
        # Calculate Fibonacci values at floor and ceiling
        floor_fib = extended_fibonacci(floor_n)
        ceil_fib = extended_fibonacci(ceil_n)
        
        # Linear interpolation
        frac_part = abs(n - floor_n)
        return floor_fib + frac_part * (ceil_fib - floor_fib)