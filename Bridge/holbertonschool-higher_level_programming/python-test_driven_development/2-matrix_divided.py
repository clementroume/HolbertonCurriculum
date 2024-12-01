#!/usr/bin/python3
"""
1. Divide a matrix

This module defines the `matrix_divided` function, which divides all elements
of a given matrix by a specified divisor. The function ensures the matrix is
well-formed (list of lists of integers or floats) and handles division safely.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
            - Must be a non-empty list of non-empty lists.
            - Each row must have the same size.
            - Elements must be integers or floats.
        div (int or float): The divisor.
            - Must be a non-zero integer or float.

    Returns:
        list of lists of float: A new matrix with each element divided
        by `div`, rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats, or if
                   rows are not of the same size, or if `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Examples:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]
        >>> matrix_divided([[1.5, 2.5]], 1.5)
        [[1.0, 1.67]]
    """
    errormsg = "matrix must be a matrix (list of lists) of integers/floats"

    # Validate `matrix` is a list of lists of integers/floats
    if not matrix or not isinstance(matrix, list):
        raise TypeError(errormsg)
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(errormsg)
        if len(rows) == 0:
            raise TypeError(errormsg)
        for values in rows:
            if not isinstance(values, (int, float)):
                raise TypeError(errormsg)

    # Validate all rows have the same size
    if len({len(rows) for rows in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate `div` is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round to 2 decimal places
    return [[round(value / div, 2) for value in lists] for lists in matrix]
