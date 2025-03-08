import pytest
from src.text_analysis import count_vowels_consonants

def test_basic_text_counting():
    """Test counting vowels and consonants in a basic text."""
    assert count_vowels_consonants("hello") == (2, 3)

def test_mixed_case_text():
    """Test that function works with mixed case text."""
    assert count_vowels_consonants("HeLLo WoRLd") == (3, 6)

def test_empty_string():
    """Test that empty string returns (0, 0)."""
    assert count_vowels_consonants("") == (0, 0)

def test_only_vowels():
    """Test a string with only vowels."""
    assert count_vowels_consonants("aeiouAEIOU") == (10, 0)

def test_only_consonants():
    """Test a string with only consonants."""
    assert count_vowels_consonants("bcdfghjklmnpqrstvwxyz") == (0, 21)

def test_non_alphabetic_characters():
    """Test that non-alphabetic characters are ignored."""
    assert count_vowels_consonants("hello 123! @#$%") == (2, 3)

def test_unicode_characters():
    """Test that non-English characters are ignored."""
    assert count_vowels_consonants("héllö wörld") == (2, 3)

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
        count_vowels_consonants(None)
        count_vowels_consonants(["hello"])