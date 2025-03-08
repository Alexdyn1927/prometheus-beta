import pytest
from src.list_utils import remove_duplicates

def test_remove_duplicates_basic():
    """Test removing duplicates from a simple list of integers."""
    input_list = [1, 2, 2, 3, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_strings():
    """Test removing duplicates from a list of strings."""
    input_list = ['a', 'b', 'a', 'c', 'b']
    expected = ['a', 'b', 'c']
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_preserve_order():
    """Ensure the order of first occurrence is maintained."""
    input_list = [3, 1, 2, 3, 4, 1, 5]
    expected = [3, 1, 2, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test handling of an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates."""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate elements."""
    input_list = [1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test a list with mixed hashable types."""
    input_list = [1, '1', 1.0, True, 1]
    expected = [1, '1', 1.0, True]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)