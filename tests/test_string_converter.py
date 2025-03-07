import pytest
from src.string_converter import to_kebab_case

def test_basic_conversion():
    """Test basic string to kebab case conversion."""
    assert to_kebab_case("Hello World") == "hello-world"
    assert to_kebab_case("hello world") == "hello-world"

def test_snake_case_conversion():
    """Test conversion from snake_case to kebab-case."""
    assert to_kebab_case("snake_case_string") == "snake-case-string"

def test_camel_case_conversion():
    """Test conversion from camelCase to kebab-case."""
    assert to_kebab_case("camelCaseString") == "camel-case-string"
    assert to_kebab_case("PascalCaseString") == "pascal-case-string"

def test_mixed_case_conversion():
    """Test conversion of mixed case strings."""
    assert to_kebab_case("Mixed_Case String") == "mixed-case-string"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_kebab_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert to_kebab_case("hello") == "hello"

def test_multiple_separators():
    """Test conversion with multiple separators."""
    assert to_kebab_case("hello__world  test") == "hello-world-test"

def test_consecutive_uppercase():
    """Test conversion with consecutive uppercase letters."""
    assert to_kebab_case("HTTPRequest") == "http-request"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_kebab_case(None)
    
    with pytest.raises(TypeError):
        to_kebab_case(123)
    
    with pytest.raises(TypeError):
        to_kebab_case(["list"])