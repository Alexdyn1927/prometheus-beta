import pytest
from src.string_digit_checker import is_digit_string

def test_is_digit_string():
    # Test strings with only digits
    assert is_digit_string("12345") == True
    assert is_digit_string("0") == True
    
    # Test strings with non-digit characters
    assert is_digit_string("123abc") == False
    assert is_digit_string("abc") == False
    
    # Test strings with spaces or special characters
    assert is_digit_string("123 ") == False
    assert is_digit_string(" 123") == False
    assert is_digit_string("12.34") == False
    
    # Test empty string and None
    assert is_digit_string("") == False
    assert is_digit_string(None) == False