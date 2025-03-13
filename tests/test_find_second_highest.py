import pytest
from src.find_second_highest import find_second_highest

def test_sorted_list_with_unique_elements():
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_sorted_list_with_duplicates():
    assert find_second_highest([1, 2, 2, 3, 3, 4, 5]) == 4

def test_list_with_two_unique_elements():
    assert find_second_highest([1, 2]) == 1

def test_list_with_all_same_elements():
    assert find_second_highest([3, 3, 3, 3]) is None

def test_empty_list():
    with pytest.raises(ValueError):
        find_second_highest([])

def test_single_element_list():
    assert find_second_highest([1]) is None

def test_non_list_input():
    with pytest.raises(TypeError):
        find_second_highest("not a list")

def test_negative_numbers():
    assert find_second_highest([-5, -4, -3, -2, -1]) == -2

def test_mixed_positive_negative():
    assert find_second_highest([-10, -5, 0, 5, 10]) == 5