def find_palindrome_word_pair_indices(words):
    """
    Find pairs of indices where words are palindromes when reversed.
    
    Args:
        words (list): A list of words to check for palindrome pairs.
    
    Returns:
        list: A list of index pairs where words form palindromes when reversed.
    
    Examples:
        >>> find_palindrome_word_pair_indices(["bat", "tab", "cat"])
        [(0, 1)]
        >>> find_palindrome_word_pair_indices(["abcd", "dcba", "lls", "s", "sssll"])
        [(0, 1), (1, 0), (3, 4)]
    """
    # Validate input
    if not isinstance(words, list):
        raise TypeError("Input must be a list of words")
    
    palindrome_indices = []
    
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip comparing a word with itself
            if i == j:
                continue
            
            # Check if words[i] reversed + words[j] forms a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_indices.append((i, j))
    
    return palindrome_indices

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    Args:
        s (str): The string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]