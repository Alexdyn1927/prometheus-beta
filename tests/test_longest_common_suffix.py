import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_basic_common_suffix():
    """Test finding a basic common suffix."""
    assert find_longest_common_suffix(["flower", "tower", "power"]) == "ower"

def test_single_string():
    """Test with a single string returns the entire string."""
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_no_common_suffix():
    """Test when no common suffix exists."""
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_empty_strings():
    """Test with empty strings."""
    assert find_longest_common_suffix(["", "", ""]) == ""

def test_partial_match():
    """Test when only some strings share a suffix."""
    assert find_longest_common_suffix(["hello", "world", "bello"]) == ""

def test_case_sensitive():
    """Test that suffix matching is case-sensitive."""
    assert find_longest_common_suffix(["Hello", "hello"]) == ""

def test_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_empty_list_error():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_suffix([])

def test_non_string_elements():
    """Test that TypeError is raised for non-string list elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["hello", 123, "world"])

def test_different_length_strings():
    """Test finding common suffix with strings of different lengths."""
    assert find_longest_common_suffix(["longer", "short"]) == ""

def test_identical_strings():
    """Test with identical strings."""
    assert find_longest_common_suffix(["hello", "hello", "hello"]) == "hello"