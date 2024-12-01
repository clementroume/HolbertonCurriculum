#!/usr/bin/python3
"""
Module: square_comparison.py

This module defines a Square class with comparison capabilities
based on the area of the square.
"""


class Square:
    """
    A class to represent a square and enable comparisons based on its area.

    Attributes:
        __size (int): The size of the square (length of its sides).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.
        """
        self.size = size  # Use setter to validate the input

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2

    # Comparison methods based on the area of the square
    def __lt__(self, other):
        """
        Less-than comparison operator (<).

        Compares the area of this square with another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is less than the other.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less-than-or-equal-to comparison operator (<=).

        Compares the area of this square with another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is less than or equal
                to the other.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Equality comparison operator (==).

        Compares the area of this square with another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is equal to the other.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not-equal comparison operator (!=).

        Compares the area of this square with another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is not equal to the other.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater-than comparison operator (>).

        Compares the area of this square with another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is greater than the other.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater-than-or-equal-to comparison operator (>=).

        Compares the area of this square with another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is greater than or equal to
                the other.
        """
        return self.area() >= other.area()
