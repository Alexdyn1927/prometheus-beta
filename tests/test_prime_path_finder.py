import pytest
from src.prime_path_finder import find_prime_path, is_prime

def test_is_prime():
    """Test primality checking function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(4) == False
    assert is_prime(15) == False

def test_find_prime_path_basic():
    """Test finding a simple prime path."""
    grid = [
        [1, 1, 3],
        [7, 3, 1],
        [2, 2, 1]
    ]
    path = find_prime_path(grid)
    assert len(path) > 1
    
    # Convert path to number
    path_number = int(''.join(str(grid[r][c]) for r, c in path))
    assert is_prime(path_number)

def test_find_prime_path_complex():
    """Test a more complex grid with potential prime paths."""
    grid = [
        [1, 1, 3, 7],
        [2, 3, 1, 9],
        [5, 2, 3, 1]
    ]
    path = find_prime_path(grid)
    assert len(path) > 1
    
    # Convert path to number
    path_number = int(''.join(str(grid[r][c]) for r, c in path))
    assert is_prime(path_number)

def test_find_prime_path_no_prime_path():
    """Test grid with no valid prime path."""
    grid = [
        [4, 6, 8],
        [9, 0, 2],
        [1, 5, 3]
    ]
    path = find_prime_path(grid)
    assert path == []

def test_find_prime_path_empty_grid():
    """Test handling of empty grid."""
    with pytest.raises(ValueError):
        find_prime_path([])
    with pytest.raises(ValueError):
        find_prime_path([[]])

def test_find_prime_path_single_cell_prime():
    """Test single cell prime path scenario."""
    grid = [[2]]
    path = find_prime_path(grid)
    assert path == [(0, 0)]

def test_find_prime_path_single_cell_non_prime():
    """Test single cell non-prime path scenario."""
    grid = [[4]]
    path = find_prime_path(grid)
    assert path == []