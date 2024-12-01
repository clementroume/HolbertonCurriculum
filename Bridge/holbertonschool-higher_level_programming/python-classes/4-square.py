#!/usr/bin/python3
"""
Module: square.py

This module defines a Square class that includes:
- Validation of the size attribute.
- Getter and setter methods for controlled access to size.
- A method to calculate the area of the square.
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
        """
        self._Square__size = size  # Set the size using direct assignment

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Validates and sets the size of the square.

        Args:
            value (int): The new size of the square. Must be non-negative.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):  # Ensure the size is an integer
            raise TypeError("size must be an integer")
        if value < 0:  # Ensure the size is non-negative
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size^2.
        """
        return self._Square__size ** 2  # Area formula: side^2
