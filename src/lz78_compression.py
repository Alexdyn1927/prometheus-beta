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
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string as a special case
    if not input_string:
        return []
    
    # Initialize dictionary and compression result
    dictionary = {0: ""}
    compressed = []
    current_index = 1
    
    # Current prefix to search in dictionary
    current_prefix = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Attempt to extend current prefix
        current_search = current_prefix + char
        
        # If current search is in dictionary, update current prefix
        if current_search in dictionary.values():
            current_prefix = current_search
        else:
            # Find the index of the current prefix
            prefix_index = next((k for k, v in dictionary.items() if v == current_prefix), 0)
            
            # Add to compressed output
            compressed.append((prefix_index, char))
            
            # Add to dictionary
            dictionary[current_index] = current_search
            current_index += 1
            
            # Reset current prefix
            current_prefix = ""
    
    # Handle any remaining prefix
    if current_prefix:
        prefix_index = next((k for k, v in dictionary.items() if v == current_prefix), 0)
        compressed.append((prefix_index, ''))
    
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
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    # Handle empty input
    if not compressed_data:
        return ""
    
    # Initialize dictionary and decompressed string
    dictionary = {0: ""}
    decompressed = []
    current_index = 1
    
    # Decompress each tuple
    for idx, char in compressed_data:
        # Get the prefix from dictionary
        prefix = dictionary.get(idx, "")
        
        # Construct current string
        current_string = prefix + char
        decompressed.append(current_string)
        
        # Add to dictionary if not the first entry
        if idx != 0:
            dictionary[current_index] = current_string
            current_index += 1
    
    return ''.join(decompressed)