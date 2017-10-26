"""
DNAList.py

Definition of the DNAList class.

Author: Jietong Chen
        Leilei Sun
"""

from Node import *


class DNAList:
    """
    A linked list of Node, can be initialized with a string.
    """
    __slots__ = (
        "head",  # the pointer to the first node of the list
        "back"  # the pointer to the last node of the list
    )

    def __init__(self, gene=''):
        """
        Initialize the list with the string such that every characters in the
        string represents one node of the list.

        :param gene:    the string representing the list
        """
        self.head = None
        self.back = None

        # initialize the list with every character of the string
        for i in gene:
            # the list is empty
            if (self.back == None):
                self.head = Node(i)
                self.back = self.head
            # the list is not empty
            else:
                self.back.next = Node(i)
                self.back = self.back.next

    def __str__(self):
        """
        DNAList object's printable string representation.

        :return:    string of every nodes in the list
        """
        # the string representing the list
        str = ""
        # helper pointer to traversal the list
        cursor = self.head

        while (cursor != None):
            str += cursor.value
            cursor = cursor.next

        return str

    def append(self, item):
        """
        Append one node with given character value at the end of the list.

        :param item:    the value of the new node
        """
        # the list is empty
        if (self.back == None):
            self.back = Node(item)
            self.head = self.back
        # the list is not empty
        else:
            self.back.next = Node(item)
            self.back = self.back.next

    def join(self, other):
        """
        Concatenate another DNAList to the end of the list.

        :param other:    the DNAList to joining
        """
        # the list is empty
        if (self.back == None):
            self.head = other.head
            self.back = other.back
        # the list is not empty
        elif (other.head != None):
            self.back.next = other.head
            self.back = other.back

    def splice(self, ind, other):
        """
        Insert another DNAList into the given position of the list.

        :param ind:    index of the insert position
        :param other:    the DNAList to inserting
        """
        pass

    def snip(self, i1, i2):
        """
        Remove a specified portion of the list.

        :param i1:    the index of starting position
        :param i2:    the index of ending position
        """
        pass

    def match(self, s, cursor):
        """
        Compare a given string with the list starting from given pointer.

        :param s:    the string to matching
        :param cursor:    the pointer to the specified position of the list.
        :return:    the pointer to the end of the string if the string match
                    the list, -1 if the string not match the list
        """
        # traversal every characters of the string
        for c in s:
            # compare the node value with the character
            if (cursor != None and cursor.value == c):
                cursor = cursor.next
            else:
                return -1

        return cursor

    def find(self, s):
        """
        Find a given string in the list.

        :param s:    the string to find
        :return:    the pointer to the starting node and the pointer to the
                    ending node if found, None if not found
        """
        # the pointer to the node in front of the cursor
        start = None
        # the pointer to the node in the list
        cursor = self.head

        # traversal the list
        while (cursor != None):
            # compare the string with the list starting from cursor
            end = self.match(s, cursor)

            # match result is not False
            if (end != -1):
                return start, end
            # match result is False
            else:
                start = cursor
                cursor = cursor.next

        return None

    def replace(self, repstr, other):
        """
        Replace a given string in the list with another DNAList.

        :param repstr:    the string to replace
        :param other:    the DNAList to replace
        """
        # determine whether there exist the string in the list
        cursor = self.find(repstr)

        # the string exist
        if (cursor != None):
            if (other.head == None):
                if (cursor[0] == None):
                    self.head = cursor[1]
                elif (cursor[1] == None):
                    self.back = cursor[0]
                else:
                    cursor[0].next = cursor[1]
            else:
                # replace the nodes between two pointer with the given list
                if (cursor[0] == None):
                    self.head = other.head
                else:
                    cursor[0].next = other.head

                if (cursor[1] == None):
                    self.back = other.back
                else:
                    other.back.next = cursor[1]

    def copy(self):
        """
        Copy the list.

        :return:    a new DNAList with same content of the list
        """
        pass
