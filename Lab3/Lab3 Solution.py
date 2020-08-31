# Lab3 Draw Random Walk wiht random steps and Random Walk that exceeds a circle
# By Jacob Bollinger and Jeffrie PETTIE

import turtle
from random import randint

# Define variables
COUNT = 0
RandomInt = randint(1,4)
DISTANCE = 0
STEPS = 1000

# Draw walk that exceeds a circle.
def drawWalk(DISTANCE, RandomInt, COUNT):
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.circle(300)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.dot()
    while DISTANCE < 300:
        if (RandomInt == 1):
            turtle.right(0)
            turtle.forward(8)
        elif (RandomInt == 2):
            turtle.right(90)
            turtle.forward(8)
        elif (RandomInt == 3):
            turtle.right(180)
            turtle.forward(8)
        elif (RandomInt == 4):
            turtle.right(270)
            turtle.forward(8)

        DISTANCE = turtle.distance((0,0))
        RandomInt = randint(1,4)
        COUNT = COUNT + 1
    turtle.dot()
    turtle.penup()
    turtle.goto(0, 300)
    TITLE = "it took", COUNT, "steps"
    turtle.write(TITLE, font=("Arial", 16, "normal"), align='center')

# Draw walk that moves a specific amount of steps
def drawSteps(RandomInt):
    turtle.tracer(0, 0)
    turtle.dot()
    for i in range(STEPS):
        if (RandomInt == 1):
            turtle.right(0)
            turtle.forward(8)
        elif (RandomInt == 2):
            turtle.right(90)
            turtle.forward(8)
        elif (RandomInt == 3):
            turtle.right(180)
            turtle.forward(8)
        elif (RandomInt == 4):
            turtle.right(270)
            turtle.forward(8)
        RandomInt = randint(1,4)
    turtle.dot()
    turtle.penup()
    turtle.goto(0, 300)
    TITLE = "it took", STEPS, "steps"
    turtle.write(TITLE, font=("Arial", 16, "normal"), align='center')

# Call drawWalk function that draws walk to exceed circle.
drawWalk(DISTANCE, RandomInt, COUNT)

# Call drawSteps function that walks a specific amount of steps
drawSteps(RandomInt)

# Keep the window open
turtle.mainloop()

# In this lab, we learned that the turtle had a distance function built into python that would tell the user how far the turtle is away from a given point. 
# We learned how to use the randomint function and use while loops. We also learned how to write text onto the screen.
# We learned that the turtle has a write function that can write something on the screen if you tell the turtle to go to a certain point. 
# We learned how to use the turtle.circle() function to draw a circle of radius size.