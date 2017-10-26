"""
Node.py

The basic node object of the linked list.

Author: Jietong Chen
        Leilei Sun
"""


class Node:
    """
    A node contains one character variable as value and a pointer to the next
    node on the linked list.
    """
    __slots__ = (
        "value",  # the value of object
        "next"  # the pointer to the next node
    )

    def __init__(self, value, nextNode=None):
        """
        Initialize the object with value and the pointer to next node.

        :param value:    the value of object
        :param nextNode:    the pointer to the next node on the linked list
        """
        self.value = value
        self.next = nextNode

    def __str__(self):
        """
        Node object's printable string representation.

        :return:    string of the value of the object
        """
        return str(self.value)
