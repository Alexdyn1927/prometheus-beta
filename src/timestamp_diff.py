from datetime import datetime, timedelta

def calculate_timestamp_difference(timestamp1, timestamp2, format='%Y-%m-%d %H:%M:%S'):
    """
    Calculate the time difference between two timestamps.

    Args:
        timestamp1 (str): First timestamp as a string.
        timestamp2 (str): Second timestamp as a string.
        format (str, optional): Format of the timestamps. Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        dict: A dictionary containing the time difference with keys:
            - 'total_seconds': Total difference in seconds
            - 'days': Whole number of days
            - 'hours': Remaining hours
            - 'minutes': Remaining minutes
            - 'seconds': Remaining seconds
            - 'is_negative': Boolean indicating if the difference is negative

    Raises:
        ValueError: If timestamps cannot be parsed or are in invalid format.
    """
    try:
        # Parse timestamps 
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)

        # Calculate time difference
        time_diff = dt2 - dt1

        # Prepare return dictionary
        total_seconds = int(time_diff.total_seconds())
        is_negative = total_seconds < 0
        
        # Use absolute value for calculations
        abs_seconds = abs(total_seconds)
        
        days, remainder = divmod(abs_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            'total_seconds': total_seconds,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'is_negative': is_negative
        }
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format. {str(e)}")