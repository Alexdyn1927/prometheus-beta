import pytest
import logging
from src.sorting_performance import compare_sorting_algorithms, bubble_sort, quick_sort

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_compare_sorting_algorithms_basic():
    """Test sorting algorithm comparison with basic input."""
    test_data = [64, 34, 25, 12, 22, 11, 90]
    time1, time2, same_output = compare_sorting_algorithms(bubble_sort, quick_sort, test_data)
    
    assert same_output == True
    assert time1 > 0
    assert time2 > 0

def test_compare_sorting_algorithms_large():
    """Test sorting algorithm comparison with larger input."""
    import random
    random.seed(42)  # For reproducibility
    test_data = [random.randint(0, 1000) for _ in range(1000)]
    time1, time2, same_output = compare_sorting_algorithms(bubble_sort, quick_sort, test_data)
    
    assert same_output == True
    assert time1 > 0
    assert time2 > 0

def test_compare_sorting_algorithms_edge_cases():
    """Test sorting algorithm comparison with edge cases."""
    # Empty list
    empty_list = []
    time1, time2, same_output = compare_sorting_algorithms(bubble_sort, quick_sort, empty_list)
    assert same_output == True

    # Single element list
    single_list = [42]
    time1, time2, same_output = compare_sorting_algorithms(bubble_sort, quick_sort, single_list)
    assert same_output == True

def test_sorting_algorithm_input_types():
    """Ensure sorting algorithms handle different input types gracefully."""
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],  # Regular list of integers
        list(range(100, 0, -1)),  # Reversed list
        [1, 1, 1, 1, 1],  # List with duplicate elements
    ]

    for test_data in test_cases:
        time1, time2, same_output = compare_sorting_algorithms(bubble_sort, quick_sort, test_data)
        assert same_output == True
        assert time1 > 0
        assert time2 > 0