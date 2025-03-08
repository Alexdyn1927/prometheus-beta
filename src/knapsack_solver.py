from typing import List, Tuple, Optional

def solve_knapsack(items: List[Tuple[int, int]], capacity: int) -> List[Tuple[int, int]]:
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (List[Tuple[int, int]]): A list of (weight, value) tuples representing items.
        capacity (int): Maximum weight capacity of the knapsack.
    
    Returns:
        List[Tuple[int, int]]: The most valuable combination of items that fit within the capacity.
    
    Raises:
        ValueError: If capacity is negative or items contain invalid weights/values.
    """
    # Input validation
    if capacity < 0:
        raise ValueError("Knapsack capacity cannot be negative")
    
    if any(weight < 0 or value < 0 for weight, value in items):
        raise ValueError("Item weights and values must be non-negative")
    
    # If no items or zero capacity, return empty list
    if not items or capacity == 0:
        return []
    
    # Create dynamic programming table
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]
            
            # Try to include current item if possible
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            # This item was selected
            selected_items.append(items[i-1])
            w -= items[i-1][0]
    
    return selected_items