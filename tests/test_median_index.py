import pytest
from src.median_index import find_median_index

def test_odd_length_array():
    """Test median index for odd-length sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert find_median_index(arr) == 2

def test_even_length_array():
    """Test median index for even-length sorted array"""
    arr = [1, 2, 3, 4]
    assert find_median_index(arr) == 1.5

def test_single_element_array():
    """Test array with single element"""
    arr = [42]
    assert find_median_index(arr) == 0

def test_two_element_array():
    """Test array with two elements"""
    arr = [1, 2]
    assert find_median_index(arr) == 0.5

def test_empty_array():
    """Test empty array raises ValueError"""
    with pytest.raises(ValueError, match="Cannot find median of an empty array"):
        find_median_index([])