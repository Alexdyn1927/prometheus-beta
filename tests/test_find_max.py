import pytest
from src.find_max import find_max_number

def test_find_max_positive_numbers():
    """Test finding max in an array of positive numbers."""
    assert find_max_number([1, 2, 3, 4, 5]) == 5
    assert find_max_number([10, 5, 8, 12, 3]) == 12

def test_find_max_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers."""
    assert find_max_number([-1, 0, 1]) == 1
    assert find_max_number([-10, -5, -3]) == -3

def test_find_max_with_floats():
    """Test finding max in an array with float numbers."""
    assert find_max_number([1.5, 2.7, 0.3]) == 2.7
    assert find_max_number([-1.5, 0, 1.5]) == 1.5

def test_find_max_single_element():
    """Test finding max in an array with a single element."""
    assert find_max_number([42]) == 42

def test_find_max_error_empty_array():
    """Test that an error is raised for an empty array."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])

def test_find_max_error_non_list():
    """Test that an error is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number(123)

def test_find_max_error_non_numeric():
    """Test that an error is raised for non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, None])