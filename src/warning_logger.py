import logging

def log_warning(message):
    """
    Log a warning message to the console.
    
    Args:
        message (str): The warning message to log.
    
    Raises:
        TypeError: If the message is not a string.
    """
    # Validate input is a string
    if not isinstance(message, str):
        raise TypeError("Warning message must be a string")
    
    # Configure logging to output to console
    logging.basicConfig(level=logging.WARNING, 
                        format='%(levelname)s: %(message)s')
    
    # Log the warning message
    logging.warning(message)