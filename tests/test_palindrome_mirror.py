import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string():
    """Test basic string palindrome mirror creation."""
    assert create_palindrome_mirror("abc") == "abcba"

def test_empty_string():
    """Test empty string palindrome mirror."""
    assert create_palindrome_mirror("") == ""

def test_single_character():
    """Test single character string."""
    assert create_palindrome_mirror("a") == "aa"

def test_with_numbers():
    """Test string with numbers."""
    assert create_palindrome_mirror("123") == "123321"

def test_with_spaces():
    """Test string with spaces."""
    assert create_palindrome_mirror("hello world") == "hello worlddlrow olleh"

def test_with_special_characters():
    """Test string with special characters."""
    assert create_palindrome_mirror("hi!@#") == "hi!@#@#!ih"

def test_invalid_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
        create_palindrome_mirror(None)
        create_palindrome_mirror(["not", "a", "string"])

def test_palindrome_mirror_calculation():
    """Test the palindrome mirror creation logic."""
    def palindrome_mirror(s):
        return s + s[::-1]
    
    test_cases = [
        "abc",
        "hello",
        "123",
        "!@#",
        ""
    ]
    
    for case in test_cases:
        assert create_palindrome_mirror(case) == palindrome_mirror(case)