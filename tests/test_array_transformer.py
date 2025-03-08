import pytest
from src.array_transformer import transform_array

def test_transform_array_basic():
    """Test basic transformation of array"""
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]

def test_transform_array_empty():
    """Test transformation of empty array"""
    assert transform_array([]) == []

def test_transform_array_zeros():
    """Test array with only zeros"""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        transform_array("not a list")
    
    with pytest.raises(TypeError):
        transform_array(None)

def test_transform_array_negative_numbers():
    """Test rejection of negative numbers"""
    with pytest.raises(ValueError):
        transform_array([-1, 2, 3])

def test_transform_array_large_numbers():
    """Test transformation with large numbers"""
    assert transform_array([10, 20, 30]) == [101, 401, 901]