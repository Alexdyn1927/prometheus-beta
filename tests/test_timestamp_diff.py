import pytest
from src.timestamp_diff import calculate_timestamp_difference

def test_positive_time_difference():
    result = calculate_timestamp_difference(
        '2023-01-01 10:00:00', 
        '2023-01-01 11:30:30'
    )
    assert result['total_seconds'] == 5430
    assert result['days'] == 0
    assert result['hours'] == 1
    assert result['minutes'] == 30
    assert result['seconds'] == 30
    assert result['is_negative'] == False

def test_negative_time_difference():
    result = calculate_timestamp_difference(
        '2023-01-01 11:30:30', 
        '2023-01-01 10:00:00'
    )
    assert result['total_seconds'] == -5430
    assert result['days'] == 0
    assert result['hours'] == 1
    assert result['minutes'] == 30
    assert result['seconds'] == 30
    assert result['is_negative'] == True

def test_multi_day_difference():
    result = calculate_timestamp_difference(
        '2023-01-01 00:00:00', 
        '2023-01-03 12:30:45'
    )
    assert result['total_seconds'] == 216645
    assert result['days'] == 2
    assert result['hours'] == 12
    assert result['minutes'] == 30
    assert result['seconds'] == 45
    assert result['is_negative'] == False

def test_custom_format():
    result = calculate_timestamp_difference(
        '01/01/2023 10:00:00', 
        '01/01/2023 11:30:30', 
        format='%m/%d/%Y %H:%M:%S'
    )
    assert result['total_seconds'] == 5430

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference(
            'invalid-format', 
            '2023-01-01 11:30:30'
        )

def test_different_date_formats():
    result = calculate_timestamp_difference(
        '2022-12-31 23:59:59', 
        '2023-01-01 00:00:00'
    )
    assert result['total_seconds'] == 1
    assert result['days'] == 0
    assert result['hours'] == 0
    assert result['minutes'] == 0
    assert result['seconds'] == 1
    assert result['is_negative'] == False