#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        self.assertEqual(max_integer[1, 2, 3, 4], 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -1, -7]), -1)
    
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_all_equal(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)


if __name__ == '__main__':
    unittest.main()