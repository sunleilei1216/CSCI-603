"""
A module that represents "spots" on the skewer.

Author: Sean Strout @ RITCS
        Jietong Chen
        Leilei Sun
"""


class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """

    __slots__ = (
        'item',  # the food item
        'next'   # the next KebabSpot on the skewer
    )

    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """
        self.item = item
        self.next = next

    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        if (self.item == None and self.next == None):
            return 0
        elif (self.item != None and self.next == None):
            return 1
        elif (self.item == None and self.next != None):
            return self.next.size()
        else:
            return self.next.size() + 1

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are all vegetables from this spot down,
        False otherwise.
        """
        if (self.item != None and self.item.isVeggie == False):
            return False
        elif (self.next != None):
            return self.next.is_vegan()
        else:
            return True

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """
        if (self.item != None and self.item.name == name):
            return True
        elif (self.next != None):
            return self.next.has(name)
        else:
            return False

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """
        if (self.next != None):
            return self.item.__str__() + ", " + self.next.string_em()
        else:
            return self.item.__str__()

    def get_item(self):
        """
        Return the food item of the kebab spot.
        :return: food item
        """
        return self.item

    def calories(self):
        """
        Return the total calories from this KebabSpot instance to the end of
        the skewer.
        :return: total calories (int)
        """
        if (self.item == None and self.next == None):
            return 0
        elif (self.item != None and self.next == None):
            return self.item.calories
        elif (self.item == None and self.next != None):
            return self.next.calories()
        else:
            return self.next.calories() + self.item.calories
