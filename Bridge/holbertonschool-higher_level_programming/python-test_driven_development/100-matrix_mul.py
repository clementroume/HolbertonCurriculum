#!/usr/bin/python3
"""
Module to multiply matrices

This module provides the `matrix_mul` function, which performs matrix
multiplication on two matrices, `m_a` and `m_b`. The matrices must be lists
of lists containing integers or floats, and the number of columns in `m_a`
must equal the number of rows in `m_b`.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices `m_a` and `m_b`.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The resulting matrix from
            multiplying `m_a` by `m_b`.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list of lists, or if they contain
                   non-numeric values, or if rows are of inconsistent sizes.
        ValueError: If `m_a` or `m_b` is empty, or if the matrices cannot
                    be multiplied due to dimension mismatches.

    Examples:
        >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
        >>> matrix_mul([[1]], [[2]])
        [[2]]
    """
    # Validate `m_a` is a list of lists containing only integers or floats
    if not m_a or not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    for rows in m_a:
        if not isinstance(rows, list):
            raise TypeError("m_a must be a list of lists")
        if len(rows) == 0:
            raise TypeError("m_a can't be empty")
        for values in rows:
            if not isinstance(values, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    # Validate `m_b` is a list of lists containing only integers or floats
    if not m_b or not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for rows in m_b:
        if not isinstance(rows, list):
            raise TypeError("m_b must be a list of lists")
        if len(rows) == 0:
            raise TypeError("m_b can't be empty")
        for values in rows:
            if not isinstance(values, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Validate that all rows in `m_a` are of the same size
    if len({len(rows) for rows in m_a}) != 1:
        raise TypeError("each row of m_a must be of the same size")

    # Validate that all rows in `m_b` are of the same size
    if len({len(rows) for rows in m_b}) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate matrix dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    m_c = [
        [
            sum(a * b for a, b in zip(A_row, B_col))
            for B_col in zip(*m_b)
        ]
        for A_row in m_a
    ]

    return m_c
