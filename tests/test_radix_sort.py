import pytest
from src.radix_sort import radix_sort

def test_radix_sort_normal_case():
    """Test radix sort with a standard list of positive integers."""
    input_list = [170, 45, 75, 90, 802, 24, 2, 66]
    expected = [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort(input_list) == expected

def test_radix_sort_empty_list():
    """Test radix sort with an empty list."""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test radix sort with a single element."""
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    """Test radix sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert radix_sort(input_list) == input_list

def test_radix_sort_reverse_sorted():
    """Test radix sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert radix_sort(input_list) == expected

def test_radix_sort_duplicate_elements():
    """Test radix sort with duplicate elements."""
    input_list = [5, 2, 9, 1, 5, 6, 2]
    expected = [1, 2, 2, 5, 5, 6, 9]
    assert radix_sort(input_list) == expected

def test_radix_sort_zero_elements():
    """Test radix sort with a list containing zeros."""
    input_list = [0, 0, 0, 1, 0]
    expected = [0, 0, 0, 0, 1]
    assert radix_sort(input_list) == expected

def test_radix_sort_invalid_input_non_list():
    """Test radix sort with non-list input raises TypeError."""
    with pytest.raises(TypeError):
        radix_sort("not a list")

def test_radix_sort_invalid_input_negative_numbers():
    """Test radix sort with negative numbers raises ValueError."""
    with pytest.raises(ValueError):
        radix_sort([1, 2, -3, 4])

def test_radix_sort_mixed_length_numbers():
    """Test radix sort with numbers of different lengths."""
    input_list = [1, 10, 100, 1000, 5, 50, 500]
    expected = [1, 5, 10, 50, 100, 500, 1000]
    assert radix_sort(input_list) == expected