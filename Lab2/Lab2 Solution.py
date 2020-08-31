# Lab 2/3 Draw the Betsy Ross flag
# author: Jacob Bollinger and Jeffrie Pettie

import turtle
from math import sin, cos, pi, tan

# Define constants.
WHITE = (255, 255, 255)
RED = (193, 3, 45)
BLUE = (0, 36, 104)
SIZE = 200
WIDTH_FLAG = 1.9 * SIZE
HEIGHT_FLAG = 1 * SIZE
WIDTH_UNION = 0.76 * SIZE
HEIGHT_UNION = 7 / 13 * SIZE
STRIPE_HEIGHT = 1 / 13 * SIZE
STAR_RADIUS = 0.0308 * SIZE
C = 7 / 13
E = 0.064
F = 0.054
CIRCLE_RADIUS = (C - E - F) / 2 * SIZE
TITLE = "Betsy Ross Flag"

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

def circleOfStars(turtle, bcx, bcy, radius, color):
    angle = pi / 2
    dt = 2 * pi / 13 
    
    #draw the 13 stars.
    for i in range(13):
        cx = bcx + CIRCLE_RADIUS * cos(angle)
        cy = bcy + CIRCLE_RADIUS * sin(angle)
        fillStar(turtle, cx, cy, STAR_RADIUS, color) 
        angle = angle + dt


# Define screen and turle variables
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle._tracer(0, 0)
screen.colormode(255)
screen.title(TITLE)
screen.setworldcoordinates(-50, -50, 300, 300)

# Draw the red stripes.
Y = STRIPE_HEIGHT
for i in range(7):
    fillRectangle(turtle, 0, Y, WIDTH_FLAG, STRIPE_HEIGHT, RED)
    Y = Y + 2 * STRIPE_HEIGHT

# Draw the Union in blue.
fillRectangle(turtle, 0, HEIGHT_FLAG, WIDTH_UNION, HEIGHT_UNION, BLUE)

# Draw the 13 white stars in a circle.
circleOfStars(turtle, WIDTH_UNION / 2, HEIGHT_FLAG - (HEIGHT_UNION / 2), CIRCLE_RADIUS, WHITE)

turtle.hideturtle()

screen.mainloop()

# In this lab we learned how to use setworldcoordinates. 
# We learned how to use trig to draw a circle of 13 5 point star.
# We learned how to use for loops effectively to draw the stars and stripes.
