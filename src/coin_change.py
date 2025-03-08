def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): List of available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make the amount
             Returns -1 if the amount cannot be made with given coins
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive integers")
    
    # Handle trivial cases
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    # Sort coins in descending order to optimize
    coins.sort(reverse=True)
    
    # Dynamic programming solution
    # Create DP table initialized with a large value
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, -1 if amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1