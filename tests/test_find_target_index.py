import pytest
from src.find_target_index import find_target_index

def test_target_in_middle():
    """Test finding a target in the middle of the list."""
    assert find_target_index([1, 2, 3, 4, 5], 3) == 2

def test_target_at_beginning():
    """Test finding a target at the beginning of the list."""
    assert find_target_index([1, 2, 3, 4, 5], 1) == 0

def test_target_at_end():
    """Test finding a target at the end of the list."""
    assert find_target_index([1, 2, 3, 4, 5], 5) == 4

def test_target_not_found():
    """Test when target is not in the list."""
    assert find_target_index([1, 2, 3, 4, 5], 6) == -1

def test_empty_list():
    """Test finding a target in an empty list."""
    assert find_target_index([], 1) == -1

def test_multiple_occurrences():
    """Test that the first occurrence is returned when target appears multiple times."""
    assert find_target_index([1, 2, 3, 2, 1], 2) == 1

def test_negative_numbers():
    """Test finding targets with negative numbers."""
    assert find_target_index([-1, -2, -3, 0, 1], -2) == 1

def test_zero_target():
    """Test finding zero as a target."""
    assert find_target_index([0, 1, 2, 3], 0) == 0