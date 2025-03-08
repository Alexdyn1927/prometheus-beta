def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on players and goals.

    Args:
        team1_players (int): Number of players on team 1
        team2_players (int): Number of players on team 2
        team1_goals (int): Number of goals scored by team 1
        team2_goals (int): Number of goals scored by team 2

    Returns:
        str: The result of the match ('Team 1 Wins', 'Team 2 Wins', or 'Draw')

    Raises:
        ValueError: If any of the input parameters are negative or not integers
    """
    # Validate input types
    if not all(isinstance(x, int) for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be integers")
    
    # Validate input values are non-negative
    if any(x < 0 for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be non-negative")
    
    # Condition 1: Team with more goals wins
    if team1_goals > team2_goals:
        return 'Team 1 Wins'
    elif team2_goals > team1_goals:
        return 'Team 2 Wins'
    
    # Condition 2: If goals are equal, team with fewer players wins
    if team1_players < team2_players:
        return 'Team 1 Wins'
    elif team2_players < team1_players:
        return 'Team 2 Wins'
    
    # If both goals and players are equal, it's a draw
    return 'Draw'