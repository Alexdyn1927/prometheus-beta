import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import quick_select, select_pivot, partition

def test_select_pivot_basic():
    """Test basic pivot selection"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    pivot = select_pivot(arr)
    assert pivot in arr

def test_select_pivot_small_array():
    """Test pivot selection for small arrays"""
    arr = [3, 1, 4]
    pivot = select_pivot(arr)
    assert pivot == 3

def test_partition_basic():
    """Test array partitioning"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    pivot = 5
    less, equal, greater = partition(arr, pivot)
    
    assert all(x < pivot for x in less)
    assert all(x == pivot for x in equal)
    assert all(x > pivot for x in greater)

def test_quick_select_basic():
    """Test finding k-th smallest element"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sorted(arr)
    
    # Test various k values
    assert quick_select(arr, 0) == min(arr)  # smallest element
    
    # Check if the 5th index (k=5) is a valid mid-point element 
    mid_val = quick_select(arr, 5)
    assert sorted_arr[5] == mid_val

    assert quick_select(arr, len(arr)-1) == 9  # largest element

def test_quick_select_sorted_array():
    """Test quick select on an already sorted array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    assert quick_select(arr, 0) == 1
    assert quick_select(arr, 4) == 5
    assert quick_select(arr, len(arr)-1) == 9

def test_quick_select_reverse_sorted():
    """Test quick select on a reverse sorted array"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    assert quick_select(arr, 0) == 1
    assert quick_select(arr, 4) == 5
    assert quick_select(arr, len(arr)-1) == 9

def test_quick_select_error_cases():
    """Test error handling"""
    # Empty array
    with pytest.raises(ValueError, match="Cannot find element in an empty array"):
        quick_select([], 0)
    
    # Out of bounds index
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="k must be between 0 and 4"):
        quick_select(arr, 5)
    
    with pytest.raises(ValueError):
        quick_select(arr, -1)

def test_quick_select_duplicate_elements():
    """Test quick select with duplicate elements"""
    arr = [3, 3, 3, 3, 3, 3, 3]
    
    assert quick_select(arr, 0) == 3
    assert quick_select(arr, 3) == 3
    assert quick_select(arr, len(arr)-1) == 3

def test_quick_select_large_array():
    """Test quick select on a larger, unsorted array"""
    arr = [42, 17, 93, 8, 55, 22, 61, 3, 99, 12, 45, 70, 31, 6, 88]
    
    # Sort the array to verify correct selection
    sorted_arr = sorted(arr)
    
    for k in range(len(arr)):
        assert quick_select(arr, k) == sorted_arr[k]