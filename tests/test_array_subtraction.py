import pytest
from src.array_subtraction import subtract_arrays

def test_basic_subtraction():
    A = [5, 7, 3, 8, 1, 9, 2, 6, 4, 0]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    expected = [4, 5, 0, 4, 6, 3, 5, 8, 5, 0]
    assert subtract_arrays(A, B) == expected

def test_negative_results():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [5, 7, 8, 9, 6, 7, 8, 9, 0, 1]
    expected = [6, 5, 5, 5, 9, 9, 9, 9, 9, 9]
    assert subtract_arrays(A, B) == expected

def test_equal_arrays():
    A = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    B = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert subtract_arrays(A, B) == expected

def test_invalid_array_length():
    with pytest.raises(ValueError):
        subtract_arrays([1, 2, 3], [4, 5, 6])
    
    with pytest.raises(ValueError):
        subtract_arrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3])

def test_zero_subtraction():
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert subtract_arrays(A, B) == expected