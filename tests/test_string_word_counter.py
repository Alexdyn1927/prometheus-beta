import pytest
from src.string_word_counter import count_words

def test_default_separator():
    """Test word count with default space separator."""
    assert count_words("hello world") == 2
    assert count_words("one two three four") == 4

def test_custom_separator():
    """Test word count with custom separators."""
    assert count_words("apple,banana,cherry", separator=",") == 3
    assert count_words("x:y:z", separator=":") == 3

def test_empty_string():
    """Test word count for empty string."""
    assert count_words("") == 0

def test_single_word():
    """Test word count for single word."""
    assert count_words("hello") == 1
    assert count_words("python", separator=",") == 1

def test_multiple_separators():
    """Test word count with multiple consecutive separators."""
    assert count_words("a,,b,,c", separator=",,") == 3

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(123)
    
    with pytest.raises(TypeError, match="Separator must be a string"):
        count_words("hello", separator=123)

def test_empty_separator():
    """Test error handling for empty separator."""
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        count_words("hello", separator="")