"""
Tests for LZP Compression Algorithm
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzp_compression import LZPCompressor

def test_lzp_compressor_initialization():
    """Test compressor initialization"""
    compressor = LZPCompressor()
    assert compressor.context_length == 8
    
    compressor_custom = LZPCompressor(context_length=4)
    assert compressor_custom.context_length == 4

def test_invalid_context_length():
    """Test invalid context length initialization"""
    with pytest.raises(ValueError):
        LZPCompressor(context_length=0)
    with pytest.raises(ValueError):
        LZPCompressor(context_length=-1)

def test_empty_compression():
    """Test compression of empty input"""
    compressor = LZPCompressor()
    assert compressor.compress(b'') == b''
    assert compressor.compress('') == b''

def test_string_input_compression():
    """Test compression with string input"""
    compressor = LZPCompressor()
    input_str = "hello world"
    compressed = compressor.compress(input_str)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == input_str

def test_byte_input_compression():
    """Test compression with byte input"""
    compressor = LZPCompressor()
    input_bytes = b'hello world'
    compressed = compressor.compress(input_bytes)
    decompressed = compressor.decompress(compressed)
    assert decompressed == input_bytes

def test_repeated_pattern_compression():
    """Test compression of repeated patterns"""
    compressor = LZPCompressor()
    input_data = b'aaaaaaaaaabbbbbbbbbb'
    compressed = compressor.compress(input_data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == input_data

def test_complex_input_compression():
    """Test compression of more complex input"""
    compressor = LZPCompressor()
    input_data = b'the quick brown fox jumps over the lazy dog'
    compressed = compressor.compress(input_data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == input_data

def test_invalid_input_types():
    """Test compression with invalid input types"""
    compressor = LZPCompressor()
    
    with pytest.raises(TypeError):
        compressor.compress(123)
    
    with pytest.raises(TypeError):
        compressor.decompress(123)

def test_round_trip_compression():
    """Test full round-trip compression and decompression"""
    test_cases = [
        b'hello world',
        b'repeated repeated repeated',
        b'',
        b'single',
        b'\x00\x01\x02\x03\x04'
    ]
    
    for test_input in test_cases:
        compressor = LZPCompressor()
        compressed = compressor.compress(test_input)
        decompressed = compressor.decompress(compressed)
        assert decompressed == test_input, f"Failed for input: {test_input}"