import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_non_palindromes():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False

def test_case_insensitive():
    """Test that palindrome check is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Level") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_with_punctuation_and_spaces():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_empty_and_single_char():
    """Test empty string and single character inputs."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])