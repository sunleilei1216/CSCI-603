"""
Lab 2
Author: Jietong Chen
        Sudhish Surendran

This is a program draw day and night scenario of the forest by python turtle graphics.
"""

# TOTAL_LUMBER is the total amount of tree trunks and house.
TOTAL_LUMBER = 0
# MARGIN is the outer border of the canvas.
MARGIN = 100

import turtle
import math
import random


def init(treesNumber, isDrawHouse):
    """
    This function initialize the program, setting properties.
    :param treesNumber:    the number of trees
    :param isDrawHouse:    whether draw a house
    """
    windowWidth = calculateWindowWidth(treesNumber, isDrawHouse)
    windowHeight = 300 + 2 * MARGIN
    initWindow(windowWidth, windowHeight)

    # setting up the turtle
    turtle.title('Forest - Lab2')
    turtle.up()
    turtle.speed(0)
    turtle.hideturtle()


def initWindow(windowWidth, windowHeight):
    """
    Setup the turtle graphics window in appropriate size.
    :param windowWidth:    window's width in pixel
    :param windowHeight:    window's height in pixel
    """
    turtle.setup(
        width=windowWidth,
        height=windowHeight,
        startx=None,
        starty=None)
    turtle.setworldcoordinates(
        - MARGIN,
        - MARGIN,
        windowWidth - MARGIN,
        windowHeight - MARGIN)


def calculateWindowWidth(treesNumber, isDrawHouse):
    """
    Calculate the window width in forest night.
    :param treesNumber:    the number of trees
    :param isDrawHouse:    whether draw a house
    :return:    corresponding window width in pixel
    """
    windowWidth = MARGIN * 2
    if (treesNumber >= 1):
        windowWidth += (treesNumber - 1) * 100
    if (isDrawHouse):
        windowWidth += 200
    return windowWidth


def calculateWallHeight():
    """
    Calculate the wall height of house built in day.
    :return:    house wall height in pixel
    """
    return TOTAL_LUMBER / (2.0 + math.sqrt(2))


def drawTrunk(trunkHeight):
    """
    This function draw a vertical straight line represent trunk.
    :param trunkHeight:    length of the trunk in pixel
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, trunkHeight), pen up
    """
    turtle.down()
    turtle.left(90)
    turtle.fd(trunkHeight)
    turtle.up()
    turtle.right(90)


def drawPineTreeTop(pineTreeTopSize=75):
    """
    This function draw a triangle represent the top of a pine tree.
    :param pineTreeTopSize:    size of the pine tree top
    :pre:    heading 0, position(0, trunkHeight), pen up
    :post:    heading 0, position(0, trunkHeight), pen up
    """
    turtle.down()
    turtle.fd(pineTreeTopSize / 2.0)
    turtle.left(120)
    turtle.fd(pineTreeTopSize)
    turtle.left(120)
    turtle.fd(pineTreeTopSize)
    turtle.left(120)
    turtle.fd(pineTreeTopSize / 2.0)
    turtle.up()


def drawMapleTreeTop(mapleTreeTopSize=80):
    """
    This function draw a circle represent the top of a maple tree.
    :param mapleTreeTopSize:    size of the maple tree top
    :pre:    heading 0, position(0, trunkHeight), pen up
    :post:    heading 0, position(0, trunkHeight), pen up
    """
    turtle.down()
    turtle.circle(mapleTreeTopSize / 2.0)
    turtle.up()


def drawCoconutTreeLeaf(CoconutLeafSize, isLeftLeaf):
    """
    This function draw a leaf of a coconut tree.
    :param CoconutLeafSize:    size of coconut tree leaf
    :param isLeftLeaf:    whether the leaf is on the left side of the tree
    """
    turtle.down()
    if (isLeftLeaf):
        turtle.right(60)
        turtle.circle(CoconutLeafSize * math.sqrt(3) / 3.0, 120)
        turtle.left(150)
        turtle.circle(-CoconutLeafSize, 60)
        turtle.right(150)
    else:
        turtle.left(60)
        turtle.circle(-CoconutLeafSize * math.sqrt(3) / 3.0, 120)
        turtle.right(150)
        turtle.circle(CoconutLeafSize, 60)
        turtle.left(150)
    turtle.up()


def drawCoconutTreeTop():
    """
    This function draw the top of a coconut tree.
    :pre:    heading 0, position(0, trunkHeight), pen up
    :post:    heading 0, position(0, trunkHeight), pen up
    """
    turtle.left(200)
    drawCoconutTreeLeaf(50, True)
    turtle.right(40)
    drawCoconutTreeLeaf(40, True)
    turtle.right(100)
    drawCoconutTreeLeaf(40, False)
    turtle.right(30)
    drawCoconutTreeLeaf(38, False)
    turtle.right(30)
    drawCoconutTreeLeaf(50, False)
    turtle.right(40)
    drawCoconutTreeLeaf(45, False)
    turtle.left(40)


def drawPineTree():
    """
    This function draw pine tree with random height and random top size.
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, 0), pen up
    :return:    trunk height of the pine tree, total height of the pine tree
    """
    trunkHeight = random.randint(50, 200)
    topSize = random.randint(65, 85)

    # draw the pine tree
    drawTrunk(trunkHeight)
    drawPineTreeTop(topSize)

    # reset the turtle to origin status
    turtle.right(90)
    turtle.fd(trunkHeight)
    turtle.left(90)

    return trunkHeight, trunkHeight + topSize * math.sqrt(3) / 2.0


def drawMapleTree():
    """
    This function draw maple tree with random height and random top size.
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, 0), pen up
    :return:    trunk height of the maple tree, total height of the maple tree
    """
    trunkHeight = random.randint(50, 150)
    topSize = random.randint(60, 100)

    # draw the maple tree
    drawTrunk(trunkHeight)
    drawMapleTreeTop(topSize)

    # reset the turtle to origin status
    turtle.right(90)
    turtle.fd(trunkHeight)
    turtle.left(90)

    return trunkHeight, trunkHeight + topSize


def drawCoconutTree():
    """
    This function draw coconut tree with random height and random top size.
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, 0), pen up
    :return:    trunk height of the coconut tree, total height of the coconut tree
    """
    trunkHeight = random.randint(50, 150)

    # draw the coconut tree
    drawTrunk(trunkHeight)
    drawCoconutTreeTop()

    # reset the turtle to origin status
    turtle.right(90)
    turtle.fd(trunkHeight)
    turtle.left(90)

    return trunkHeight, trunkHeight + 50


def drawTree():
    """
    This function draw a random tree.
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, 0), pen up
    :return:    trunk height of the drawn tree, total height of the drawn tree
    """
    # list of all tree drawing function
    treeList = [drawPineTree, drawMapleTree, drawCoconutTree]
    # call a random draw function
    return treeList[random.randint(0, 2)]()


def drawHouse(wallHeight=100):
    """
    This function draw a house with given size.
    :param wallHeight:    size of the house
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(wallHeight, 0), pen up
    """
    turtle.down()
    turtle.fd(wallHeight)
    turtle.left(90)
    turtle.fd(wallHeight)
    turtle.left(45)
    turtle.fd(wallHeight * math.sqrt(2) / 2.0)
    turtle.left(90)
    turtle.fd(wallHeight * math.sqrt(2) / 2.0)
    turtle.left(45)
    turtle.fd(wallHeight)
    turtle.up()

    turtle.left(90)
    turtle.fd(wallHeight)


def drawStar(starHeight, starSize=40):
    """
    This function draw an asterisk like star at given height.
    :param starHeight:    height of the star from horizon
    :param starSize:    size of the star
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(0, starHeight), pen up
    """
    turtle.left(90)
    turtle.fd(starHeight)

    # draw a star
    turtle.down()
    turtle.fd(starSize)
    turtle.up()

    turtle.right(90)
    turtle.fd(starSize * math.sqrt(2) / 4.0)
    turtle.right(90)
    turtle.fd(starSize * (2 - math.sqrt(2)) / 4.0)

    turtle.down()
    turtle.right(45)
    turtle.fd(starSize)
    turtle.up()

    turtle.right(45)
    turtle.fd(starSize * (2 - math.sqrt(2)) / 4.0)
    turtle.right(90)
    turtle.fd(starSize * math.sqrt(2) / 4.0)

    turtle.down()
    turtle.right(90)
    turtle.fd(starSize)
    turtle.up()

    turtle.right(90)
    turtle.fd(starSize * math.sqrt(2) / 4.0)
    turtle.right(90)
    turtle.fd(starSize * (2 - math.sqrt(2)) / 4.0)

    turtle.down()
    turtle.right(45)
    turtle.fd(starSize)
    turtle.up()

    # reset the turtle to origin status
    turtle.left(135)
    turtle.fd(starSize * (2 + math.sqrt(2)) / 4.0)
    turtle.left(90)
    turtle.fd(starSize * math.sqrt(2) / 4.0)


def drawSun(sunHeight, sunSize=50):
    """
    This function draw circle represent sun at given height.
    :param sunHeight:    height of the sun from horizon
    :param sunSize:    size of the sun
    :pre:    heading 0, position(0, 0), pen up
    :post:    heading 0, position(sunSize / 3.0, sunHeight), pen up
    """
    turtle.fd(sunSize / 3.0)
    turtle.left(90)
    turtle.fd(sunHeight)
    turtle.right(90)
    turtle.down()
    turtle.circle(sunSize)
    turtle.up()


def drawForestNight(treesNumber, isDrawHouse):
    """
    This function draw the forest scene at night.
    :param treesNumber:    the number of trees
    :param isDrawHouse:    whether draw a house
    """
    # total number of tree trunk and wooden house's walls and rooftop
    totalLumber = 0
    # the tallest tree/house in the forest
    tallestTree = 0

    if (isDrawHouse):
        # in the case that tree number is less than 2
        if (treesNumber < 2):
            # draw a 100px house first
            drawHouse(100)
            totalLumber += 100 * math.sqrt(2) + 200
            # assign the tallestTree as the top of the house
            tallestTree = max(50 * math.sqrt(2) + 100, tallestTree)

            if (treesNumber == 1):
                # draw ground
                turtle.down()
                turtle.fd(100)
                turtle.up()

                # draw a tree
                newTree = drawTree()
                totalLumber += newTree[0]
                tallestTree = max(newTree[1], tallestTree)

        # tree number is greater than or equal 2, the house must draw between two trees
        else:
            # select a random position for house
            # the variable means the house is behind the (housePosition - 1)th tree from left to right
            housePosition = random.randint(0, treesNumber - 2)

            for i in range(treesNumber - 1):
                # draw a tree
                newTree = drawTree()
                totalLumber += newTree[0]
                tallestTree = max(newTree[1], tallestTree)

                # draw the ground
                turtle.down()
                turtle.fd(100)
                turtle.up()

                if (i == housePosition):
                    # draw the house
                    drawHouse(100)
                    totalLumber += 100 * math.sqrt(2) + 200
                    tallestTree = max(50 * math.sqrt(2) + 100, tallestTree)

                    # draw the ground
                    turtle.down()
                    turtle.fd(100)
                    turtle.up()

            newTree = drawTree()
            totalLumber += newTree[0]
            tallestTree = max(newTree[1], tallestTree)


    else:
        for i in range(treesNumber - 1):
            # draw a tree
            newTree = drawTree()
            totalLumber += newTree[0]
            tallestTree = max(newTree[1], tallestTree)

            # draw the ground
            turtle.down()
            turtle.fd(100)
            turtle.up()

        newTree = drawTree()
        totalLumber += newTree[0]
        tallestTree = max(newTree[1], tallestTree)

    # draw a star 10px higher than the highest point
    drawStar(tallestTree + 10)

    # assign the global variable with total lumber number
    global TOTAL_LUMBER
    TOTAL_LUMBER = totalLumber


def drawForestDay():
    """
    This function draw the forest scene at day.
    """
    # unbind the key event, prevent misclick while drawing
    turtle.onkey(None, "Return")

    # reset the window size adapt to the new scene
    dayHouseWallHeight = calculateWallHeight()
    initWindow(dayHouseWallHeight + MARGIN * 2, dayHouseWallHeight * 3 / 2 + MARGIN * 2)

    print("We have", TOTAL_LUMBER, "units of lumber for building.")
    print("We will build a house with walls", dayHouseWallHeight, "tall.")

    # reset the turtle status and clear the canvas
    turtle.reset()
    turtle.speed(0)
    turtle.hideturtle()

    drawHouse(dayHouseWallHeight)
    drawSun(dayHouseWallHeight * 3 / 2 + 10)

    print("Day is done, house is built, press enter to quit")
    # bind the Enter key to turtle.bye()
    turtle.onkey(turtle.bye, "Return")


def main():
    """
    The main function of this program.
    """
    # the number of trees
    treesNumber = int(input("How many trees in your forest? "))
    isDrawHouseStr = input("Is there a house in the forest (y/n)? ")
    # whether draw a house
    isDrawHouse = False

    if isDrawHouseStr == 'y':
        isDrawHouse = True
    elif isDrawHouseStr == 'n':
        isDrawHouse = False

    # initialize the program
    init(treesNumber, isDrawHouse)

    # draw the forest at night
    drawForestNight(treesNumber, isDrawHouse)

    # bind the Enter key event
    turtle.listen()
    turtle.onkey(drawForestDay, "Return")

    print("Night is done, press enter for day")
    turtle.mainloop()


if __name__ == '__main__':
    main()
