import pytest
from src.phone_validator import validate_phone_number

def test_valid_phone_number_formats():
    """Test valid phone number formats"""
    # Test format 1: (123) 456-7890
    assert validate_phone_number('(123) 456-7890') == True
    
    # Test format 2: 123-456-7890
    assert validate_phone_number('123-456-7890') == True
    
    # Test format 3: 123 456 7890
    assert validate_phone_number('123 456 7890') == True

def test_invalid_phone_number_formats():
    """Test invalid phone number formats"""
    # Test incomplete numbers
    assert validate_phone_number('(123) 456-789') == False
    assert validate_phone_number('123-456-789') == False
    assert validate_phone_number('123 456 789') == False
    
    # Test incorrect separators
    assert validate_phone_number('(123)456-7890') == False
    assert validate_phone_number('123/456/7890') == False
    
    # Test non-numeric characters
    assert validate_phone_number('(abc) def-ghij') == False
    
    # Test empty string
    assert validate_phone_number('') == False
    
    # Test extra characters
    assert validate_phone_number('(123) 456-7890 ext') == False
    
def test_whitespace_handling():
    """Test handling of surrounding whitespace"""
    assert validate_phone_number('  (123) 456-7890  ') == True
    assert validate_phone_number('  123-456-7890  ') == True
    assert validate_phone_number('  123 456 7890  ') == True