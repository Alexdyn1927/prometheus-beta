import pytest
from src.min_max_diff import find_min_max_difference

def test_basic_functionality():
    """Test finding difference with a simple comma-separated string."""
    assert find_min_max_difference("1,5,3,9") == 8

def test_negative_numbers():
    """Test finding difference with negative numbers."""
    assert find_min_max_difference("-10,5,0,3") == 15

def test_single_number():
    """Test with a single number."""
    assert find_min_max_difference("7") == 0

def test_repeated_numbers():
    """Test with repeated numbers."""
    assert find_min_max_difference("5,5,5,5") == 0

def test_whitespace_handling():
    """Test handling of whitespace around numbers."""
    assert find_min_max_difference(" 1 , 5 , 3 , 9 ") == 8

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_min_max_difference("")

def test_non_integer_raises_error():
    """Test that non-integer values raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a comma-separated string of integers"):
        find_min_max_difference("1,2,three,4")

def test_no_valid_numbers_raises_error():
    """Test that an empty list after parsing raises a ValueError."""
    with pytest.raises(ValueError, match="No valid numbers found in the input string"):
        find_min_max_difference(",")