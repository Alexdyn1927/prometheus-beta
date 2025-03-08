def count_vowels_consonants(text):
    """
    Count the number of vowels and consonants in a given text string.

    Args:
        text (str): The input text string to analyze.

    Returns:
        tuple: A tuple containing two integers (num_vowels, num_consonants).
               Returns (0, 0) for empty or non-alphabetic strings.

    Raises:
        TypeError: If input is not a string.
    """
    # Validate input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Convert to lowercase to simplify counting
    text = text.lower()

    # Define vowels
    vowels = set('aeiou')

    # Initialize counters
    num_vowels = 0
    num_consonants = 0

    # Count vowels and consonants
    for char in text:
        # Skip spaces and replace non-ASCII characters with their ASCII equivalent if possible
        try:
            # Convert to ASCII equivalent if possible
            char = char.encode('ascii', 'ignore').decode('ascii')
            
            # If character is now empty, skip it
            if not char:
                continue
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue

        # Only count alphabetic characters
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return (num_vowels, num_consonants)