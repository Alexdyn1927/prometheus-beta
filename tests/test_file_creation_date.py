import os
import pytest
import datetime
import time
from src.file_creation_date import get_file_creation_date

def test_get_readme_creation_date():
    # Test creation date of existing README.md
    readme_path = 'README.md'
    
    # Get the creation date
    creation_date = get_file_creation_date(readme_path)
    
    # Check if it's a datetime object and is recent
    assert isinstance(creation_date, datetime.datetime)
    assert creation_date <= datetime.datetime.now()

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('nonexistent_file.txt')

def test_requirements_file_creation_date():
    # Test creation date of requirements.txt
    requirements_path = 'requirements.txt'
    
    # Get the creation date
    creation_date = get_file_creation_date(requirements_path)
    
    # Check if it's a datetime object
    assert isinstance(creation_date, datetime.datetime)
    assert creation_date <= datetime.datetime.now()