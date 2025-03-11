import os
import zipfile


def extract_zip_files(zip_path, extract_path=None):
    """
    Extract all files from a zip archive to a specified destination.

    Args:
        zip_path (str): Path to the input zip file.
        extract_path (str, optional): Destination directory for extracted files. 
                                      If None, extracts to the zip file's directory.

    Returns:
        list: List of paths to extracted files.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        ValueError: If the input path is not a valid zip file.
        PermissionError: If there are insufficient permissions to extract files.
    """
    # Validate input zip file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    # Validate it's a zip file
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a valid zip file: {zip_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(zip_path))
    
    # Ensure extraction path exists
    os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    try:
        # Open and extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files, preserving directory structure
            for file in zip_ref.namelist():
                # Construct full file path
                full_path = zip_ref.extract(file, path=extract_path)
                extracted_files.append(full_path)

        return extracted_files

    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract files to {extract_path}")
    except zipfile.BadZipFile:
        raise ValueError(f"Corrupted or invalid zip file: {zip_path}")