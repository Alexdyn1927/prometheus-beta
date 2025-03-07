"""
Unit tests for LZC compression and decompression functions.
"""

import pytest
import random
from src.lzc_compression import lzc_compress, lzc_decompress

def test_simple_compression_decompression():
    """Test basic compression and decompression with simple input."""
    original_data = b'ABCABCABCABC'
    compressed = lzc_compress(original_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original_data

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzc_compress(b'')
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzc_decompress(b'')

def test_invalid_input_type():
    """Test that non-bytes input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzc_compress('not bytes')
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        lzc_decompress('not bytes')

def test_random_data_compression():
    """Test compression and decompression with random data."""
    # Generate a random byte array
    random.seed(42)  # For reproducibility
    original_data = bytes(random.randint(0, 255) for _ in range(1000))
    
    compressed = lzc_compress(original_data)
    decompressed = lzc_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)  # Compression should reduce size

def test_repeated_pattern_compression():
    """Test compression of highly repetitive data."""
    original_data = b'AAAAAAAAAABBBBBBBBBBCCCCCCCCCC' * 10
    compressed = lzc_compress(original_data)
    decompressed = lzc_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)  # Compression should significantly reduce size

def test_edge_cases():
    """Test various edge cases."""
    # Single byte input
    single_byte = b'A'
    compressed = lzc_compress(single_byte)
    assert lzc_decompress(compressed) == single_byte

    # All unique bytes
    unique_bytes = bytes(range(256))
    compressed = lzc_compress(unique_bytes)
    assert lzc_decompress(compressed) == unique_bytes

def test_invalid_compressed_data():
    """Test handling of invalid compressed data."""
    # Odd-length compressed data
    with pytest.raises(ValueError, match="Compressed data must have an even length"):
        lzc_decompress(b'\x01')

    # Invalid code in compressed data
    with pytest.raises(ValueError, match="Invalid compressed data"):
        lzc_decompress(b'\xFF\xFF\xFF\xFF')  # Impossible code