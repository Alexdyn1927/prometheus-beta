"""
Extended Fibonacci Sequence Generator

This module provides a function to generate Fibonacci sequence values 
for both positive and negative indices, supporting integer and float inputs.
"""
import math

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
    
    # Handle float inputs first for improved interpolation
    if isinstance(n, float):
        # Get floor and ceiling of float index
        floor_n = math.floor(n)
        ceil_n = math.ceil(n)
        
        # Calculate Fibonacci values at floor and ceiling
        floor_fib = extended_fibonacci(floor_n)
        ceil_fib = extended_fibonacci(ceil_n)
        
        # Linear interpolation
        if floor_n == ceil_n:
            return float(floor_fib)
        
        # Interpolate between floor and ceiling Fibonacci values
        ratio = abs(n - floor_n)
        interpolated = floor_fib + ratio * (ceil_fib - floor_fib)
        return interpolated
    
    # Handle integer inputs
    if n >= 0:
        # Standard Fibonacci for non-negative indices
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Iterative approach for positive indices
        a, b = 0, 1
        for _ in range(2, int(n) + 1):
            a, b = b, a + b
        return b
    
    # For negative indices, use the extended Fibonacci property
    else:
        # Alternate sign for negative indices
        sign = (-1) ** (abs(int(n)) + 1)
        return sign * extended_fibonacci(abs(n))