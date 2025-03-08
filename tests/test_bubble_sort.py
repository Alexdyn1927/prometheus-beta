import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_normal_case():
    """Test sorting a typical unsorted list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_empty_list():
    """Test sorting an empty list"""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")

def test_bubble_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [3, 1, 4, 2]
    original_copy = input_list.copy()
    bubble_sort(input_list)
    assert input_list == original_copy