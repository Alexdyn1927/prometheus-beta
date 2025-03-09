import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test list with all identical elements."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_order_preservation():
    """Ensure the first occurrence of each element is preserved."""
    assert remove_duplicates([5, 2, 5, 3, 2, 1, 3]) == [5, 2, 3, 1]

def test_remove_duplicates_with_zero():
    """Test handling of zero in the list."""
    assert remove_duplicates([0, 1, 0, 2, 1, 3]) == [0, 1, 2, 3]

def test_remove_duplicates_large_list():
    """Test with a larger list of numbers."""
    input_list = list(range(10)) * 3
    assert remove_duplicates(input_list) == list(range(10))

def test_remove_duplicates_type_error():
    """Ensure the function handles invalid input types."""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    with pytest.raises(TypeError):
        remove_duplicates(None)