import pytest
from src.palindrome_substrings import find_shortest_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_shortest_palindromic_substrings("") == []

def test_single_character_string():
    """Test a string with a single character."""
    assert find_shortest_palindromic_substrings("a") == ["a"]

def test_all_unique_characters():
    """Test a string with no repeated characters."""
    assert sorted(find_shortest_palindromic_substrings("abcde")) == ["a", "b", "c", "d", "e"]

def test_multiple_shortest_palindromes():
    """Test a string with multiple shortest palindromes."""
    assert sorted(find_shortest_palindromic_substrings("aabaa")) == ["a", "aa"]

def test_multiple_same_length_palindromes():
    """Test a string with multiple palindromes of the same length."""
    assert sorted(find_shortest_palindromic_substrings("abcba")) == ["a", "b", "c", "bcb"]

def test_overlapping_palindromes():
    """Test a string with overlapping palindromes."""
    assert sorted(find_shortest_palindromic_substrings("aaa")) == ["a", "aa"]

def test_complex_palindrome_string():
    """Test a more complex string with various palindromes."""
    result = find_shortest_palindromic_substrings("racecar")
    assert sorted(result) == ["a", "c", "r", "racecar"]

def test_no_palindromes_longer_than_one():
    """Test a string with no palindromes longer than one character."""
    assert sorted(find_shortest_palindromic_substrings("abcdef")) == ["a", "b", "c", "d", "e", "f"]