import pytest
from src.palindrome_pairs import find_palindrome_word_pair_indices, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_find_palindrome_word_pair_indices_basic():
    """Test basic functionality of finding palindrome word pair indices."""
    words = ["bat", "tab", "cat"]
    assert find_palindrome_word_pair_indices(words) == [(0, 1)]

def test_find_palindrome_word_pair_indices_complex():
    """Test more complex scenarios of palindrome word pairs."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_word_pair_indices(words)
    assert (0, 1) in result
    assert (1, 0) in result
    assert (3, 4) in result

def test_find_palindrome_word_pair_indices_empty_list():
    """Test behavior with an empty list."""
    assert find_palindrome_word_pair_indices([]) == []

def test_find_palindrome_word_pair_indices_single_word():
    """Test behavior with a single word."""
    assert find_palindrome_word_pair_indices(["hello"]) == []

def test_find_palindrome_word_pair_indices_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        find_palindrome_word_pair_indices("not a list")
    with pytest.raises(TypeError):
        find_palindrome_word_pair_indices(123)
    with pytest.raises(TypeError):
        find_palindrome_word_pair_indices(None)