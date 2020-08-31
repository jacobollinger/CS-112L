#   File: panama.py
#   Draw the national flag of Panama. 

#   author: yanushka

import turtle
from math import sin, cos, pi, tan

#   Define constants. By convention constants use all upper case letters.
RED = ( 211, 7, 49 )
BLUE = ( 0, 81, 148 )
SIZE = 4
WIDTH = 80 * SIZE
HEIGHT = 40 * SIZE
RADIUS = 12 * SIZE

TITLE = "Panama's National Flag"

#   Fill a 5 point star with center at the point ( x, y ) of a particular 
#   radius with a particular color.
def fillStar( turtle, x, y, radius, color ) :
#   Define a radius, angle and change of angle variable dt.
    angle = pi / 2
    dt = 2 * pi / 5

    #   Use trigonometry to find five points of a star that points north.
    a = ( x + radius * cos( angle ), y + radius * sin( angle ) )
    angle = angle + dt
    b = ( x + radius * cos( angle ), y + radius * sin( angle ) )
    angle = angle + dt
    c = ( x + radius * cos( angle ), y + radius * sin( angle ) )
    angle = angle + dt
    d = ( x + radius * cos( angle ), y + radius * sin( angle ) )
    angle = angle + dt
    e = ( x + radius * cos( angle ), y + radius * sin( angle ) )

    #   Translate design into code to find the point ae where the line 
    #   through points a and d meets the line through points b and e.
    #   A point a = ( x, y ) has x coordinate in Python of a[ 0 ] and
    #   y coordinate of a[ 1 ].
    adSlope = ( a[ 1 ] - d[ 1 ] ) / ( a[ 0 ] - d[ 0 ] )
    ae = ( ( b[ 1 ] - a[ 1 ] ) / adSlope + a[ 0 ], b[ 1 ] )
    innerRadius = ( ( ae[ 0 ] - x ) ** 2 + ( ae[ 1 ] - y ) ** 2 ) ** 0.5

    #   Find the remaining 4 points as ab bc cd de of inner circle.
    innerAngle = pi / 2 + pi / 5
    ab = ( x + innerRadius * cos( innerAngle ), 
            y + innerRadius * sin( innerAngle ) )
    innerAngle = innerAngle + dt
    bc = ( x + innerRadius * cos( innerAngle ), 
            y + innerRadius * sin( innerAngle ) )
    innerAngle = innerAngle + dt
    cd = ( x + innerRadius * cos( innerAngle ), 
            y + innerRadius * sin( innerAngle ) )
    innerAngle = innerAngle + dt
    de = ( x + innerRadius * cos( innerAngle ), 
            y + innerRadius * sin( innerAngle ) )

    #   First draw a filled red star in CBU red.
    turtle.penup()
    turtle.goto( a )
    screen.colormode( 255 )
    turtle.fillcolor( color )
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto( ab )
    turtle.goto( b )
    turtle.goto( bc )
    turtle.goto( c )
    turtle.goto( cd )
    turtle.goto( d )
    turtle.goto( de )
    turtle.goto( e )
    turtle.goto( ae )
    turtle.goto( a )
    turtle.end_fill()
    turtle.penup()

#   Fill a rectangle with a drawing turtle with upper left at the point ( x, y )
#   of a particular width and height and color.
def fillRectangle( turtle, x, y, width, height, color ) :
    turtle.penup()
    turtle.goto( x, y )
    turtle.fillcolor( color )
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto( x, y - height )
    turtle.goto( x + width, y - height )
    turtle.goto( x + width, y )
    turtle.goto( x, y )
    turtle.penup()
    turtle.end_fill()

#   Draw a rectangle with a drawing turtle with upper left at the point ( x, y )
#   of a width w and height h.
def drawRectangle( t, x, y, w, h ) :
    t.penup()
    t.goto( x, y )
    t.pendown()
    t.goto( x, y - h )
    t.goto( x + w, y - h )
    t.goto( x + w, y )
    t.goto( x, y )
    t.pendown()

#   Define a screen variable and a turtle variable.
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed( 0 )
screen.colormode( 255 )
screen.title( TITLE )

fillRectangle( turtle, 0, HEIGHT, WIDTH, HEIGHT, RED )
fillRectangle( turtle, -WIDTH, 0, WIDTH, HEIGHT, BLUE )
fillStar( turtle, -WIDTH / 2, HEIGHT / 2, RADIUS, BLUE )
fillStar( turtle, WIDTH / 2, -HEIGHT / 2, RADIUS, RED )
drawRectangle( turtle, -WIDTH, HEIGHT, 2 * WIDTH, 2 * HEIGHT )
turtle.hideturtle()

screen.mainloop()
