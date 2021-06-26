import math
from random import randint, choice
from turtle import Turtle, Screen, colormode
from math import floor
import colorgram

tim = Turtle()
screen = Screen()

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

color_list = [(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97),
              (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199),
              (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142),
              (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (
              118, 117, 163)]

tim.hideturtle()

def hirst(x):
    colormode(255)

    def turn_left():
        tim.dot(10, choice(color_list))
        tim.left(90)
        tim.pu()
        tim.forward(20)
        tim.left(90)
        tim.pd()

    def turn_right():
        tim.dot(10, choice(color_list))
        tim.right(90)
        tim.pu()
        tim.forward(20)
        tim.right(90)
        tim.pd()

    def moveanddot():
        for i in range(x-1):
            tim.dot(10, choice(color_list))
            tim.pu()
            tim.forward(20)
            tim.pd()

    for j in range(x-1):
        moveanddot()
        if j % 2 == 0:
            turn_left()
        else:
            turn_right()


hirst(9)


# draw a square
def square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)


# draw a dashed line
def dashed():
    for i in range(15):
        tim.forward(5)
        tim.pu()
        tim.forward(5)
        tim.pd()


def shapes():
    for n in range(3, 11):
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
        for i in range(n):
            tim.forward(100)
            tim.left(float(360/n))


def random_walk():
    colormode(255)
    tim.pensize(5)
    tim.speed(10)
    for n in range(2500):
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.forward(20)
        tim.left(90*randint(0,3))


def spirograph():
    colormode(255)
    tim.speed(0)
    for n in range(360):
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.circle(100, None, None)
        tim.left(n)

screen.exitonclick()