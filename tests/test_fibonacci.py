"""
Tests for the extended Fibonacci sequence generator.
"""

import pytest
import math
import sys
sys.path.append('.')

from src.fibonacci import extended_fibonacci

def test_positive_indices():
    """Test Fibonacci sequence for positive integer indices."""
    assert extended_fibonacci(0) == 0
    assert extended_fibonacci(1) == 1
    assert extended_fibonacci(2) == 1
    assert extended_fibonacci(3) == 2
    assert extended_fibonacci(4) == 3
    assert extended_fibonacci(5) == 5
    assert extended_fibonacci(6) == 8

def test_negative_indices():
    """Test Fibonacci sequence for negative integer indices."""
    assert extended_fibonacci(-1) == 1
    assert extended_fibonacci(-2) == -1
    assert extended_fibonacci(-3) == 2
    assert extended_fibonacci(-4) == -3
    assert extended_fibonacci(-5) == 5

def test_float_indices():
    """Test Fibonacci sequence for float indices."""
    # Check interpolation
    assert math.isclose(extended_fibonacci(1.5), 1.5, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(2.5), 2.5, rel_tol=1e-9)
    
    # Test some known interpolated values
    assert math.isclose(extended_fibonacci(0.5), 0.5, rel_tol=1e-9)
    assert math.isclose(extended_fibonacci(-1.5), -1.5, rel_tol=1e-9)

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        extended_fibonacci(None)
    with pytest.raises(TypeError):
        extended_fibonacci("not a number")
    with pytest.raises(TypeError):
        extended_fibonacci([1, 2, 3])