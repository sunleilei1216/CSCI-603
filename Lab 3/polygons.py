"""
Lab 3
Author: Jietong Chen

This program draw polygons recursively with the python turtle graphics.
"""

# colors of the polygons
COLORS = ('#ff0000', '#ff7f00', '#ffff00', '#00ff00', '#0033ff', '#ff00ff')

# window dimensions
WINDOW_LENGTH = 800
SIDE_LENGTH = 200

# pen sizes to use for filled and unfilled polygons
FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 4

# size of the display font
FONT_SIZE = 24

import turtle
import sys
import math


def init(sides, isFill):
    """
    Initialize the turtle window and draw text on it
    :param sides:    sides number of the main polygon
    :param isFill:    whether fill the polygons or not
    """
    # set up turtle
    turtle.title('Polygons - Lab 3')
    turtle.setup(
        width=WINDOW_LENGTH,
        height=WINDOW_LENGTH,
        startx=None,
        starty=None)

    turtle.hideturtle()
    turtle.tracer(0, 0)
    turtle.up()

    # change pen size according to whether fill polygons
    if (isFill):
        turtle.pensize(FILL_PEN_WIDTH)
    else:
        turtle.pensize(UNFILL_PEN_WIDTH)

    # draw the text messages
    drawText(sides, isFill)


def drawText(sides, isFill):
    """
    Draw the prompting text on the lower left corner of the window
    :param sides:    sides number of the main polygon
    :param isFill:    whether fill the polygons or not
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(-SIDE_LENGTH / 2.0,
                                  -SIDE_LENGTH * math.tan(math.radians(90 * (sides - 2) / sides)) / 2.0), pen up
    """
    turtle.goto(-WINDOW_LENGTH / 2.0 + 25,
                -WINDOW_LENGTH / 2.0 + 25 + FONT_SIZE * 1.4)
    # write the name of author
    turtle.write("Jietong Chen", False, "left", ("Arial", FONT_SIZE, "normal"))
    turtle.goto(-WINDOW_LENGTH / 2.0 + 25,
                -WINDOW_LENGTH / 2.0 + 25)
    # write the user input parameters
    turtle.write("Sides: %d, Fill: %s" % (sides, isFill), False, "left", ("Arial", FONT_SIZE, "normal"))
    turtle.goto(-SIDE_LENGTH / 2.0, -SIDE_LENGTH * math.tan(math.radians(90 * (sides - 2) / sides)) / 2.0)


def drawPolygons(side, length, isFill=False):
    """
    Draw the polygon with corresponding value given, then recursive call the smaller level function of drawing polygon.
    :param side:    sides number of the current drawing polygon
    :param length:    length of the current drawing polygon
    :param isFill:    whether fill the polygons or not
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, 0), pen up
    :return:    the total length of sides drawn
    """
    # total number of length drawn
    sum = 0

    # the smallest polygon is triangle
    if (side < 3):
        return sum

    # in the case of filling polygons
    if (isFill):
        turtle.down()
        # change the color of outline and filling
        turtle.color('#000000', COLORS[side - 3])
        turtle.begin_fill()

        # draw the main polygon
        for _ in range(side):
            turtle.forward(length)
            turtle.left(360.0 / side)

        turtle.end_fill()
        turtle.up()

    # recursive call the smaller level polygon drawing function
    for _ in range(side):
        turtle.forward(length)
        turtle.left(90)
        # draw the smaller polygon with one less side number and half of the length
        # adding the total length of smaller polygons to the sum
        sum += drawPolygons(side - 1, length / 2.0, isFill)
        turtle.right(90)
        turtle.left(360.0 / side)

    # in the case of not filling polygons
    if (not isFill):
        turtle.down()
        # change the pen color
        turtle.pencolor(COLORS[side - 3])

        # draw the main polygon
        for _ in range(side):
            turtle.forward(length)
            turtle.left(360.0 / side)

        turtle.up()

    return length * side + sum


def main():
    """
    The main function of this program.
    """

    # command line arguments number is incorrect
    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print("You should input the sides number of polygons in command line!\n"
              + "Run the program like following:\n\n"
              + "$ python3 polygons.py #_sides [ fill | unfill ]\n"
              + "           #_sides:  the number of sides of the main polygon [3, 8]\n"
              + " [ fill | unfill ]:  fill the polygons or not, default as not fill")
        return

    # first command line argument contain character not digits
    if (not sys.argv[1].isdigit()):
        print("Invalid sides number! The input should be integer numbers.")
        return

    sides = int(sys.argv[1])

    # the sides number is out of range
    if (sides < 3 or sides > 8):
        print("Invalid sides number! Sides number should in the range [3, 8].")
        return

    # whether fill the polygons, default is False
    isFill = False

    # there is a second command line argument
    if (len(sys.argv) == 3):
        if (sys.argv[2] == "fill"):
            isFill = True
        elif (sys.argv[2] != "unfill"):
            print("Invalid command! The command should be fill or unfill.")
            return

    # initialize the turtle
    init(int(sys.argv[1]), isFill)
    # draw the polygons and calculate total length drawn
    sum = drawPolygons(int(sys.argv[1]), SIDE_LENGTH, isFill)
    print("Sum: %d" % sum)

    turtle.update()
    turtle.mainloop()


if __name__ == '__main__':
    main()