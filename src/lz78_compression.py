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
    dictionary = {"": 0}
    compressed = []
    current_index = 1
    
    # Current prefix to match
    current_prefix = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Attempt to extend current prefix
        test_prefix = current_prefix + char
        
        # If we've seen this prefix before, update current prefix
        if test_prefix in dictionary:
            current_prefix = test_prefix
        else:
            # Output current index and character for this new sequence
            compressed.append((dictionary[current_prefix], char))
            
            # Add this new sequence to dictionary
            dictionary[test_prefix] = current_index
            current_index += 1
            
            # Reset current prefix
            current_prefix = ""
    
    # Handle any remaining prefix
    if current_prefix:
        compressed.append((dictionary[current_prefix], ''))
    
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
    
    # Handle empty input 
    if not compressed_data:
        return ""
    
    # Initialize dictionary and result
    dictionary = {0: ""}
    result = []
    current_index = 1
    
    # Decompress each tuple
    for idx, char in compressed_data:
        # Validate index exists in dictionary
        if idx not in dictionary:
            raise ValueError(f"Invalid compression data: index {idx} not found")
        
        # Get the prefix string from dictionary
        prefix = dictionary[idx]
        
        # Construct current string 
        current_string = prefix + char
        result.append(current_string)
        
        # Add new entry to dictionary
        dictionary[current_index] = current_string
        current_index += 1
    
    return ''.join(result)