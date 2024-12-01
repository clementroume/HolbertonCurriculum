#!/usr/bin/python3
"""
Module: square.py

This module defines a Square class with validation for its size.
It includes functionality to ensure that the size is a non-negative integer.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square (private attribute), representing
                      the length of its sides.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
                        Must be a non-negative integer.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.

        Attributes:
            __size (int): A private attribute to store the validated size.
        """
        # Validate the size argument
        if not isinstance(size, int):  # Ensure the type is an integer
            raise TypeError("size must be an integer")
        if size < 0:  # Ensure the value is non-negative
            raise ValueError("size must be >= 0")

        self._Square__size = size  # Set the private size attribute
