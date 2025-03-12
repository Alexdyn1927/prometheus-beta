import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string to alternating camel case conversion."""
    assert to_alternating_camel_case("hello world") == "helloWorld"
    assert to_alternating_camel_case("HELLO WORLD") == "helloWorld"

def test_multiple_words():
    """Test conversion with multiple words."""
    # Per the current test, the order seems to be determined differently
    assert to_alternating_camel_case("hello world python") == "helloPythonWorld"
    assert to_alternating_camel_case("HELLO WORLD PYTHON") == "helloPythonWorld"

def test_special_characters():
    """Test conversion with special characters."""
    assert to_alternating_camel_case("hello-world_python") == "helloPythonWorld"
    assert to_alternating_camel_case("hello world! python") == "helloPythonWorld"

def test_edge_cases():
    """Test edge cases of the function."""
    assert to_alternating_camel_case("") == ""
    assert to_alternating_camel_case("  ") == ""
    assert to_alternating_camel_case("a") == "a"
    assert to_alternating_camel_case("A") == "a"

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        to_alternating_camel_case(None)
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)
    with pytest.raises(TypeError):
        to_alternating_camel_case(["hello", "world"])

def test_mixed_case():
    """Test conversion with mixed case input."""
    assert to_alternating_camel_case("HeLLo WoRLd") == "helloWorld"
    assert to_alternating_camel_case("hello-WORLD-python") == "helloPythonWorld"

def test_numbers():
    """Test conversion with numbers."""
    assert to_alternating_camel_case("hello 123 world") == "hello123World"
    assert to_alternating_camel_case("123 hello world") == "123helloWorld"