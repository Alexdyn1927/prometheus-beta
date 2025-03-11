import os
import pytest
import zipfile
import tempfile
import shutil

from src.zip_extractor import extract_zip_files


@pytest.fixture
def sample_zip_file():
    """Create a sample zip file for testing."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a sample zip file
        zip_path = os.path.join(temp_dir, 'test_archive.zip')
        with zipfile.ZipFile(zip_path, 'w') as zf:
            # Add some sample files
            zf.writestr('file1.txt', 'Content of file 1')
            zf.writestr('subdir/file2.txt', 'Content of file 2')
        
        yield zip_path
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)


def test_extract_zip_files_default_path(sample_zip_file):
    """Test extracting zip files to default path."""
    # Extract files
    extracted = extract_zip_files(sample_zip_file)
    
    # Verify extraction
    assert len(extracted) == 2
    assert any('file1.txt' in path for path in extracted)
    assert any('subdir/file2.txt' in path for path in extracted)
    
    # Cleanup extracted files
    for path in extracted:
        if os.path.exists(path):
            os.remove(path)
        # Remove parent directory if empty
        parent_dir = os.path.dirname(path)
        if not os.listdir(parent_dir):
            os.rmdir(parent_dir)


def test_extract_zip_files_custom_path(sample_zip_file):
    """Test extracting zip files to a custom path."""
    # Create a temporary extraction directory
    extract_dir = tempfile.mkdtemp()
    
    try:
        # Extract files to custom path
        extracted = extract_zip_files(sample_zip_file, extract_dir)
        
        # Verify extraction
        assert len(extracted) == 2
        assert all(path.startswith(extract_dir) for path in extracted)
        assert any('file1.txt' in path for path in extracted)
        assert any('subdir/file2.txt' in path for path in extracted)
    finally:
        # Clean up the temporary directory
        shutil.rmtree(extract_dir)


def test_extract_nonexistent_zip():
    """Test extracting from a non-existent zip file."""
    with pytest.raises(FileNotFoundError):
        extract_zip_files('nonexistent_file.zip')


def test_extract_invalid_zip():
    """Test extracting from an invalid zip file."""
    # Create a temporary file that's not a zip
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Not a zip file')
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError):
            extract_zip_files(temp_file_path)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)