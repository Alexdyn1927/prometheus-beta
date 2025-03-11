def heap_sort(arr):
    """
    Implement Heap Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr_to_sort = arr.copy()
    
    def heapify(arr, n, i):
        """
        Maintain heap property for a subtree rooted at index i.
        
        Args:
            arr (list): The list being sorted.
            n (int): Size of the heap.
            i (int): Root index of the subtree.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if left child exists and is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # Check if right child exists and is larger than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # If largest is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    # Build max heap
    n = len(arr_to_sort)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_to_sort, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr_to_sort[0], arr_to_sort[i] = arr_to_sort[i], arr_to_sort[0]
        
        # Heapify the reduced heap
        heapify(arr_to_sort, i, 0)
    
    return arr_to_sort