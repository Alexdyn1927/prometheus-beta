import pytest
from src.palindrome_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("radar is a palindrome") == True
    assert contains_palindrome_word("Hello level world") == True
    assert contains_palindrome_word("A man racecar") == True
    
    # Test cases without palindrome words
    assert contains_palindrome_word("Hello world") == False
    assert contains_palindrome_word("") == False
    
    # Test cases with mixed content
    assert contains_palindrome_word("123 bob 456") == True
    assert contains_palindrome_word("Special ch@r@cters radar") == True
    
    # Test case sensitivity
    assert contains_palindrome_word("Madam") == True
    
    # Test edge cases
    assert contains_palindrome_word("a") == True  # Single character is a palindrome
    assert contains_palindrome_word("ab") == False  # Two different characters
    
    # Test with punctuation and special characters
    assert contains_palindrome_word("Hello, madam! How are you?") == True
    assert contains_palindrome_word("12345 special chars 54321") == False