import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from binary_search import binary_search


def test_binary_search():
    # Test cases
    test_cases = [
        ([], 5, -1, True),                              # Empty list, first occurrence
        ([1], 1, 0, True),                              # Single element list, first occurrence
        ([1, 2], 1, 0, True),                           # Two elements, first occurrence
        ([1, 2, 3, 4, 5], 0, -1, True),                 # Target smaller than all elements, first occurrence
        ([1, 2, 3, 4, 5], 6, -1, True),                 # Target larger than all elements, first occurrence
        ([1, 2, 2, 2, 3], 2, 1, True),                  # Duplicate elements (first occurrence)
        ([1, 2, 2, 2, 3], 3, 4, True),                  # Duplicate elements (first occurrence)
        ([-5, -3, -1, 0, 1, 3, 5], 3, 5, True),         # Negative numbers, first occurrence
        ([], 5, -1, False),                             # Empty list, last occurrence
        ([1], 1, 0, False),                             # Single element list, last occurrence
        ([1, 2], 1, 0, False),                          # Two elements, last occurrence
        ([1, 2, 3, 4, 5], 0, -1, False),                # Target smaller than all elements, last occurrence
        ([1, 2, 3, 4, 5], 6, -1, False),                # Target larger than all elements, last occurrence
        ([1, 2, 2, 2, 3], 2, 3, False),                 # Duplicate elements (last occurrence)
        ([1, 2, 2, 2, 3], 3, 4, False),                 # Duplicate elements (last occurrence)
        ([-5, -3, -1, 0, 1, 3, 5], 3, 5, False),        # Negative numbers, last occurrence
        ([-5, -3, -1, 0, 1, 3, 5, 5], 5, 7, False),     # Negative numbers, last occurrence
    ]
    
    for arr, target, expected, first_occurrence in test_cases:
        found_index = binary_search(arr, target, first_occurrence)
        if found_index != -1:
            logger.info(f"Index of target: {target}, in array: {arr}, index: {found_index}, expected result: {expected}")
        else:
            logger.info(f"Target: {target} not found in array: {arr}, index: {found_index}, expected result: {expected}")

        if found_index == expected:
            logger.info("Test Passed")
        else:
            logger.error(f"Test Failed, Expected index is {expected} but found index is {found_index}, there might be wrong with array or expected value")

        logger.info(f"Search for first occurrence: {first_occurrence}")
        logger.info("*"*100)

if __name__ == "__main__":
    test_binary_search()