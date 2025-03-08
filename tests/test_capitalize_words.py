import pytest
from src.capitalize_words import capitalize_comma_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_comma_words('hello,world') == 'Hello,World'

def test_already_capitalized():
    """Test string with already capitalized words."""
    assert capitalize_comma_words('Hello,World') == 'Hello,World'

def test_multiple_words():
    """Test capitalization of multiple words."""
    assert capitalize_comma_words('python,is,awesome') == 'Python,Is,Awesome'

def test_empty_string():
    """Test empty string input."""
    assert capitalize_comma_words('') == ''

def test_single_word():
    """Test single word input."""
    assert capitalize_comma_words('python') == 'Python'

def test_invalid_input_with_whitespace():
    """Test that whitespace raises a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words('hello world')

def test_invalid_input_with_punctuation():
    """Test that punctuation raises a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words('hello.world')

def test_invalid_input_with_numbers():
    """Test that numbers raise a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words('hello123,world')