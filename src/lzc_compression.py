"""
Lempel-Ziv-Clearwater (LZC) Compression Algorithm Implementation.

This module provides functions for LZC compression and decompression.
"""

def lzc_compress(input_data):
    """
    Compress input data using the Lempel-Ziv-Clearwater (LZC) compression algorithm.
    
    Args:
        input_data (bytes or bytearray): The data to be compressed.
    
    Returns:
        bytearray: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or bytearray.
        ValueError: If input is empty.
    """
    # Input validation
    if not isinstance(input_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Initialize compression dictionary and variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    max_dict_size = 65536  # Limit dictionary size to 16-bit codes
    
    # Compression variables
    result = bytearray()
    current_sequence = bytes([input_data[0]])
    
    # Compress the input data
    for byte in input_data[1:]:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If sequence exists, continue building it
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            result.extend(dictionary[current_sequence].to_bytes(2, 'big'))
            
            # Add new sequence to dictionary if not full
            if next_code < max_dict_size:
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output the last sequence
    result.extend(dictionary[current_sequence].to_bytes(2, 'big'))
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data compressed with the Lempel-Ziv-Clearwater (LZC) compression algorithm.
    
    Args:
        compressed_data (bytes or bytearray): The data to be decompressed.
    
    Returns:
        bytearray: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes or bytearray.
        ValueError: If input is empty or has an odd length.
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    if len(compressed_data) % 2 != 0:
        raise ValueError("Compressed data must have an even length")
    
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    max_dict_size = 65536  # Limit dictionary size to 16-bit codes
    
    # Decompression variables
    result = bytearray()
    previous_code = int.from_bytes(compressed_data[:2], 'big')
    result.extend(dictionary[previous_code])
    
    # Decompress the data
    for i in range(2, len(compressed_data), 2):
        current_code = int.from_bytes(compressed_data[i:i+2], 'big')
        
        # Retrieve current sequence
        if current_code in dictionary:
            current_sequence = dictionary[current_code]
        elif current_code == next_code:
            # Special case: code not yet in dictionary
            current_sequence = dictionary[previous_code] + bytes([dictionary[previous_code][0]])
        else:
            raise ValueError(f"Invalid compressed data at index {i}")
        
        # Add current sequence to result
        result.extend(current_sequence)
        
        # Add new dictionary entry if not full
        if next_code < max_dict_size:
            dictionary[next_code] = dictionary[previous_code] + bytes([current_sequence[0]])
            next_code += 1
        
        # Update previous code
        previous_code = current_code
    
    return result