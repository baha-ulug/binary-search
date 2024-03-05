# Binary Search in Python

This repository contains Python code for implementing binary search and unit tests for the implementation.

## 1. Binary Search Algorithm

The `binary_search.py` file defines the `binary_search` function that performs a binary search on a sorted list to find the index of a target element. The function accepts the following arguments:

- `arr`: A sorted list of integers.
- `target`: The element to search for.
- `first_occurrence` (optional, defaults to True): A boolean flag indicating whether to search for the first or last occurrence of the target element.

The function returns the index of the target element if found, or -1 otherwise.

## 2. Unit Tests

The `test_binary_search.py` file contains unit tests for the `binary_search` function using the `unittest` framework. The tests cover various scenarios, including:

- Empty list
- Single element list
- Two elements list
- Target smaller than all elements
- Target larger than all elements
- Duplicate elements (finding both first and last occurrences)
- Negative numbers

## 3. Simple Test

The `README.md` file includes a simple test script that demonstrates how to use the `binary_search` function and interpret the results. The script defines several test cases and calls the `binary_search` function for each case. It logs the expected and actual results and checks for any discrepancies.

## 4. Running the Tests

To run the unit tests, navigate to the directory containing the Python files and execute the following command:

