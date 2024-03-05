from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def binary_search(arr: List[int], target: int, first_occurrence: bool = True) -> int:
    """
    Perform binary search in a sorted array to find the first or last occurrence of a target element.
    
    Parameters:
        arr (List[int]): Sorted list of elements.
        target (int): The element to be searched in the array.
        first_occurrence (bool): If True, search for the first occurrence of the target element,
                                 otherwise search for the last occurrence.
    
    Returns:
        int: Index of the first or last occurrence of the target element if found, -1 otherwise.
    """
    if not arr:
        logger.info("Empty array provided.")
        return -1

    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]
        
        if mid_element == target:
            result = mid
            if first_occurrence:
                right = mid - 1
            else:
                left = mid + 1
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
