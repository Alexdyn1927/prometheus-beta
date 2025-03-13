import pytest
from src.min_steps_to_target_sum import min_steps_to_target_sum

def test_basic_positive_scenario():
    """Test a basic scenario where the target can be reached"""
    assert min_steps_to_target_sum([1, 2, 3], 4) == 2  # e.g., 1 + 3

def test_negative_numbers():
    """Test scenarios with negative numbers"""
    assert min_steps_to_target_sum([-1, 2, 3], 2) == 1  # e.g., 2 or 3 or 3-1

def test_exact_match():
    """Test when a number exactly matches the target"""
    assert min_steps_to_target_sum([1, 2, 3, 4], 3) == 1

def test_impossible_target():
    """Test when the target cannot be reached"""
    assert min_steps_to_target_sum([1, 2], 10) == -1

def test_zero_target():
    """Test targeting zero sum"""
    assert min_steps_to_target_sum([1, -1, 2, -2], 0) == 2

def test_multiple_ways_minimum_steps():
    """Test that the function returns the minimum number of steps"""
    assert min_steps_to_target_sum([1, 2, 3, 4], 5) == 2

def test_error_on_empty_list():
    """Test that an error is raised for an empty input list"""
    with pytest.raises(ValueError):
        min_steps_to_target_sum([], 5)

def test_large_numbers():
    """Test with larger numbers"""
    assert min_steps_to_target_sum([10, 20, 30, 40], 50) == 2

def test_mixed_signs():
    """Test with mixed positive and negative numbers"""
    assert min_steps_to_target_sum([-5, 5, 10, -10], 0) == 2