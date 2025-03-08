import pytest
from src.advanced_string_reversal import advanced_string_reversal

def test_basic_string_reversal():
    """Test basic string reversal."""
    assert advanced_string_reversal("hello") == "olleh"

def test_mixed_string_reversal():
    """Test mixed string with words and numbers."""
    assert advanced_string_reversal("hello123world") == "olleh321dlrow"

def test_palindrome_preservation():
    """Test that palindromes remain unchanged."""
    assert advanced_string_reversal("racecar") == "racecar"
    assert advanced_string_reversal("hello racecar world") == "olleh racecar dlrow"

def test_numbers_reversal():
    """Test number reversal."""
    assert advanced_string_reversal("123abc456") == "321abc654"

def test_mixed_content():
    """Test complex mixed content."""
    assert advanced_string_reversal("hello 123 world") == "olleh 321 dlrow"

def test_special_characters():
    """Test string with special characters."""
    assert advanced_string_reversal("hello, world! 123") == "olleh, dlrow! 321"

def test_empty_string():
    """Test empty string input."""
    assert advanced_string_reversal("") == ""

def test_non_string_input():
    """Test non-string input raises TypeError."""
    with pytest.raises(TypeError):
        advanced_string_reversal(123)

def test_whitespace_handling():
    """Test string with multiple types of whitespace."""
    assert advanced_string_reversal("  hello  123  ") == "  olleh  321  "

def test_unicode_characters():
    """Test handling of unicode characters."""
    assert advanced_string_reversal("résumé 123") == "émusér 321"