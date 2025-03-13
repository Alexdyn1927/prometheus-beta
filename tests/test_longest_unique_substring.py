import pytest
from src.longest_unique_substring import longest_unique_substring_length

def test_basic_cases():
    """Test basic scenarios for longest unique substring length."""
    assert longest_unique_substring_length("abcabcbb") == 3
    assert longest_unique_substring_length("bbbbb") == 1
    assert longest_unique_substring_length("pwwkew") == 3

def test_edge_cases():
    """Test edge cases like empty string and single character."""
    assert longest_unique_substring_length("") == 0
    assert longest_unique_substring_length("a") == 1
    assert longest_unique_substring_length(" ") == 1

def test_all_unique_characters():
    """Test strings with all unique characters."""
    assert longest_unique_substring_length("abcdef") == 6
    assert longest_unique_substring_length("python") == 6

def test_repeated_characters():
    """Test strings with various repeated character patterns."""
    assert longest_unique_substring_length("aab") == 2
    assert longest_unique_substring_length("dvdf") == 3
    assert longest_unique_substring_length("tmmzuxt") == 5

def test_special_characters():
    """Test strings with special characters and whitespace."""
    assert longest_unique_substring_length("!@#$%^&*()") == 10
    assert longest_unique_substring_length("a b c d e") == 3  # Corrected to match actual behavior
    assert longest_unique_substring_length("  hello  ") == 4

def test_unicode_characters():
    """Test strings with Unicode characters."""
    assert longest_unique_substring_length("こんにちは") == 5
    assert longest_unique_substring_length("🌈🌞🌍🌊🌻") == 5