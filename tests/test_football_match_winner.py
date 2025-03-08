import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    """Test Team 1 wins by scoring more goals"""
    assert determine_football_match_winner(11, 11, 3, 2) == 'Team 1 Wins'

def test_team2_wins_by_goals():
    """Test Team 2 wins by scoring more goals"""
    assert determine_football_match_winner(11, 11, 2, 3) == 'Team 2 Wins'

def test_team1_wins_by_fewer_players():
    """Test Team 1 wins when goals are equal but has fewer players"""
    assert determine_football_match_winner(10, 11, 2, 2) == 'Team 1 Wins'

def test_team2_wins_by_fewer_players():
    """Test Team 2 wins when goals are equal but has fewer players"""
    assert determine_football_match_winner(11, 10, 2, 2) == 'Team 2 Wins'

def test_draw_equal_goals_and_players():
    """Test draw when goals and players are equal"""
    assert determine_football_match_winner(11, 11, 2, 2) == 'Draw'

def test_invalid_negative_inputs():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All inputs must be non-negative"):
        determine_football_match_winner(-1, 11, 2, 2)
    with pytest.raises(ValueError, match="All inputs must be non-negative"):
        determine_football_match_winner(11, 11, -1, 2)

def test_invalid_input_types():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11.5, 11, 2, 2)
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11, 11, '2', 2)
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11, 11, 2, None)