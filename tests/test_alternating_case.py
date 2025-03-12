import pytest
from src.alternating_case import to_alternating_case

def test_basic_alternating_case():
    """Test basic string conversion to alternating case."""
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("world") == "WoRlD"

def test_mixed_case_input():
    """Test that input with mixed case is correctly converted."""
    assert to_alternating_case("HeLLo") == "HeLlO"

def test_special_characters():
    """Test that special characters and spaces are preserved."""
    assert to_alternating_case("hello world!") == "HeLlO WoRlD!"

def test_empty_string():
    """Test empty string returns empty string."""
    assert to_alternating_case("") == ""

def test_single_character():
    """Test single character conversion."""
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("B") == "b"

def test_numbers_and_symbols():
    """Test conversion with numbers and symbols."""
    assert to_alternating_case("123!@#") == "123!@#"

def test_error_handling():
    """Test that non-string inputs raise TypeError."""
    with pytest.raises(TypeError):
        to_alternating_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_case(None)
    
    with pytest.raises(TypeError):
        to_alternating_case(["list"])