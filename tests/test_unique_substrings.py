import pytest
from src.unique_substrings import find_unique_substrings

def test_basic_unique_substrings():
    """Test finding unique substrings in a simple string."""
    result = find_unique_substrings("abc")
    expected = ['', 'a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == expected

def test_empty_string():
    """Test behavior with an empty string."""
    assert find_unique_substrings("") == []

def test_single_character_string():
    """Test a single character string."""
    result = find_unique_substrings("a")
    expected = ['', 'a']
    assert sorted(result) == expected

def test_repeated_characters():
    """Test a string with repeated characters."""
    result = find_unique_substrings("aaa")
    expected = ['', 'a', 'aa', 'aaa']
    assert sorted(result) == expected

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(None)

def test_complex_string():
    """Test a more complex string with various characters."""
    result = find_unique_substrings("hello")
    expected = ['', 'e', 'el', 'ell', 'ello', 'h', 'he', 'hel', 'hell', 'hello', 'l', 'll', 'llo', 'lo', 'o']
    assert sorted(result) == expected