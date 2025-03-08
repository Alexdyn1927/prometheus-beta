def subtract_arrays(A, B):
    """
    Subtract two arrays element-wise with modulo 10 operation.
    
    Args:
        A (list): First input array of 10 integers
        B (list): Second input array of 10 integers
    
    Returns:
        list: Result array where each element is (A[i] - B[i]) % 10, 
              with negative results set to 0
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    # Input validation
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    # Compute result array in O(n) time
    return [max(0, (a - b) % 10) for a, b in zip(A, B)]