import os

def calculate_directory_size(directory_path):
    """
    Calculate the total size of all files in a given directory.
    
    Args:
        directory_path (str): Path to the directory to calculate size for.
    
    Returns:
        int: Total size of files in bytes.
    
    Raises:
        ValueError: If the directory does not exist.
        PermissionError: If there's no permission to access the directory.
    """
    # Validate directory existence
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory does not exist: {directory_path}")
    
    # Validate it's a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"Provided path is not a directory: {directory_path}")
    
    total_size = 0
    
    # Walk through all files in the directory and subdirectories
    try:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                # Get full file path
                file_path = os.path.join(dirpath, filename)
                
                # Add file size (if possible to access)
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, PermissionError):
                    # Skip files that can't be accessed
                    continue
    
    except PermissionError:
        raise PermissionError(f"No permission to access directory: {directory_path}")
    
    return total_size