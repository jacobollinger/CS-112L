#   File: gr.py
#   Graph a polynomial on an interval xMin to xMax.

import turtle
from random import randint

FONT = ( 'Arial', 12, 'normal' )
LO = -9
HI = 9
BTM = .25 # 2 # 10
JUMP = 10
HORIZONTAL_PIXELS = 400

SUPER_SCRIPTS = [ '⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹' ]

#   Return a random polynomial of a particular degree.
#   Represent a polynomial as a list of its coefficients.
def randomPoly( degree ) :
    poly = [ 0 ] * ( degree + 1 )

    for i in range( 0, degree + 1 ) :
        poly[ i ] = randint( LO, HI ) # / BTM

    while poly[ -1 ] == 0 :
        poly[ i ] = randint( LO, HI ) # / BTM

    return poly

#	Evaluate a polynomial at x with synthetic division.
def evalPoly( poly, x ) :
    return synDiv( poly, x )[ -1 ]
	
#   Return a list of coefficients for a polynomial divided by x - a 
#   for a particular value a.
def synDiv( poly, a ) :
    value = poly[ -1 ]
#   qr abbreviates quotient remainder.
    qr = [ value ]

    for j in range( len( poly ) - 2, -1, -1 ) :
        value = a * value + poly[ j ]
        qr.append( value )
    
    return qr 

#   Decide if each term in list qr is non negative.
def qrNonNeg( qr ) :
    return all( value >= 0 for value in qr )

#   Decide if the terms in list qr alternate in sign.	
def qrAlternates( qr ) :
    evens = qr[ 0 : : 2 ]
    odds = qr[ 1 : : 2 ]
    if qr[ 0 ] < 0 :
        pm = all( value <= 0 for value in evens ) and \
             all( value >= 0 for value in odds )
    else :
        pm = all( value >= 0 for value in evens ) and \
             all( value <= 0 for value in odds )

    return pm

#   Define a 'sine' function.
def s( x ) :
    return ( x - floor( x ) - ( x  - floor( x ) ) ** 2 ) * \
	       ( 1 - 2 * floor( x - 2 * floor( x / 2 ) ) )

#   Define a function f.
def f( x ) :
    n = 15
    return cos( n * acos( x ) )
    # return -.3 * x * x * x - 4 * x * x + 5 * x - 6
    # return 3 * x * x * x - 4 * x * x + 5 * x - 6

#   Fill a list of values for a polynomial from a to b with a particular 
#   step size.
#   Return a list of y values for the polynomial.
def fillPoly( poly, a, b, step ) :
    valueL = []
    x = a

    while x <= b :
        value = evalPoly( poly, x )
        valueL.append( value )
        x += step
		
    # print( 'fillPoly', valueL[ 0 ],  valueL[ -1 ] )
	
    return valueL

#   Draw a grid for the graph in the window xMin to xMax by yMin to yMax.
#   Places indicate the number of decimals in the x and y labels.
def drawGrid( turtle, xMin, xMax, yMin, yMax, places ) :
    turtle.penup()
    turtle.color( 'lightgray' )
    #   Draw vertical lines.
    xGap = ( xMax - xMin ) / 10
    for i in range( 1, 11 ) :
        turtle.goto( xMin + i * xGap, yMin )
        turtle.pendown()
        turtle.goto( xMin + i * xGap, yMax )
        turtle.penup()
    #   Draw horizontal lines.
    yGap = ( yMax - yMin ) / 10
    for i in range( 1, 11 ) :
        turtle.goto( xMin, yMin + i * yGap )
        turtle.pendown()
        turtle.goto( xMax, yMin + i * yGap )
        turtle.penup()
    turtle.color( 'black' )
    #   Write labels.
    for i in range( 1, 11 ) :
        turtle.goto( -0.1, yMin + i * yGap )
        if places > 0  :
            turtle.write( str( round( yMin + i * yGap, places ) ) )
        else :
            turtle.write( str( round( yMin + i * yGap ) ) )
        if yMin > 0 :
            vPos = yMin + .1
        elif yMax < 0 :
            vPos = yMax - .1
        else :
            vPos = -.1
        turtle.goto( xMin + i * xGap, vPos ) # -.1 )
        if yMax - yMin < 2 :
            places = 2
        turtle.write( str( round( xMin + i * xGap, places ) ), align = 'center')

#   Draw the x axis if yMin < 0 < yMax.
def drawXAxis( turtle, a, b, step ) :
    turtle.color( 'lightgray' )
    turtle.penup()
    turtle.goto( a, 0 )
    turtle.pendown()
    turtle.goto( b, 0 )
    turtle.penup()
    turtle.goto( b - step, -step )
    turtle.write( 'x', font = FONT ) #, True, 'left' )

#   Draw the y axis.
def drawYAxis( turtle, a, b, step ) :
    turtle.color( 'lightgray' )
    turtle.penup()
    turtle.goto( 0, a )
    turtle.pendown()
    turtle.goto( 0, b )
    turtle.penup()
    turtle.goto( -2 * step, .9* b )
    turtle.write( 'y', font = FONT ) #, True, 'right' )

#   Draw a polynomial in the window xMin to xMax by yMin to yMax.
def drawPoly( turtle, valueL, a, b, yMin, yMax, step ) :
    turtle.penup()
    x = a
    turtle.goto( x, valueL[ 0 ] )
    turtle.pendown()
    x += step
    i = 1

    turtle.pendown()
    while x < b :
        curValue = valueL[ i ]
        turtle.goto( x, curValue )
        x += step
        i += 1

    turtle.penup()
    if ( yMin <= 0 ) and ( 0 <= yMax ) :
        drawXAxis( turtle, a, b, step )
    if ( a <= 0 ) and ( 0 <= b ) :
        drawYAxis( turtle, yMin, yMax, step )
    
    drawGrid( turtle, a, b, yMin, yMax, 1 )
	
#   Find values negative a and positive b containing all real roots.
#   Use precalculus facts.
def findABroots( ply ) :
    leader = ply[ -1 ]
    if leader < 0 :
        poly = [ -value for value in ply ]
    else :
        poly = ply

    a = -1
    b = 1
    looking = True
    delta = .25

    while looking : 
        qr = synDiv( poly, b )
        looking = not qrNonNeg( qr ) 
        if looking :
            b += delta 

    looking = True
    while looking : 
        qr = synDiv( poly, a )
        looking = not qrAlternates( qr ) 
        if looking :
            a -= delta 

    return a, b 

#   Convert positive integer n to a superscripted string.
def toExpo( n ) :
    expo = ''
    sn = str( n )
    for ch in sn :
        expo += SUPER_SCRIPTS[ int( ch ) ]

    return expo

#   Convert list of coefficients of a polynomial to a string in standard
#   form from high to low degree.
def toString( poly ) :
    polyS = 'Graph of polynomial ' 

    for i in range( len( poly ) - 1, 1, -1 ) :
        if poly[ i ] > 0 :
            if ( poly[ i ] == 1 ) :
                polyS += ' + x' + toExpo( i )
            else :
                polyS += ' + ' + str( poly[ i ] ) + 'x' + toExpo( i )
        elif poly[ i ] < 0 :
            if ( poly[ i ] == -1 ) :
                polyS += ' - x' + toExpo( i )
            else :
                polyS += ' - ' + str( abs( poly[ i ] ) ) + 'x' + toExpo( i )
    if poly[ 1 ] > 0 :
        if poly[ 1 ] == 1 :
            polyS = ' + x'
        else :
            polyS += ' + ' + str( poly[ 1 ] ) + 'x' 
    elif poly[ 1 ] < 0 :
        if poly[ 1 ] == -1 :
            polyS = ' - x'
        else :
            polyS += ' - ' + str( abs( poly[ 1 ] ) ) + 'x' 
    if poly[ 0 ] > 0 :
        polyS += ' + ' + str( poly[ 0 ] )
    elif poly[ 0 ] < 0 :
        polyS += ' - ' + str( abs( poly[ 0 ] ) )

    return polyS

#   Test a polynomial.
def testPoly( degree ) :
    poly = randomPoly( degree )
    a, b = findABroots( poly )
    step = ( b - a ) / HORIZONTAL_PIXELS # 0.01
    valueL = fillPoly( poly, a, b, step ) 
    yMin = min( valueL )
    yMax = max( valueL )
    print( 'testPoly', poly, a, b, round( yMin, 5 ), round( yMax, 5 ) )
    screen.setworldcoordinates( a, yMin, b, yMax )
    screen.tracer( 2 )
    screen.title( toString( poly ) )
    drawPoly( turtle, valueL, a, b, yMin, yMax, step )
    turtle.hideturtle()

screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed( 0 )

degree = 8 
testPoly( degree )
screen.mainloop()