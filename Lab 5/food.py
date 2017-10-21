"""
A module that represents the valid food types.

Author: Sean Strout @ RITCS
        Jietong Chen
        Leilei Sun
"""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato', 'mushroom'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato', 'mushroom'}

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom': 7
}


class Food:
    """
    Class: Food
    Description: This class define a food item on the skewer.
    """

    __slots__ = (
        'name',      # the name of the food
        'isVeggie',  # whether the food is vegetable
        'calories'   # the number of calories
    )

    def __init__(self, name):
        """
        Initialize food object with valid name and assign proper variable value
        to the object.
        :param name: the name of the food
        """
        self.name = name

        self.isVeggie = False

        for veggie in VEGGIES:
            if (veggie == self.name):
                self.isVeggie = True

        self.calories = CALORIES[self.name]

    def __new__(cls, name):
        """
        Create a food object if given name is valid.
        :param name: the name of the food
        :return: Food object if given name is valid, None if not
        """
        for food in FOODS:
            if (food == name):
                return object.__new__(cls)

        return None

    def __str__(self):
        """
        Get a string representing the food item.
        :return: the name of the food
        """
        return self.name

    def is_veggie(self):
        """
        Determine whether the food is veggie.
        :return: True if the food is veggie, False if not
        """
        return self.isVeggie
