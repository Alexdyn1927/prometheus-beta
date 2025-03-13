from typing import List
from itertools import combinations

def min_steps_to_target_sum(numbers: List[int], target: int) -> int:
    """
    Calculate the minimum number of steps to reach the target sum using given numbers.
    
    Each number can be used only once, and steps can involve addition or subtraction.
    
    Args:
        numbers (List[int]): List of integers to use
        target (int): Target sum to reach
    
    Returns:
        int: Minimum number of steps to reach the target sum
             Returns -1 if it's impossible to reach the target
    
    Raises:
        ValueError: If input list is empty
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Try all possible combinations of numbers
    for step_count in range(1, len(numbers) + 1):
        for combo in combinations(numbers, step_count):
            # Try all possible sign combinations
            for signs in range(2 ** step_count):
                current_sum = 0
                for i, num in enumerate(combo):
                    # Determine sign based on binary representation
                    sign = 1 if (signs & (1 << i)) == 0 else -1
                    current_sum += sign * num
                
                # Check if we've reached the target
                if current_sum == target:
                    return step_count
    
    # If no combination works
    return -1