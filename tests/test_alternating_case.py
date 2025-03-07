import pytest
from src.alternating_case import to_alternating_case

def test_basic_alternating_case():
    """Test basic string conversion to alternating case."""
    assert to_alternating_case("hello world") == "HeLlO wOrLd"

def test_empty_string():
    """Test empty string input."""
    assert to_alternating_case("") == ""

def test_single_character():
    """Test single character input."""
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("b") == "B"

def test_multiple_words():
    """Test multiple words input."""
    assert to_alternating_case("python is awesome") == "PyThOn Is AwEsOmE"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_case("MiXeD CaSe") == "MiXeD cAsE"

def test_special_characters():
    """Test input with special characters."""
    assert to_alternating_case("hello, world!") == "HeLlO, wOrLd!"

def test_error_non_string_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_case(None)