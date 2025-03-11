import pytest
from datetime import datetime
from src.date_utils import get_day_name

def test_get_day_name_string_input():
    """Test get_day_name with string input"""
    assert get_day_name('2023-06-21') == 'Wednesday'
    assert get_day_name('2023-12-25') == 'Monday'

def test_get_day_name_datetime_input():
    """Test get_day_name with datetime input"""
    date_obj = datetime(2023, 6, 21)
    assert get_day_name(date_obj) == 'Wednesday'

def test_get_day_name_invalid_string():
    """Test get_day_name with invalid string format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('21-06-2023')  # wrong format
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('2023/06/21')  # wrong separator

def test_get_day_name_invalid_input():
    """Test get_day_name with invalid input type"""
    with pytest.raises(ValueError, match="Input must be"):
        get_day_name(12345)  # invalid input type
    with pytest.raises(ValueError, match="Input must be"):
        get_day_name(None)  # None input

def test_get_day_name_boundary_dates():
    """Test get_day_name with boundary dates"""
    assert get_day_name('0001-01-01') == 'Monday'  # earliest possible date
    assert get_day_name('9999-12-31') == 'Friday'  # latest possible date