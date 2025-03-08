import pytest
from src.longest_subarray_diff import longest_subarray_diff

def test_basic_case():
    """Test a basic scenario where there's a clear longest subarray"""
    assert longest_subarray_diff([1, 5, 3, 8, 12], 3) == 4

def test_single_element_array():
    """Test array with a single element"""
    assert longest_subarray_diff([5], 2) == 1

def test_no_valid_subarray():
    """Test case where no elements meet the difference condition"""
    assert longest_subarray_diff([1, 2, 3, 4, 5], 10) == 1

def test_entire_array_valid():
    """Test case where the entire array meets the condition"""
    assert longest_subarray_diff([1, 5, 9, 14, 20], 4) == 5

def test_multiple_valid_subarrays():
    """Test case with multiple potential valid subarrays"""
    assert longest_subarray_diff([3, 1, 6, 4, 9, 2, 10], 3) == 3

def test_empty_array_raises_error():
    """Test that empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        longest_subarray_diff([], 2)

def test_negative_k_raises_error():
    """Test that negative k raises a ValueError"""
    with pytest.raises(ValueError, match="k must be non-negative"):
        longest_subarray_diff([1, 2, 3], -1)

def test_boundary_condition():
    """Test boundary condition where difference is exactly k"""
    assert longest_subarray_diff([1, 4, 8, 13], 4) == 3