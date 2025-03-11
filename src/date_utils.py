from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.

    Args:
        date (datetime or str): The starting date. 
            If a string, it should be in ISO format (YYYY-MM-DD).
        days (int): Number of days to add. Can be positive or negative.

    Returns:
        datetime: A new datetime object with days added.

    Raises:
        TypeError: If date is not a datetime or valid date string.
        ValueError: If days is not an integer.
    """
    # Validate input types
    if not isinstance(days, int):
        raise ValueError("Days must be an integer")

    # Convert string to datetime if needed
    if isinstance(date, str):
        try:
            date = datetime.fromisoformat(date)
        except ValueError:
            raise TypeError("Date must be a datetime object or a string in ISO format (YYYY-MM-DD)")
    
    # Validate date is a datetime object
    if not isinstance(date, datetime):
        raise TypeError("Date must be a datetime object or a string in ISO format (YYYY-MM-DD)")

    # Add days and return new date
    return date + timedelta(days=days)