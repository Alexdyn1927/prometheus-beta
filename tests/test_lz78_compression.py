"""
Test suite for LZ78 Compression Algorithm
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress


def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original


def test_empty_string():
    """Test compression and decompression of an empty string"""
    original = ""
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original


def test_single_character():
    """Test compression and decompression of a single character"""
    original = "A"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original


def test_repeated_sequences():
    """Test compression of repeated sequences"""
    original = "ABABABABABABABAB"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original


def test_complex_string():
    """Test compression of a complex string with varied repetitions"""
    original = "hello world hello world hello"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original


def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        lz78_compress(123)
    
    with pytest.raises(TypeError):
        lz78_decompress("not a list")


def test_invalid_compression_data():
    """Test error handling for invalid compression data"""
    with pytest.raises(ValueError):
        lz78_decompress([(10, 'a')])  # Non-existent dictionary index


def test_compression_length_efficiency():
    """Test that compression reduces string length for repetitive sequences"""
    original = "ABCABCABCABC" * 10
    compressed = lz78_compress(original)
    assert len(compressed) < len(original)  # Compressed list should be shorter
    decompressed = lz78_decompress(compressed)
    assert decompressed == original


def test_unicode_support():
    """Test compression and decompression with Unicode characters"""
    original = "こんにちは世界 こんにちは世界"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original