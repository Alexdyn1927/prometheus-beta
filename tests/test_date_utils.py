import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 10)
    assert result == datetime(2023, 1, 11)

def test_add_days_to_date_string():
    """Test adding days to a date string."""
    base_date = "2023-01-01"
    result = add_days_to_date(base_date, 10)
    assert result == datetime(2023, 1, 11)

def test_subtract_days():
    """Test subtracting days."""
    base_date = datetime(2023, 1, 15)
    result = add_days_to_date(base_date, -5)
    assert result == datetime(2023, 1, 10)

def test_zero_days():
    """Test adding zero days."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 0)
    assert result == base_date

def test_invalid_date_type():
    """Test that an invalid date type raises a TypeError."""
    with pytest.raises(TypeError):
        add_days_to_date(123, 10)

def test_invalid_date_string():
    """Test that an invalid date string raises a TypeError."""
    with pytest.raises(TypeError):
        add_days_to_date("not-a-date", 10)

def test_invalid_days_type():
    """Test that non-integer days raises a ValueError."""
    with pytest.raises(ValueError):
        add_days_to_date(datetime(2023, 1, 1), "10")

def test_leap_year():
    """Test adding days across a leap year boundary."""
    base_date = datetime(2020, 2, 28)
    result = add_days_to_date(base_date, 1)
    assert result == datetime(2020, 2, 29)

def test_large_day_addition():
    """Test adding a large number of days."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 365)
    assert result == datetime(2024, 1, 1)