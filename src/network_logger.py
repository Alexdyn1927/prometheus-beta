import time
import requests
import logging
from typing import Dict, Any, Optional

def log_network_request_response_time(
    url: str, 
    method: str = 'GET', 
    headers: Optional[Dict[str, str]] = None, 
    timeout: float = 10.0
) -> Dict[str, Any]:
    """
    Log the response time of a network request.

    Args:
        url (str): The URL to send the network request to.
        method (str, optional): HTTP method. Defaults to 'GET'.
        headers (dict, optional): Optional headers for the request. Defaults to None.
        timeout (float, optional): Request timeout in seconds. Defaults to 10.0.

    Returns:
        Dict[str, Any]: A dictionary containing request details and response metrics.

    Raises:
        ValueError: If an invalid URL is provided.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL provided")

    # Prepare request parameters
    request_params = {
        'url': url,
        'method': method.upper(),
        'timeout': timeout
    }
    if headers:
        request_params['headers'] = headers

    # Log start of request
    logging.info(f"Starting network request to {url}")

    # Measure request time
    start_time = time.time()

    try:
        # Send request
        response = requests.request(**request_params)
        
        # Calculate response time
        response_time = time.time() - start_time

        # Prepare response metrics
        request_metrics = {
            'url': url,
            'method': method.upper(),
            'status_code': response.status_code,
            'response_time_seconds': round(response_time, 4),
            'response_size_bytes': len(response.content)
        }

        # Log successful request details
        logging.info(f"Request to {url} completed in {response_time:.4f} seconds")

        return request_metrics

    except requests.RequestException as e:
        # Log and re-raise network-related exceptions
        logging.error(f"Network request error: {str(e)}")
        raise