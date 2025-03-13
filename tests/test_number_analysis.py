import pytest
from src.number_analysis import analyze_numbers

def test_mixed_numbers():
    """Test with a mix of even and odd numbers."""
    result = analyze_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_empty_list():
    """Test with an empty list."""
    result = analyze_numbers([])
    assert result == (0, 0)

def test_only_even_numbers():
    """Test with only even numbers."""
    result = analyze_numbers([2, 4, 6, 8])
    assert result == (20, 0)

def test_only_odd_numbers():
    """Test with only odd numbers."""
    result = analyze_numbers([1, 3, 5, 7])
    assert result == (0, 4)

def test_negative_numbers():
    """Test with negative numbers."""
    result = analyze_numbers([-1, -2, -3, -4, -5, -6])
    assert result == (-12, 3)

def test_invalid_input_type():
    """Test with invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        analyze_numbers(123)

def test_invalid_element_type():
    """Test with list containing non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        analyze_numbers([1, 2, '3', 4])