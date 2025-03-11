import time
import random
import logging
from typing import List, Callable, Tuple

def compare_sorting_algorithms(
    algorithm1: Callable[[List[int]], List[int]], 
    algorithm2: Callable[[List[int]], List[int]], 
    input_data: List[int]
) -> Tuple[float, float, bool]:
    """
    Compare performance of two sorting algorithms.

    Args:
        algorithm1 (Callable): First sorting algorithm to compare
        algorithm2 (Callable): Second sorting algorithm to compare
        input_data (List[int]): Input list to be sorted

    Returns:
        Tuple containing:
        - Time taken by algorithm1
        - Time taken by algorithm2
        - Boolean indicating if both algorithms produce the same sorted output
    """
    # Create copies to ensure fair comparison
    data1 = input_data.copy()
    data2 = input_data.copy()

    # Measure time for first algorithm
    start_time1 = time.perf_counter()
    sorted_result1 = algorithm1(data1)
    end_time1 = time.perf_counter()
    time1 = end_time1 - start_time1

    # Measure time for second algorithm
    start_time2 = time.perf_counter()
    sorted_result2 = algorithm2(data2)
    end_time2 = time.perf_counter()
    time2 = end_time2 - start_time2

    # Check if both algorithms produce the same output
    same_output = sorted_result1 == sorted_result2

    # Logging performance details
    logging.info(f"Algorithm 1 Time: {time1:.6f} seconds")
    logging.info(f"Algorithm 2 Time: {time2:.6f} seconds")
    logging.info(f"Results Match: {same_output}")

    return time1, time2, same_output

# Example sorting algorithms for testing
def bubble_sort(arr: List[int]) -> List[int]:
    """Simple bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: List[int]) -> List[int]:
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)