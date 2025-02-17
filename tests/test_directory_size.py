import os
import pytest
import tempfile
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.directory_size import calculate_directory_size

def test_calculate_directory_size_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        assert calculate_directory_size(tmpdir) == 0

def test_calculate_directory_size_single_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a file with known size
        test_file_path = os.path.join(tmpdir, 'test.txt')
        with open(test_file_path, 'w') as f:
            f.write('Hello World')
        
        assert calculate_directory_size(tmpdir) == len('Hello World')

def test_calculate_directory_size_multiple_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files
        files = [
            ('file1.txt', 'First content'),
            ('file2.txt', 'Second content'),
            ('file3.txt', 'Third content')
        ]
        
        total_size = 0
        for filename, content in files:
            file_path = os.path.join(tmpdir, filename)
            with open(file_path, 'w') as f:
                f.write(content)
            total_size += len(content)
        
        assert calculate_directory_size(tmpdir) == total_size

def test_calculate_directory_size_subdirectories():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create subdirectories with files
        os.makedirs(os.path.join(tmpdir, 'subdir1'))
        os.makedirs(os.path.join(tmpdir, 'subdir2'))
        
        files = [
            ('file1.txt', 'First content', None),
            ('file2.txt', 'Second content', 'subdir1'),
            ('file3.txt', 'Third content', 'subdir2')
        ]
        
        total_size = 0
        for filename, content, subdir in files:
            if subdir:
                file_path = os.path.join(tmpdir, subdir, filename)
            else:
                file_path = os.path.join(tmpdir, filename)
            
            with open(file_path, 'w') as f:
                f.write(content)
            total_size += len(content)
        
        assert calculate_directory_size(tmpdir) == total_size

def test_calculate_directory_size_non_existent_directory():
    with pytest.raises(ValueError, match="Directory does not exist"):
        calculate_directory_size('/path/to/non/existent/directory')

def test_calculate_directory_size_file_instead_of_directory():
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b'Test content')
        tmpfile.close()
        
        try:
            with pytest.raises(ValueError, match="Provided path is not a directory"):
                calculate_directory_size(tmpfile.name)
        finally:
            os.unlink(tmpfile.name)