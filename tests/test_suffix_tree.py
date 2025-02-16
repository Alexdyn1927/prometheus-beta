import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    text = "banana"
    suffix_tree = SuffixTree(text)
    assert suffix_tree.text == "banana$"
    assert suffix_tree.root is not None

def test_search_pattern():
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Test existing patterns
    assert suffix_tree.search("ban") == True
    assert suffix_tree.search("ana") == True
    assert suffix_tree.search("banana") == True
    
    # Test non-existing patterns
    assert suffix_tree.search("banan") == False
    assert suffix_tree.search("apple") == False
    assert suffix_tree.search("") == False

def test_find_all_occurrences():
    text = "bananabanana"
    suffix_tree = SuffixTree(text)
    
    # Test pattern with multiple occurrences
    assert suffix_tree.find_all_occurrences("banana") == [0, 6]
    assert suffix_tree.find_all_occurrences("ana") == [1, 3, 7, 9]
    
    # Test pattern with single occurrence
    assert suffix_tree.find_all_occurrences("ban") == [0, 6]
    
    # Test non-existing pattern
    assert suffix_tree.find_all_occurrences("apple") == []
    assert suffix_tree.find_all_occurrences("") == []

def test_edge_cases():
    # Test with empty string
    suffix_tree = SuffixTree("")
    assert suffix_tree.search("") == False
    assert suffix_tree.find_all_occurrences("test") == []

    # Test with single character
    suffix_tree = SuffixTree("a")
    assert suffix_tree.search("a") == True
    assert suffix_tree.find_all_occurrences("a") == [0]