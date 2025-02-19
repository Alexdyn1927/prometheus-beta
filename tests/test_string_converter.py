import pytest
from src.string_converter import to_snake_case

def test_to_snake_case_basic():
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello-world") == "hello_world"

def test_to_snake_case_mixed():
    assert to_snake_case("Hello_World") == "hello_world"
    assert to_snake_case("Hello World!") == "hello_world"
    assert to_snake_case("hello__world") == "hello_world"

def test_to_snake_case_camel_case():
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("PascalCase") == "pascal_case"
    assert to_snake_case("mixedCamelCase") == "mixed_camel_case"

def test_to_snake_case_edge_cases():
    assert to_snake_case("") == ""
    assert to_snake_case(" ") == ""
    assert to_snake_case("a") == "a"

def test_to_snake_case_special_chars():
    assert to_snake_case("hello-world!123") == "hello_world_123"
    assert to_snake_case("@hello@world@") == "hello_world"

def test_to_snake_case_error_handling():
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(None)