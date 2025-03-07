"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based lossless compression algorithm that builds a 
dynamic dictionary of previously seen substrings during compression.
"""

from typing import List, Tuple


def lz78_compress(input_string: str) -> List[Tuple[int, str]]:
    """
    Compress the input string using the LZ78 compression algorithm.
    
    Args:
        input_string (str): The string to be compressed
    
    Returns:
        List[Tuple[int, str]]: A list of tuples (dictionary_index, next_character)
        
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary and compression result
    dictionary = {}
    compressed = []
    current_index = 1
    
    # Current prefix to search in dictionary
    current_prefix = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Attempt to extend current prefix
        current_search = current_prefix + char
        
        # If current search is in dictionary, update current prefix
        if current_search in dictionary:
            current_prefix = current_search
        else:
            # If not in dictionary, add new entry
            # Find the index of the current prefix or 0 if not found
            prefix_index = dictionary.get(current_prefix, 0)
            
            # Add to compressed output and dictionary
            compressed.append((prefix_index, char))
            dictionary[current_search] = current_index
            current_index += 1
            
            # Reset current prefix
            current_prefix = ""
    
    # Handle any remaining prefix
    if current_prefix:
        compressed.append((dictionary.get(current_prefix, 0), ''))
    
    return compressed


def lz78_decompress(compressed_data: List[Tuple[int, str]]) -> str:
    """
    Decompress data that was compressed using the LZ78 algorithm.
    
    Args:
        compressed_data (List[Tuple[int, str]]): Compressed data to decompress
    
    Returns:
        str: The original decompressed string
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If input contains invalid compression data
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    if not compressed_data:
        return ""
    
    # Initialize dictionary and decompressed string
    dictionary = {0: ""}
    decompressed = []
    current_index = 1
    
    # Decompress each tuple
    for idx, char in compressed_data:
        # Get the prefix from dictionary
        prefix = dictionary.get(idx, None)
        
        if prefix is None:
            raise ValueError(f"Invalid compression data: index {idx} not found")
        
        # Construct current string
        current_string = prefix + char
        decompressed.append(current_string)
        
        # Add to dictionary if not the first entry
        if idx != 0:
            dictionary[current_index] = prefix + char[0]
            current_index += 1
    
    return ''.join(decompressed)