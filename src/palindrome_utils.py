def find_shortest_palindromic_substrings(s):
    """
    Find the shortest palindromic substrings in the given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list: A list of the shortest palindromic substrings found in the string
    """
    if not s:
        return []
    
    # Helper function to check if a substring is a palindrome
    def is_palindrome(substr):
        return substr == substr[::-1]
    
    # Find all shortest palindromic substrings
    shortest_palindromes = []
    min_length = float('inf')
    
    # Iterate through all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            
            # If it's a palindrome
            if is_palindrome(substr):
                # If it's shorter than current shortest, reset list
                if len(substr) < min_length:
                    shortest_palindromes = [substr]
                    min_length = len(substr)
                # If it's equal to current shortest, add to list
                elif len(substr) == min_length:
                    if substr not in shortest_palindromes:
                        shortest_palindromes.append(substr)
    
    return sorted(set(shortest_palindromes))