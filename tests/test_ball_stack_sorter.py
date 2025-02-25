import pytest
from src.ball_stack_sorter import BallStackSorter

def test_initial_invalid_stacks():
    """Test invalid initial stack configurations."""
    # Different length stacks
    with pytest.raises(ValueError, match="equal number of balls"):
        BallStackSorter([['Red', 'Blue'], ['Green'], ['Blue']])
    
    # Invalid colors
    with pytest.raises(ValueError, match="Balls must be Red, Blue, or Green"):
        BallStackSorter([['Red', 'Yellow'], ['Blue', 'Green'], ['Green', 'Red']])
    
    # Not exactly 3 stacks
    with pytest.raises(ValueError, match="Must provide exactly 3 stacks"):
        BallStackSorter([['Red'], ['Blue']])

def test_already_sorted_stacks():
    """Test scenario where stacks are already sorted."""
    sorter = BallStackSorter([
        ['Red', 'Red'], 
        ['Blue', 'Blue'], 
        ['Green', 'Green']
    ])
    sorted_stacks = sorter.sort()
    
    assert sorter.is_sorted()
    assert sorted_stacks == [
        ['Red', 'Red'], 
        ['Blue', 'Blue'], 
        ['Green', 'Green']
    ]

def test_mixed_color_sorting():
    """Test sorting of mixed color stacks."""
    sorter = BallStackSorter([
        ['Red', 'Blue'], 
        ['Green', 'Red'], 
        ['Blue', 'Green']
    ])
    sorted_stacks = sorter.sort()
    
    assert sorter.is_sorted()
    
    # Validate that each stack now has the same color
    for stack in sorted_stacks:
        assert len(set(stack)) <= 1

def test_moves_tracking():
    """Test that moves are tracked correctly."""
    sorter = BallStackSorter([
        ['Red', 'Blue'], 
        ['Green', 'Red'], 
        ['Blue', 'Green']
    ])
    sorter.sort()
    
    # Verify moves were recorded
    moves = sorter.get_moves()
    assert len(moves) > 0
    
    # Verify each move is between valid stack indices
    for move in moves:
        assert 0 <= move[0] < 3
        assert 0 <= move[1] < 3
        assert move[0] != move[1]

def test_edge_case_empty_stacks():
    """Test behavior with empty stacks."""
    sorter = BallStackSorter([
        [], [], []
    ])
    
    sorted_stacks = sorter.sort()
    assert sorter.is_sorted()
    assert sorted_stacks == [[], [], []]

def test_insufficient_sorting():
    """Test scenario where sorting is impossible."""
    # A contrived scenario that cannot be sorted
    with pytest.raises(ValueError, match="Unable to sort stacks"):
        sorter = BallStackSorter([
            ['Red', 'Green'], 
            ['Blue', 'Red'], 
            ['Green', 'Blue']
        ])
        sorter.sort()