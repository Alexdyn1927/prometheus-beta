import pytest
import re
from src.time_utils import get_current_time

def test_get_current_time_format():
    """
    Test that the returned time string matches HH:MM:SS format
    """
    current_time = get_current_time()
    
    # Check that the time is a string
    assert isinstance(current_time, str), "Return value should be a string"
    
    # Check the format using regex
    time_format_regex = r'^\d{2}:\d{2}:\d{2}$'
    assert re.match(time_format_regex, current_time), "Time should be in HH:MM:SS format"
    
    # Validate hours, minutes, seconds are in valid ranges
    hours, minutes, seconds = map(int, current_time.split(':'))
    assert 0 <= hours <= 23, "Hours should be between 0 and 23"
    assert 0 <= minutes <= 59, "Minutes should be between 0 and 59"
    assert 0 <= seconds <= 59, "Seconds should be between 0 and 59"