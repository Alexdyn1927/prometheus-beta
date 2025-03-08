import pytest
from src.find_smallest_multiple import find_smallest_multiple_of_five

def test_basic_array():
    """Test with a basic array that needs a small addition."""
    assert find_smallest_multiple_of_five([1, 2, 3]) == 4

def test_already_multiple():
    """Test when the sum is already a multiple of 5."""
    assert find_smallest_multiple_of_five([5, 10, 15]) == 0

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_smallest_multiple_of_five([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_smallest_multiple_of_five(42)

def test_non_integer_elements():
    """Test that non-integer elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_smallest_multiple_of_five([1, 2, '3'])

def test_negative_numbers():
    """Test array with negative numbers."""
    assert find_smallest_multiple_of_five([-3, -2, -1]) == 1

def test_large_array():
    """Test with a larger array to ensure correct calculation."""
    assert find_smallest_multiple_of_five([7, 12, 13, 14]) == 4

def test_zero_in_array():
    """Test an array containing zero."""
    assert find_smallest_multiple_of_five([0, 1, 2]) == 2