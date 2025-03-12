def select_pivot(arr):
    """
    Select the pivot using the median of medians algorithm.
    
    This function implements the linear-time selection algorithm 
    to find the k-th smallest element in an unsorted array.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        The pivot element used for partitioning
    """
    # If the array is small, return its median
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]
    
    # Divide the array into groups of 5
    sublists = [sorted(arr[i:i+5]) for i in range(0, len(arr), 5)]
    
    # Find the median of the medians of these sublists
    medians = [sublist[len(sublist) // 2] for sublist in sublists]
    
    # Recursively find the median of medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select_pivot(medians)
    
    return pivot

def partition(arr, pivot):
    """
    Partition the array around the pivot.
    
    Args:
        arr (list): Input list to partition
        pivot: Pivot element to partition around
    
    Returns:
        tuple: Lists of elements less than, equal to, and greater than pivot
    """
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return less, equal, greater

def quick_select(arr, k):
    """
    Find the k-th smallest element in an unsorted array.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (0-based index)
    
    Returns:
        The k-th smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds
    """
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    
    # Input validation
    if not arr:
        raise ValueError("Cannot find element in an empty array")
    
    if k < 0 or k >= len(arr):
        raise ValueError(f"k must be between 0 and {len(arr)-1}")
    
    # Select pivot using median of medians
    pivot = select_pivot(arr)
    
    # Partition the array
    less, equal, greater = partition(arr, pivot)
    
    # Determine which partition the k-th element is in
    if k < len(less):
        return quick_select(less, k)
    elif k < len(less) + len(equal):
        return pivot
    else:
        return quick_select(greater, k - len(less) - len(equal))