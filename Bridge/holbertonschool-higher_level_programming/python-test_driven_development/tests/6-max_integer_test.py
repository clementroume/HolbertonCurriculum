#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_same(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_type(self):
        self.assertIs(list, list)

    def test_multipleMax(self):
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

    def test_single(self):
        self.assertEqual(max_integer([1]), 1)

    def test_float(self):
        self.assertEqual(max_integer([1.6, 1.1, 1.9, 1.3]), 1.9)

    # fmt: off
    def test_invalid(self):
        self.assertRaises(TypeError, max_integer([1, 2, 3, 4]),
                          msg="unorderable types: str() > int()")


# fmt: on
