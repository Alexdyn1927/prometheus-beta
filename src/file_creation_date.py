import os
import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file.
    
    Args:
        file_path (str): Relative path to the file
    
    Returns:
        datetime.datetime: Creation date of the file
    
    Raises:
        FileNotFoundError: If the file does not exist
        OSError: If the file creation time cannot be determined
    """
    # Convert to absolute path to ensure correct file access
    abs_file_path = os.path.abspath(file_path)
    
    if not os.path.exists(abs_file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Use platform-specific methods to get file creation time
        if os.name == 'nt':  # Windows
            creation_time = os.path.getctime(abs_file_path)
        else:  # Unix/Linux/macOS
            stat = os.stat(abs_file_path)
            try:
                creation_time = stat.st_birthtime  # macOS
            except AttributeError:
                creation_time = stat.st_ctime  # Linux/Unix fallback
        
        return datetime.datetime.fromtimestamp(creation_time)
    
    except Exception as e:
        raise OSError(f"Could not retrieve file creation time: {str(e)}")