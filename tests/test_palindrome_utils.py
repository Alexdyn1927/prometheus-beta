import pytest
from src.palindrome_utils import find_shortest_palindromic_substrings

def test_empty_string():
    assert find_shortest_palindromic_substrings("") == []

def test_single_character():
    assert find_shortest_palindromic_substrings("a") == ["a"]

def test_no_palindromes():
    assert find_shortest_palindromic_substrings("abc") == ["a", "b", "c"]

def test_multiple_single_char_palindromes():
    assert find_shortest_palindromic_substrings("aab") == ["a", "b"]

def test_mixed_palindromes():
    result = find_shortest_palindromic_substrings("abcba")
    assert set(result) == {"a", "b", "c", "bcb", "abcba"}

def test_repeated_palindromes():
    result = find_shortest_palindromic_substrings("racecar")
    assert set(result) == {"a", "c", "r", "ac", "rr", "acca", "racecar"}

def test_multiple_palindromes_of_same_length():
    result = find_shortest_palindromic_substrings("abcdefedcba")
    assert set(result) == {"a", "b", "c", "d", "e", "f"}

def test_all_same_character():
    assert find_shortest_palindromic_substrings("aaaa") == ["a"]