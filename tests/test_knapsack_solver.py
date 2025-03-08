import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario with multiple items."""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    result = solve_knapsack(items, capacity)
    
    # Validate total weight and value
    total_weight = sum(item[0] for item in result)
    total_value = sum(item[1] for item in result)
    
    assert total_weight <= capacity
    assert result == [(5, 6), (3, 4), (2, 3)] or result == [(4, 5), (3, 4), (2, 3)]

def test_empty_items():
    """Test behavior with empty items list."""
    assert solve_knapsack([], 10) == []

def test_zero_capacity():
    """Test behavior with zero capacity."""
    items = [(1, 10), (2, 20), (3, 30)]
    assert solve_knapsack(items, 0) == []

def test_single_item_fits():
    """Test scenario with a single item that fits exactly."""
    items = [(5, 10)]
    capacity = 5
    result = solve_knapsack(items, capacity)
    assert result == [(5, 10)]

def test_no_items_fit():
    """Test scenario where no items fit in the knapsack."""
    items = [(6, 10), (7, 20), (8, 30)]
    capacity = 5
    assert solve_knapsack(items, capacity) == []

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Negative capacity
    with pytest.raises(ValueError, match="Knapsack capacity cannot be negative"):
        solve_knapsack([(1, 10)], -5)
    
    # Negative item weight
    with pytest.raises(ValueError, match="Item weights and values must be non-negative"):
        solve_knapsack([(-1, 10)], 10)
    
    # Negative item value
    with pytest.raises(ValueError, match="Item weights and values must be non-negative"):
        solve_knapsack([(1, -10)], 10)

def test_multiple_optimal_solutions():
    """Test case with multiple optimal solutions."""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    result = solve_knapsack(items, capacity)
    
    # Check that result is one of the possible optimal solutions
    valid_solutions = [
        [(5, 6), (3, 4), (2, 3)],
        [(4, 5), (3, 4), (2, 3)]
    ]
    assert result in valid_solutions