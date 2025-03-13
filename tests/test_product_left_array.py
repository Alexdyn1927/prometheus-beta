import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from product_left_array import product_left_elements

def test_basic_array():
    """Test with a basic array of integers"""
    assert product_left_elements([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_empty_array():
    """Test with an empty array"""
    assert product_left_elements([]) == []

def test_single_element_array():
    """Test with a single element array"""
    assert product_left_elements([5]) == [1]

def test_array_with_zeros():
    """Test array that includes zeros"""
    assert product_left_elements([1, 0, 2, 3]) == [1, 0, 0, 0]

def test_float_numbers():
    """Test with floating point numbers"""
    assert product_left_elements([1.5, 2.0, 3.0]) == [1, 1.5, 3.0]

def test_invalid_input_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError):
        product_left_elements("not a list")

def test_non_numeric_elements():
    """Test that a list with non-numeric elements raises ValueError"""
    with pytest.raises(ValueError):
        product_left_elements([1, 2, "three", 4])

def test_negative_numbers():
    """Test with negative numbers"""
    assert product_left_elements([-1, 2, -3, 4]) == [1, -1, -2, -6]