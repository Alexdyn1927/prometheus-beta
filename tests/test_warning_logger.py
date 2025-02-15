import pytest
import logging
import io
import sys
from src.warning_logger import log_warning

def test_log_warning_basic():
    """Test that a warning message is logged correctly."""
    # Capture console output
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    # Log a warning
    log_warning("Test warning message")
    
    # Reset redirect
    sys.stderr = sys.__stderr__
    
    # Check output contains the warning message
    assert "WARNING: Test warning message" in captured_output.getvalue()

def test_log_warning_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(123)
    
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(None)

def test_log_warning_empty_string():
    """Test logging an empty string."""
    # Capture console output
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    # Log an empty warning
    log_warning("")
    
    # Reset redirect
    sys.stderr = sys.__stderr__
    
    # Check output contains the warning message
    assert "WARNING:" in captured_output.getvalue()