import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating a few known triangle numbers."""
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [0]
    assert generate_triangle_sequence(5) == [0, 1, 3, 6, 10]

def test_generate_triangle_sequence_full_sequence():
    """Test a longer sequence of triangle numbers."""
    expected = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    assert generate_triangle_sequence(10) == expected

def test_generate_triangle_sequence_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_invalid_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(None)