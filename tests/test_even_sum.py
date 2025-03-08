import pytest
from src.even_sum import sum_positive_even_numbers

def test_sum_positive_even_numbers():
    # Test normal case with mixed positive and even numbers
    assert sum_positive_even_numbers([1, 2, 3, 4, 5, 6]) == 12

    # Test case with negative numbers
    assert sum_positive_even_numbers([-1, -2, 1, 3, 4, 6]) == 10

    # Test case with no even numbers
    assert sum_positive_even_numbers([1, 3, 5]) == 0

    # Test case with only negative numbers
    assert sum_positive_even_numbers([-1, -3, -5]) == 0

    # Test empty list
    assert sum_positive_even_numbers([]) == 0

    # Test large numbers
    assert sum_positive_even_numbers([10000, 20000, -30000, 40000]) == 70000

def test_input_types():
    # Test with different input types
    with pytest.raises(TypeError):
        sum_positive_even_numbers("not a list")
    
    with pytest.raises(TypeError):
        sum_positive_even_numbers([1, 2, "3", 4])

def test_none_input():
    # Test None input
    with pytest.raises(TypeError):
        sum_positive_even_numbers(None)