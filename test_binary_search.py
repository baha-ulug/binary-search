import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_list(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_two_elements_list(self):
        self.assertEqual(binary_search([1, 2], 1), 0)
        self.assertEqual(binary_search([1, 2], 2), 1)

    def test_target_smaller_than_all_elements(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)

    def test_target_larger_than_all_elements(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_duplicate_elements_first_occurrence(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 3], 2), 1)

    def test_duplicate_elements_last_occurrence(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 3], 3, first_occurrence=False), 4)

    def test_negative_numbers_first_occurrence(self):
        self.assertEqual(binary_search([-5, -3, -1, 0, 1, 3, 5], 3), 5)

    def test_negative_numbers_last_occurrence(self):
        self.assertEqual(binary_search([-5, -3, -1, 0, 1, 3, 5], 5, first_occurrence=False), 6)
        self.assertEqual(binary_search([-5, -3, -1, 0, 1, 3, 5, 5], 5, first_occurrence=False), 7)

if __name__ == '__main__':
    unittest.main()
