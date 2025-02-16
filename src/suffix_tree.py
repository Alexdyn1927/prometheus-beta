class SuffixTreeNode:
    def __init__(self):
        pass

class SuffixTree:
    def __init__(self, text):
        """
        Initialize a Suffix Tree for the given text.
        
        Args:
            text (str): The input text to build the suffix tree for.
        """
        self.text = text + '$'
        self.root = SuffixTreeNode()

    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): The pattern to search for.
        
        Returns:
            bool: True if pattern is found, False otherwise.
        """
        if not pattern:
            return False

        # Check if pattern is a prefix of any suffix
        return any(suffix.startswith(pattern) for suffix in [self.text[i:] for i in range(len(self.text))])

    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text.
        
        Args:
            pattern (str): The pattern to search for.
        
        Returns:
            list: Indices of all occurrences of the pattern.
        """
        if not pattern:
            return []

        return [i for i in range(len(self.text) - 1) if self.text[i:].startswith(pattern)]