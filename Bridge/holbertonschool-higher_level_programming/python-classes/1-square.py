#!/usr/bin/python3
"""
Module: square.py

This module defines a Square class with basic functionality.
At this stage, the class includes an initializer to set the size
of the square during instantiation.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square, representing the length
                        of its sides. Must be a positive integer.

        Attributes:
            __size (int): A private attribute to store the size of the square.
        """
        self._Square__size = size  # Private attribute following name mangling
