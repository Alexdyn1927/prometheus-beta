import pytest
from src.validate_sequence import is_valid_sequence

def test_valid_sequence_basic():
    """Test a basic valid increasing sequence"""
    assert is_valid_sequence([1, 2, 3, 4, 5]) == True

def test_valid_sequence_negative_numbers():
    """Test a valid sequence with negative numbers"""
    assert is_valid_sequence([-5, -3, 0, 2, 4]) == True

def test_empty_sequence():
    """Test that an empty list is considered valid"""
    assert is_valid_sequence([]) == True

def test_single_element_sequence():
    """Test that a single-element list is considered valid"""
    assert is_valid_sequence([42]) == True

def test_invalid_sequence_not_increasing():
    """Test sequence that is not strictly increasing"""
    assert is_valid_sequence([1, 2, 2, 3, 4]) == False

def test_invalid_sequence_decreasing():
    """Test a decreasing sequence"""
    assert is_valid_sequence([5, 4, 3, 2, 1]) == False

def test_invalid_sequence_non_increasing():
    """Test a non-increasing sequence"""
    assert is_valid_sequence([1, 3, 2, 4, 5]) == False

def test_raise_non_list_input():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        is_valid_sequence("not a list")

def test_raise_non_integer_elements():
    """Test that list with non-integer elements raises ValueError"""
    with pytest.raises(ValueError):
        is_valid_sequence([1, 2, "3", 4, 5])

def test_raise_mixed_types():
    """Test that mixed type list raises ValueError"""
    with pytest.raises(ValueError):
        is_valid_sequence([1, 2.5, 3, 4, 5])