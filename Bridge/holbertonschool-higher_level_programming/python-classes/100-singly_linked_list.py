#!/usr/bin/python3
"""
Module: singly_linked_list.py

This module defines classes to manipulate singly linked lists:
- The `Node` class represents a node in the list.
- The `SinglyLinkedList` class provides operations to manage the list,
  including insertion in a sorted order.
"""


class Node:
    """
    A class to represent a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node or None): The reference to the next node.
                                    Defaults to None.

        Raises:
            TypeError: If `data` is not an integer or `next_node` is not a
                        Node or None.
        """
        self.data = data  # Use setter for validation
        self.next_node = next_node  # Use setter for validation

    @property
    def data(self):
        """
        Getter for the `data` attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the `data` attribute.

        Validates that the data is an integer.

        Args:
            value (int): The data to store in the node.

        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for the `next_node` attribute.

        Returns:
            Node or None: The reference to the next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the `next_node` attribute.

        Validates that the next node is either a Node object or None.

        Args:
            value (Node or None): The next node in the list.

        Raises:
            TypeError: If `value` is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
        head (Node or None): The first node in the list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None  # Start with an empty list

    def __str__(self):
        """
        Provides a string representation of the list.

        Returns:
            str: A string with one data element per line.
        """
        result = []
        node = self.head
        while node:  # Traverse the list
            result.append(str(node.data))
            node = node.next_node
        return "\n".join(result)  # Join all elements with a newline

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the list in sorted order.

        Args:
            value (int): The value to insert into the list.

        Raises:
            TypeError: If `value` is not an integer.
        """
        new_node = Node(value)  # Create a new node
        # If the list is empty or the new node should be at the head
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        # Traverse the list to find the correct insertion point
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node
