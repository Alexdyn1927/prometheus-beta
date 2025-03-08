import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic_cases():
    """Test basic cases of Fibonacci sum function."""
    assert fibonacci_sum(1) == 0, "Sum of first 1 Fibonacci number should be 0"
    assert fibonacci_sum(2) == 1, "Sum of first 2 Fibonacci numbers should be 1"
    assert fibonacci_sum(3) == 2, "Sum of first 3 Fibonacci numbers should be 2"
    assert fibonacci_sum(4) == 4, "Sum of first 4 Fibonacci numbers should be 4"
    assert fibonacci_sum(5) == 7, "Sum of first 5 Fibonacci numbers should be 7"

def test_fibonacci_sum_larger_numbers():
    """Test Fibonacci sum for larger number of terms."""
    assert fibonacci_sum(10) == 88, "Sum of first 10 Fibonacci numbers should be 88"
    assert fibonacci_sum(15) == 1597, "Sum of first 15 Fibonacci numbers should be 1597"

def test_fibonacci_sum_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("5")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(None)