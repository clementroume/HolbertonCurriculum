#!/usr/bin/python3
"""
2. Say my name

This module defines the `say_my_name` function, which prints a formatted
string that introduces a person by their first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name of the person. Must be a string.
        last_name (str, optional): The last name of the person. Defaults to an
                                   empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Alice")
        My name is Alice
    """
    # Validate that `first_name` is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Validate that `last_name` is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))
