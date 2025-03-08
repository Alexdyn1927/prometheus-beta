import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindrome inputs."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_case_insensitive():
    """Ensure the function is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True

def test_special_characters():
    """Test handling of special characters and spaces."""
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("a!b@c#c@b!a") == True
    assert is_palindrome("hello world") == False

def test_edge_cases():
    """Test edge cases and unusual inputs."""
    assert is_palindrome(" ") == True
    assert is_palindrome("  ") == True
    assert is_palindrome("!!") == True
    assert is_palindrome("a b") == False

def test_non_string_input():
    """Ensure the function handles non-string inputs appropriately."""
    with pytest.raises(AttributeError):
        is_palindrome(None)
    with pytest.raises(AttributeError):
        is_palindrome(123)