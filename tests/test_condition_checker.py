import pytest
from src.condition_checker import check_conditions

def test_check_conditions_single_true():
    """Test single true condition passes"""
    assert check_conditions(True) is True

def test_check_conditions_multiple_true():
    """Test multiple true conditions pass"""
    assert check_conditions(True, True, True) is True

def test_check_conditions_with_custom_message():
    """Test condition with custom error message"""
    assert check_conditions((1 == 1, "Custom message")) is True

def test_check_conditions_multiple_with_custom_messages():
    """Test multiple conditions with custom messages"""
    assert check_conditions((1 == 1, "First message"), (2 > 1, "Second message")) is True

def test_check_conditions_single_false():
    """Test single false condition raises AssertionError"""
    with pytest.raises(AssertionError):
        check_conditions(False)

def test_check_conditions_multiple_with_false():
    """Test multiple conditions with a false condition raises AssertionError"""
    with pytest.raises(AssertionError):
        check_conditions(True, False, True)

def test_check_conditions_custom_false_message():
    """Test false condition with custom error message"""
    with pytest.raises(AssertionError, match="Custom error"):
        check_conditions((False, "Custom error"))

def test_check_conditions_mixed_conditions():
    """Test mixed true and false conditions"""
    with pytest.raises(AssertionError):
        check_conditions(True, (False, "Error"), True)

def test_check_conditions_no_arguments():
    """Test function with no arguments"""
    assert check_conditions() is True