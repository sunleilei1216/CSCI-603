__author__ = 'Jietong Chen'

"""
Lab 1
Author: Jietong Chen (jc3165@rit.edu)

This is a program that draws my name with Python
turtle graphics.
"""

# TEXT is the letter show on the screen.
TEXT = 'Jietong Chen'
# FONT_SIZE determine the font size.
FONT_SIZE = 72
# WORD_SPACE is the space bewteen two letters.
WORD_SPACE = 12
# FONT_COLOR determine what color the letters
# appears. In a format of (R, G, B) color.
FONT_COLOR = (0.0, 0.0, 0.0)
# FONT_THICKNESS is the thickness of letters outline.
FONT_THICKNESS = 3
# BG_COLOR is the color of canvas.
BG_COLOR = (1.0, 1.0, 1.0)
# MARGIN is the outer border of the letters.
MARGIN = 24

# precalculated root value
ROOT_3 = 1.7320508076
ROOT_5 = 2.2360679775
ROOT_15 = 3.8729833462

import turtle

"""
This function initialize the program, setting properties
"""
def init():
    WINDOW_WIDTH = calWindowWidth()
    WINDOW_HEIGHT = 3 * FONT_SIZE + 2 * MARGIN

    turtle.title('Jietong Chen')
    turtle.setup(
        width = WINDOW_WIDTH, 
        height = WINDOW_HEIGHT, 
        startx = None, 
        starty = None)
    turtle.setworldcoordinates(
        - MARGIN, 
        - MARGIN - FONT_SIZE, 
        WINDOW_WIDTH - MARGIN, 
        WINDOW_HEIGHT - MARGIN - FONT_SIZE)

    turtle.up()
    turtle.color(FONT_COLOR)
    turtle.pensize(FONT_THICKNESS)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor(BG_COLOR)

"""
This function calculate correct width of the
screen.
:return: windows width
"""
def calWindowWidth():
    WINDOW_WIDTH = 2 * MARGIN
    #WINDOW_WIDTH += 11

    for letter in TEXT:
        if letter == 'C':
            WINDOW_WIDTH += 1.5 * FONT_SIZE
        elif letter == 'i':
            WINDOW_WIDTH += 0.5 * FONT_SIZE
        elif letter == 'J':
            WINDOW_WIDTH += 1.25 * FONT_SIZE
        else:
            WINDOW_WIDTH += FONT_SIZE
        WINDOW_WIDTH += WORD_SPACE
    else:
        WINDOW_WIDTH -= WORD_SPACE

    return WINDOW_WIDTH

"""
This function draw nothing but a empty space.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_space(originX, originY):
    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a upper case letter C.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (1.5 * FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_C(originX, originY):
    turtle.goto(
        originX + (6 + 3 * ROOT_3) * FONT_SIZE / 8, 
        originY + 9 * FONT_SIZE / 8)
    turtle.seth(120)

    turtle.down()
    turtle.circle(3 * FONT_SIZE / 4, 300)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.circle(- FONT_SIZE / 2, 300)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.up()

    turtle.goto(
        originX + 1.5 * FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter e.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_e(originX, originY):
    turtle.goto(
        originX + (4 - ROOT_3) * FONT_SIZE / 8, 
        originY + 5 * FONT_SIZE / 8)
    turtle.seth(0)

    turtle.down()
    turtle.fd(ROOT_3 * FONT_SIZE / 4)
    turtle.seth(120)
    turtle.circle(FONT_SIZE / 4, 120)
    turtle.up()

    turtle.goto(
        originX + (4 - ROOT_3) * FONT_SIZE / 8, 
        originY + 3 * FONT_SIZE / 8)
    turtle.seth(0)

    turtle.down()
    turtle.fd((ROOT_3 + ROOT_15) * FONT_SIZE / 8)
    turtle.seth(75.522)
    turtle.circle(FONT_SIZE / 2, 335)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.circle(-FONT_SIZE / 4, 110.522)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter g.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_g(originX, originY):
    turtle.goto(
        originX + FONT_SIZE / 2, 
        originY + FONT_SIZE / 4)
    turtle.seth(0)

    turtle.down()
    turtle.circle(FONT_SIZE / 4)
    turtle.up()

    turtle.goto(
        originX + 3 * FONT_SIZE / 4, 
        originY + FONT_SIZE / 8)
    turtle.seth(228.19)

    turtle.down()
    turtle.circle(- 5 * FONT_SIZE / 16, 48.19)
    turtle.circle(- FONT_SIZE / 2, 180)
    turtle.circle(- 5 * FONT_SIZE / 16, 48.19)
    turtle.seth(90)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(9 * FONT_SIZE / 8)
    turtle.circle(- FONT_SIZE / 2, 150)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.circle(FONT_SIZE / 4, 150)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter h.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_h(originX, originY):
    turtle.goto(
        originX + FONT_SIZE / 4, 
        originY + 7 * FONT_SIZE / 8)
    turtle.seth(90)

    turtle.down()
    turtle.fd(FONT_SIZE / 2)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(5 * FONT_SIZE / 4)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.circle(- FONT_SIZE / 4 ,180)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.circle(FONT_SIZE / 2, 90)
    turtle.circle(5 * FONT_SIZE / 16, 48.19)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter i.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (0.5 * FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_i(originX, originY):
    turtle.goto(
        originX + FONT_SIZE / 8, 
        originY + 7 * FONT_SIZE / 8)
    turtle.seth(90)

    turtle.down()
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 4)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE / 4, 
        originY + 1.4 * FONT_SIZE)
    turtle.seth(0)

    turtle.down()
    turtle.circle(- FONT_SIZE / 8)
    turtle.up()

    turtle.goto(
        originX + 0.5 * FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a upper case letter J.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (1.25 * FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_J(originX, originY):
    turtle.goto(
        originX + 5 * FONT_SIZE / 8, 
        originY + 5 * FONT_SIZE / 4)
    turtle.seth(180)

    turtle.down()
    turtle.fd(FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(FONT_SIZE / 4)
    turtle.seth(270)
    turtle.fd(7 * FONT_SIZE / 8)
    turtle.circle(- 3 * FONT_SIZE / 8, 180)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(7 * FONT_SIZE / 8)
    turtle.up()

    turtle.goto(
        originX + 1.25 * FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter n.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_n(originX, originY):
    turtle.goto(
        originX + FONT_SIZE / 4, 
        originY + 7 * FONT_SIZE / 8)
    turtle.seth(90)

    turtle.down()
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 4)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.circle(- FONT_SIZE / 4 ,180)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.circle(FONT_SIZE / 8, 180)
    turtle.fd(3 * FONT_SIZE / 8)
    turtle.circle(FONT_SIZE / 2, 90)
    turtle.circle(5 * FONT_SIZE / 16, 48.19)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter o.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_o(originX, originY):
    turtle.goto(
        originX + FONT_SIZE / 2, 
        originY + FONT_SIZE / 4)
    turtle.seth(0)

    turtle.down()
    turtle.circle(FONT_SIZE / 4)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE / 2, 
        originY)

    turtle.down()
    turtle.circle(FONT_SIZE / 2)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function draw a lower case letter t.
:pre: (relative) pos (0,0), heading (east), up
:post: (relative) pos (FONT_SIZE,0), heading (east), up
:return: None
"""
def draw_t(originX, originY):
    turtle.goto(
        originX + 3 * FONT_SIZE / 8, 
        originY + 3 * FONT_SIZE / 4)
    turtle.seth(180)

    turtle.down()
    turtle.fd(FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(FONT_SIZE / 4)
    turtle.seth(90)
    turtle.fd(FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(FONT_SIZE / 4)
    turtle.seth(0)
    turtle.fd(FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(FONT_SIZE / 4)
    turtle.seth(270)
    turtle.fd(FONT_SIZE / 2)
    turtle.seth(0)
    turtle.fd(FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 8, 180)
    turtle.fd(FONT_SIZE / 4)
    turtle.circle(- FONT_SIZE / 4, 90)
    turtle.fd(FONT_SIZE / 2)
    turtle.up()

    turtle.goto(
        originX + FONT_SIZE + WORD_SPACE, 
        originY)

"""
This function read every letter in TEXT, then 
call the corresponding draw letter function.
"""
def draw():

    for letter in TEXT:
        if letter == 'C':
            draw_C(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'e':
            draw_e(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'g':
            draw_g(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'h':
            draw_h(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'i':
            draw_i(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'J':
            draw_J(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'n':
            draw_n(turtle.pos()[0], turtle.pos()[1])
        elif letter == 'o':
            draw_o(turtle.pos()[0], turtle.pos()[1])
        elif letter == 't':
            draw_t(turtle.pos()[0], turtle.pos()[1])
        elif letter == ' ':
            draw_space(turtle.pos()[0], turtle.pos()[1])

"""
The main function of this program.
"""
def main():
    init()
    draw()
    turtle.mainloop()

if __name__ == '__main__':
    main()