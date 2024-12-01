#!/usr/bin/python3
"""
Module for lazy matrix multiplication

This module defines the `lazy_matrix_mul` function, which multiplies two
matrices using the NumPy library for efficient computation.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.matrix: The result of the matrix multiplication.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list of lists or contains
                   non-numeric elements.
        ValueError: If rows in `m_a` or `m_b` are not of consistent sizes,
                    or if the matrices cannot be multiplied due to
                    incompatible dimensions.

    Examples:
        >>> lazy_matrix_mul([[1, 2]], [[3], [4]])
        matrix([[11]])
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        matrix([[19, 22],
                [43, 50]])
    """
    # Validation des éléments de la matrice `m_a`.
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        if len(row) != len(m_a[0]):
            raise ValueError("setting an array element with a sequence.")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("invalid data type for einsum")

    # Validation des éléments de la matrice `m_b`.
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        if len(row) != len(m_b[0]):
            raise ValueError("setting an array element with a sequence.")
        for num in row:
            if not isinstance(num, (int, float)):
                raise ValueError("invalid data type for einsum")

    return np.matrix(m_a) * np.matrix(m_b)
