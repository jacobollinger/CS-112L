# Lab 1 Draw the flag of Burkina Faso
# author: Jacob Bollinger and Jeffrie Pettie

import turtle
from math import sin, cos, pi, tan

# Define constants.
PINK = (239, 43, 45)
GREEN = (0, 158, 73)
YELLOW = (252, 209, 22)
SIZE = 15
WIDTH = 30 * SIZE
HEIGHT = 20 * SIZE
RADIUS = 3.5 * SIZE

TITLE = "Burkina Faso's National Flag"

# Draw and fill a rectangle.
def fillRectangle(turtle, x, y, width, height, color) :
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(x, y - height)
    turtle.goto(x + width, y - height)
    turtle.goto(x + width, y)
    turtle.goto(x, y)
    turtle.penup()
    turtle.end_fill()

# Draw and fill a 5 point star.
def fillStar(turtle, x, y, radius, color) :
    angle = pi / 2
    dt = 2 * pi / 5

    # Find the 5 points of the star.
    a = (x + radius * cos(angle), y + radius * sin(angle))
    angle = angle + dt
    b = (x + radius * cos(angle), y + radius * sin(angle))
    angle = angle + dt
    c = (x + radius * cos(angle), y + radius * sin(angle))
    angle = angle + dt
    d = (x + radius * cos(angle), y + radius * sin(angle))
    angle = angle + dt
    e = (x + radius * cos(angle), y + radius * sin(angle))

    # Find the inner radius of the star.
    adSlope = ( a[1] - d[1]) / (a[0] - d[0])
    ae = ((b[1] - a[1]) / adSlope + a[0], b[1])
    innerRadius = ((ae[0] - x) ** 2 + (ae[1] - y) ** 2) ** 0.5

    # Find the 4 other points of the inner radius of the star.
    innerAngle = pi / 2 + pi / 5
    ab = (x + innerRadius * cos(innerAngle), y + innerRadius * sin(innerAngle))
    innerAngle = innerAngle + dt
    bc = (x + innerRadius * cos(innerAngle), y + innerRadius * sin(innerAngle))
    innerAngle = innerAngle + dt
    cd = (x + innerRadius * cos(innerAngle), y + innerRadius * sin(innerAngle))
    innerAngle = innerAngle + dt
    de = (x + innerRadius * cos(innerAngle), y + innerRadius * sin(innerAngle))

    # Draw the yellow star.
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(a)
    screen.colormode(255)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(ab)
    turtle.goto(b)
    turtle.goto(bc)
    turtle.goto(c)
    turtle.goto(cd)
    turtle.goto(d)
    turtle.goto(de)
    turtle.goto(e)
    turtle.goto(ae)
    turtle.goto(a)
    turtle.end_fill()
    turtle.penup()

# Define screen and turle variables
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(0)
screen.colormode(255)
screen.title(TITLE)

fillRectangle(turtle, -WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT / 2, PINK)
fillRectangle(turtle, -WIDTH / 2, 0, WIDTH, HEIGHT / 2, GREEN)
fillStar(turtle, 0, 0, RADIUS, YELLOW)
turtle.hideturtle()

screen.mainloop()

# In this lab we learned how to use turtle to create rectangles and stars. 
# We learned how to use trig to draw a 5 point star. 
# We learned to change the outline color to the color of the shape.
