import pytest
import requests
import logging
from src.network_logger import log_network_request_response_time

def test_successful_get_request(requests_mock):
    """Test a successful GET request with response time logging."""
    mock_url = 'https://example.com'
    requests_mock.get(mock_url, text='Hello World')
    
    result = log_network_request_response_time(mock_url)
    
    assert result['url'] == mock_url
    assert result['method'] == 'GET'
    assert result['status_code'] == 200
    assert 'response_time_seconds' in result
    assert result['response_time_seconds'] > 0

def test_invalid_url():
    """Test handling of invalid URL."""
    with pytest.raises(ValueError):
        log_network_request_response_time('')
    
    with pytest.raises(ValueError):
        log_network_request_response_time('invalid_url')

def test_different_http_methods(requests_mock):
    """Test different HTTP methods."""
    mock_url = 'https://example.com'
    requests_mock.post(mock_url, text='Created')
    
    result = log_network_request_response_time(mock_url, method='POST')
    
    assert result['method'] == 'POST'

def test_request_with_headers(requests_mock):
    """Test request with custom headers."""
    mock_url = 'https://example.com'
    mock_headers = {'Authorization': 'Bearer test_token'}
    requests_mock.get(mock_url, text='Authorized', request_headers=mock_headers)
    
    result = log_network_request_response_time(mock_url, headers=mock_headers)
    
    assert result['status_code'] == 200

def test_network_error(requests_mock):
    """Test network request exception handling."""
    mock_url = 'https://example.com'
    requests_mock.get(mock_url, exc=requests.ConnectionError)
    
    with pytest.raises(requests.RequestException):
        log_network_request_response_time(mock_url)

def test_response_size(requests_mock):
    """Test response size calculation."""
    mock_url = 'https://example.com'
    test_content = 'Hello, World!' * 100
    requests_mock.get(mock_url, text=test_content)
    
    result = log_network_request_response_time(mock_url)
    
    assert result['response_size_bytes'] == len(test_content)

def test_timeout_parameter(requests_mock):
    """Test custom timeout handling."""
    mock_url = 'https://example.com'
    requests_mock.get(mock_url, text='Timeout Test')
    
    result = log_network_request_response_time(mock_url, timeout=5.0)
    
    assert 'response_time_seconds' in result