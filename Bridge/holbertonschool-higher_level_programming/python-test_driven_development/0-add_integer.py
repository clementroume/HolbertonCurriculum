#!/usr/bin/python3
"""
0. Integers addition

This module provides a function `add_integer` to add two integers or floats.
The function ensures that both inputs are either integers or floats, and
converts them to integers before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.

    Args:
        a (int or float): The first number to add. Must be an integer or a
                            float.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of `a` and `b`, cast to an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Examples:
        >>> add_integer(3, 5)
        8
        >>> add_integer(3.5, 2.5)
        5
        >>> add_integer(10)
        108
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
