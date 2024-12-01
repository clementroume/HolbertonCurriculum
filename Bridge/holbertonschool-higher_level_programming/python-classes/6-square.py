#!/usr/bin/python3
"""
Module: square.py

This module defines a Square class with the following features:
- Validation and controlled access to the size and position attributes.
- Calculation of the square's area.
- A method to visually represent the square with position adjustment.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square (private attribute), representing
                      the length of its sides.
        __position (tuple): The position of the square (private attribute),
                            represented by (horizontal_space, vertical_space).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
                        Must be a non-negative integer.
            position (tuple): A tuple of 2 positive integers indicating the
                              horizontal and vertical offsets.
                              Defaults to (0, 0).

        Raises:
            TypeError: If `size` is not an integer or `position` is not a
                        valid tuple.
            ValueError: If `size` is negative.
        """
        self.size = size  # Use setter for validation
        self.position = position  # Use setter for validation

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

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
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The current position of the square as (horizontal_space,
            vertical_space).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Validates and sets the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers representing
                           horizontal and vertical offsets.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):  # Check if value is a tuple
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:  # Ensure the tuple has exactly 2 elements
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            # Check for non-negative integers
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size^2.
        """
        return self.__size ** 2  # Area formula: side^2

    def my_print(self):
        """
        Prints a visual representation of the square using the `#` character,
        taking into account its position.

        If the size of the square is 0, prints an empty line.
        Otherwise:
        - Adds `vertical_space` newlines before the square.
        - Each row of the square is prefixed by `horizontal_space` spaces.
        """
        if self.size == 0:  # Handle case where size is 0
            print()
        else:
            horizontal_space, vertical_space = self.position
            # Print vertical offset (newlines)
            for _ in range(vertical_space):
                print("")
            # Print the square row by row
            for _ in range(self.size):
                print(" " * horizontal_space + "#" * self.size)
