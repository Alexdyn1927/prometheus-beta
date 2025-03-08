import pytest
from src.string_reverser import reverse_string

def test_reverse_simple_string():
    """Test reversing a simple string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multiword_string():
    """Test reversing a multi-word string."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_with_numbers():
    """Test reversing a string with numbers."""
    assert reverse_string("abc123") == "321cba"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)