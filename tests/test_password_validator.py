import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test a password that meets all requirements"""
    assert validate_password("StrongP@ss123") == True

def test_too_short_password():
    """Test password that is too short"""
    assert validate_password("Short1!") == False

def test_too_long_password():
    """Test password that is too long"""
    assert validate_password("A" * 65 + "1!") == False

def test_missing_uppercase():
    """Test password without uppercase letter"""
    assert validate_password("lowercase1!") == False

def test_missing_lowercase():
    """Test password without lowercase letter"""
    assert validate_password("UPPERCASE1!") == False

def test_missing_digit():
    """Test password without a digit"""
    assert validate_password("NoDigitPass!") == False

def test_missing_special_char():
    """Test password without a special character"""
    assert validate_password("NoSpecialChar123") == False

def test_non_string_input():
    """Test non-string input"""
    assert validate_password(12345) == False
    assert validate_password(None) == False

def test_edge_case_special_chars():
    """Test various special characters"""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in special_chars:
        password = f"ValidPass1{char}"
        assert validate_password(password) == True

def test_minimum_valid_password():
    """Test a password at the minimum length with all requirements"""
    assert validate_password("aA1!2345") == True

def test_maximum_valid_password():
    """Test a password at the maximum length with all requirements"""
    assert validate_password("A" * 30 + "1!" + "a" * 30) == True