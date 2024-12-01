#!/usr/bin/python3
"""
3. Print square

This module defines the `print_square` function, which prints a square
of a given size using the `#` character.
"""


def print_square(size):
    """
    Prints a square with the character `#`.

    Args:
        size (int): The size of the square's sides.
            - Must be a non-negative integer.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is negative.

    Examples:
        >>> print_square(3)
        ###
        ###
        ###
        >>> print_square(0)

        >>> print_square(2)
        ##
        ##
    """
    # Validate that `size` is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Validate that `size` is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
