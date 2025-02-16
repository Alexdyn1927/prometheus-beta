class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = -1
        self.end = -1
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, text):
        """
        Initialize a Suffix Tree for the given text.
        
        Args:
            text (str): The input text to build the suffix tree for.
        """
        self.text = text + '$'  # Append termination character
        self.root = SuffixTreeNode()
        self._build_suffix_tree()

    def _build_suffix_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm.
        """
        n = len(self.text)
        for i in range(n):
            self._extend_suffix_tree(i)

    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for the current phase.
        
        Args:
            phase (int): Current phase of suffix tree construction.
        """
        # Placeholder for Ukkonen's algorithm implementation
        pass

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

        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

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

        current = self.root
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]

        return self._collect_leaf_indices(current)

    def _collect_leaf_indices(self, node):
        """
        Collect all leaf indices starting from the given node.
        
        Args:
            node (SuffixTreeNode): Starting node to collect indices.
        
        Returns:
            list: Indices of all leaf nodes.
        """
        indices = []
        if node.suffix_index != -1:
            indices.append(node.suffix_index)
        
        for child in node.children.values():
            indices.extend(self._collect_leaf_indices(child))
        
        return indices