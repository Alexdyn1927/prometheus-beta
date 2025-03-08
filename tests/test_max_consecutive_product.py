import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_basic_positive_array():
    """Test with a basic positive integer array"""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60  # 3 * 4 * 5

def test_array_with_negatives():
    """Test array with negative numbers"""
    arr = [-1, -2, -3, 4, 5]
    assert find_max_consecutive_product(arr) == 24  # -1 * -2 * -3 or 4 * 5 * -3

def test_array_with_zeros():
    """Test array containing zeros"""
    arr = [1, 0, 2, 3, 4]
    assert find_max_consecutive_product(arr) == 24  # 2 * 3 * 4

def test_all_negative_array():
    """Test array with all negative numbers"""
    arr = [-10, -5, -2, -1]
    assert find_max_consecutive_product(arr) == -10  # -10 * -5 * -2 highest is -10 by consecutive selection

def test_mixed_sign_array():
    """Test array with mixed positive, negative, and zero values"""
    arr = [-3, 1, 2, -1, 4, 0, 5]
    assert find_max_consecutive_product(arr) == 8  # 2 * 4 * 1

def test_minimum_array_length():
    """Test array with exactly 3 elements"""
    arr = [1, 2, 3]
    assert find_max_consecutive_product(arr) == 6  # 1 * 2 * 3

def test_insufficient_array_length():
    """Test that ValueError is raised for array with fewer than 3 elements"""
    with pytest.raises(ValueError, match="Array must contain at least 3 elements"):
        find_max_consecutive_product([1, 2])

def test_large_numbers():
    """Test array with large numbers"""
    arr = [1000, 1000, 1000, 1, 2, 3]
    assert find_max_consecutive_product(arr) == 1_000_000_000  # 1000 * 1000 * 1000