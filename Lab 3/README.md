# Lab 2
## Problem
For this assignment, you will draw some pictures — first of a night-time scence in a forest containing some trees, an optional house, and a star. The second scene will be a day-time scene of a house “built” from the trees, and the sun.

![Lab2](https://i.imgur.com/biHKPPe.png)

### Forest at night
The forest at night will have the following:
- A number of trees selected by the user
- A house if requested by the user
- A single star, which is slightly higher than the tallest tree.

The type of each tree will be chosen at random each time the program is run from the following:
- Pine trees have a trunk up to 200 pixels tall and a triangle at the top
- Maple trees have a trunk up to 150 pixels tall and a circle at the top
- A third type of tree of your choice — it should have a different look to the other two but share some of the same code.

All trees will have a trunk of random height between 50 pixels and the given maximum height. Your solution should contain a single function to draw all types of trees, with shared code as much as feasible between the different types.

The house will be a pentagonal shape with a 45 degree roof angle, and 100 pixel tall walls, as shown in the picture above. It will appear between two trees, but which two trees it appears between should be selected randomly. There should be 100 pixels between tree truncks as well as between the house and its neighboring trees.

Finally, the star should look as pictured, with the bottom of the star 10 pixels higher than the top of the tallest tree.

### Forest during the day
In the morning, all of the trees get harvested to make a larger house. You will need to compute how much wood is available from the trunks of all the trees and the walls and roof of the house (that is, the ground/floor is not considered). Then, draw a house that uses exactly all that wood. That is, draw a house such that the total length of its walls and roof is the same as the total length of the house lines and tree trunks drawn previously.

You must use the same function to draw this house as you did for the optional house drawn at night.

There is also a sun, beside and above the house, as shown above. The sun may partially overlap with the border, but it must be above the house. I.e., the bottom pixel of the sun must be higher than the top pixel of the house.

### Helpful Tools
You may want to remember the Pythagorean Theorem for right triangles, which says that a triangle with a hypotenuse of length _h_ and side lengths _a_ and _b_ must satisfy the property that _a_^2 + _b_^2 = _h_^2.

Powers in python are computed with the ** operator. E.g., 2 ∗∗ 2 returns the value 4. To compute square roots in python, you must first import the math package. E.g.,
```python
import math
math.sqrt(2)
```
Because the roof is drawn at 45 degree angles from the walls, you should not need any trigonometric functions to solve this problem. However, if you wish to try them out, they are also in the math package.

You may prompt the user for input using the `input(message)` function, where message should be a quoted string prompting the user for a response.

One way of generating random numbers in python is to use the randint function from the random module. The following code prints a random integer from the closed range [0, 100].
```python
import random
random.randint(0,100)
```
Finally, you may wish to adjust the size of the canvas with the turtle function `setworldcoordinates`. For more information, type the following in the python interpreter:
```python
import turtle
help(turtle.setworldcoordinates)
```

## Implementation
Your implementation should prompt the user for the number of trees in the forest, and whether to include a house at night.

Your output should also include the size of the house that was constructed during the day, similar to the following:
```
How many trees in your forest? 4
Is there a house in the forest (y/n)? y
Night is done, press enter for day
We have 839.4213562373095 units of lumber for building.
We will build a house with walls 245.86082296909933 tall.
Day is done, house is built, press enter to quit
```
You may not use the `goto` and `heading` functions of the turtle. You may use the `reset` function when changing from night to day.
