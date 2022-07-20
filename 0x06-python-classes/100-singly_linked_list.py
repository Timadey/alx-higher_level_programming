#!/usr/bin/python3
"""This module defines a `Node` and a `SinglyLinkedList` Class
Attributes:
    Node: a node class, a node holds a data and the next node
    SinglyLinkedList: a class that defines a singly linked list
"""


class Node:
    """Node defines a node of a singly linked list"""

    def __init___(self, data, next_node=None):
        """The Node is initialized with data and the next node

        Args:
            data(int): the data the node will hold
            next_node(Node): the next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in a node

        :value: int: the value to store in the node

        Raises:
            TypeError if the value is not of int type
        """

        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be aan integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in a list

        :value: node: the next node

        Raises:
            TypeError if value is not a node object
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        try:
            if (type(value) != type(self)):
                raise TypeError("next_node must be a node object")
        except TypeError:
            if value is not None:
                raise
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list

        Instantiates the head of the list
        """

        self.__head = None

    def __str__(self):
        """Print the entire list in stdout one node number by line
        """

        current_node = self.__head

        while (current_node is not None):
            print(f"{current_node.data:d}", end="")
            if current_node.next_node is not None:
                print()
            current_node = current_node.next_node
        return ""

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position int the
        list(increasing order)

        Args:
            value(int): the value of the new node to add
        """

        new_node = Node()
        new_node.data = value
        new_node.next_node = None

        if (self.__head is None):
            # check if list is empty and set new node to be head if true

            self.__head = new_node

        elif (new_node.data < self.__head.data):
            # else if new node data is less than that of head
            # put new node behind head and set head to new node

            new_node.next_node = self.__head
            self.__head = new_node

        else:
            # else loop till we find the number greater than new_node.data
            # and put new_node behind it

            current_node = self.__head

            while (current_node.next_node is not None
                    and current_node.next_node.data < new_node.data):
                current_node = current_node.next_node

            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
