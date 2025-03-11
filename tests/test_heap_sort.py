import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from heap_sort import heap_sort

def test_heap_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [4, 10, 3, 5, 1]
    expected = [1, 3, 4, 5, 10]
    assert heap_sort(input_list) == expected

def test_heap_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == input_list

def test_heap_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == expected

def test_heap_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert heap_sort(input_list) == expected

def test_heap_sort_empty_list():
    """Test sorting an empty list."""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert heap_sort(input_list) == [42]

def test_heap_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert heap_sort(input_list) == expected

def test_heap_sort_input_not_modified():
    """Ensure the original input list is not modified."""
    input_list = [4, 2, 7, 1, 5, 3]
    original_copy = input_list.copy()
    heap_sort(input_list)
    assert input_list == original_copy

def test_heap_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort(None)