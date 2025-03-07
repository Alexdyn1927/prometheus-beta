import pytest
from src.max_subarray_sum import find_max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert find_max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert find_max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]) == 9

def test_all_negative_numbers():
    """Test with an array of all negative numbers."""
    assert find_max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element array."""
    assert find_max_subarray_sum([42]) == 42

def test_zero_sum():
    """Test an array where the max sum is zero."""
    assert find_max_subarray_sum([-1, -1, 0, -1, -1]) == 0

def test_multiple_max_subarrays():
    """Test an array with multiple possible max subarrays."""
    assert find_max_subarray_sum([1, -1, 1, -1, 1]) == 1

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_max_subarray_sum("not a list")

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_max_subarray_sum([])