#Author: Skylar Newman and Jacob Bollinger
#Lab 8: The goal of this lab is to graph lab 7 several ways. 
#The first five function are from lab 7

import turtle 

def createList(l1, r1):
	return [item for item in range(l1, r1+1)]
#This function reads a text file to get the appropriate digits and pairs to test Benford's law. 
def fileCount(FileName):
	count = 0
	fIn = open(FileName)
	firstDigitList = [0] * 10
	firstTwoDigitsList = [0] * 100
	lastDigitList = [0] * 10
	lastTwoDigitsList = [0] * 100
	i = 0
	for line in fIn:
		line = line.strip()
		i = i + 1
		if i > 2:
			firstDigit = int(line[0])
			firstDigitList[firstDigit] += 1
			firstTwoDigits = int(line[0:2])
			firstTwoDigitsList[firstTwoDigits] += 1
			lastDigit = int(line[-1])
			lastDigitList[lastDigit] += 1
			lastTwoDigits = int(line[-2:])
			lastTwoDigitsList[lastTwoDigits] += 1
	return firstDigitList, firstTwoDigitList, lastDigitList, lastTwoDigitsList
#This function takes the information from the previous function and finds the percentages for each digit or pair.
def percents(digitList):
	fdTotal = sum(firstDigitList)
	fpTotal = sum(firstTwoDigitsList)
	ldTotal = sum(lastDigitList)
	lpTotal = sum(lastTwoDigitsList)
	fdpercentList = []
	ldpercentList = []
	ftpercentList = []
	ltpercentList = []
	for i in firstDigitList:
		fdPercent = (i) / (fdTotal)
		fdPercent = round(fdPercent * 100, 2)
		fdpercentList.append(fdPercent)
	for i in lastDigitList:
		ldPercent = (i) / (ldTotal)
		ldPercent = round(ldPercent * 100, 2)
		ldpercentList.append(ldPercent)
	for i in firstTwoDigitList:
		ftPercent = (i) / (fpTotal)
		ftPercent = round(ftPercent * 100, 2)
		ftpercentList.append(ftPercent)
	for i in lastTwoDigitsList:
		ltPercent = (i) / (lpTotal)
		ltPercent = round(ltPercent * 100, 2)
		ltpercentList.append(ltPercent)
	return fdpercentList, ftpercentList, ldpercentList, ltpercentList
	
#This is the function to calculate the first and last digits and pairs for the powers of two.
def powerCount():
	firstDigitList = [0] * 10
	firstTwoDigitList = [0] * 100
	lastDigitList = [0] * 10
	lastTwoDigitList = [0] * 100
	index = 0
	for i in range (10,10000):
			power = index ** 2
			digit = int(str(power)[0])
			firstDigitList[digit] += 1
			digit = int(str(power)[0:2])
			firstTwoDigitList[digit] += 1
			digit = int(str(power)[-1:])
			lastDigitList[digit] += 1
			digit = int(str(power)[-2:])
			lastTwoDigitList[digit] += 1
			index = index + 1
	return firstDigitList, firstTwoDigitList, lastDigitList, lastTwoDigitList
#This gives us the percents for the powers of two.
def percentPower(digitList):
	fdTotal = sum(firstDigitList)
	ftTotal = sum(firstTwoDigitList)
	ldTotal = sum(lastDigitList)
	ltTotal = sum(lastTwoDigitsList)
	fdpercentList = []
	ldpercentList = []
	ftpercentList = []
	ltpercentList = []
	for i in firstDigitList:
		fdPercent = (i) / (fdTotal)
		fdPercent = round(fdPercent * 100, 2)
		fdpercentList.append(fdPercent)
	for i in lastDigitList:
		ldPercent = (i) / (ldTotal)
		ldPercent = round(ldPercent * 100, 2)
		ldpercentList.append(ldPercent)
	for i in firstTwoDigitList:
		ftPercent = (i) / (ftTotal)
		ftPercent = round(ftPercent * 100, 2)
		ftpercentList.append(ftPercent)
	for i in lastTwoDigitsList:
		ltPercent = (i) / (ltTotal)
		ltPercent = round(ltPercent * 100, 2)
		ltpercentList.append(ltPercent)
	return fdpercentList, ldpercentList, ftpercentList, ltpercentList

#These will tell the function what to look at and the function to call for each. You do have to comment out the one you don't want to run.	
firstDigitList, firstTwoDigitList, lastDigitList, lastTwoDigitLists = powerCount()
firstDigitList, firstTwoDigitsList, lastDigitList, lastTwoDigitsList = fileCount('//winfile1/Students$/snewman/Desktop/rtTrmp.txt')
fdpercentList = percents(firstDigitList)
ftpercentList = percents(firstTwoDigitList)
ldpercentList = percents(lastDigitList)
ltpercentList = percents(lastTwoDigitsList)

def vertical():
	print("\t\t\tFirst Digit\t\tCount\t\t\tPercent\n")
	for i in range(0, 9):
		print ("\t\t\t", i, "\t\t\t", firstDigitList[i], "\t\t\t", fdpercentList[0][i])
	print()
	
	print("\t\t\tFirst Pair\t\tCount\t\t\tPercent\n")
	for i in range(10, 99):
		print("\t\t\t", i, "\t\t\t", firstTwoDigitsList[i], "\t\t\t", ftpercentList[1][i])
	print()
	
	print("\t\t\tLast Digit\t\tCount\t\t\tPercent\n")
	for i in range(0, 9):
		print("\t\t\t", i, "\t\t\t", lastDigitList[i], "\t\t\t", ldpercentList[2][i])
	print()
	
	print("\t\t\tLast Pair\t\tCount\t\t\tPercent\n")
	for i in range(10, 99):
		print("\t\t\t", i, "\t\t\t", lastTwoDigitsList[i], "\t\t\t", ltpercentList[3][i])
	print()

print(vertical())



def drawGrid(turtle, xMin, xMax, yMin, yMax, places) :
    turtle.penup()
    turtle.color('lightgray')
    #   Draw vertical lines.
    xGap = (xMax - xMin) / 10
    for i in range(1, 11) :
        turtle.goto(xMin + i * xGap, yMin)
        turtle.pendown()
        turtle.goto(xMin + i * xGap, yMax)
        turtle.penup()
    #   Draw horizontal lines.
    yGap = (yMax - yMin) / 10
    for i in range(1, 11) :
        turtle.goto(xMin, yMin + i * yGap)
        turtle.pendown()
        turtle.goto(xMax, yMin + i * yGap)
        turtle.penup()
    turtle.color('black')
    #   Write labels.
    for i in range(1, 11) :
        turtle.goto(-0.1, yMin + i * yGap)
        if places > 0  :
            turtle.write(str(round(yMin + i * yGap, places)))
        else :
            turtle.write(str(round(yMin + i * yGap)))
        if yMin > 0 :
            vPos = yMin + .1
        elif yMax < 0 :
            vPos = yMax - .1
        else :
            vPos = -.1
        turtle.goto(xMin + i * xGap, vPos) # -.1)
        if yMax - yMin < 2 :
            places = 2
        turtle.write(str(round(xMin + i * xGap, places)), align = 'center')

#   Draw the x axis if yMin < 0 < yMax.
def drawXAxis(turtle, a, b, step) :
    turtle.color('lightgray')
    turtle.penup()
    turtle.goto(a, 0)
    turtle.pendown()
    turtle.goto(b, 0)
    turtle.penup()
    turtle.goto(b - step, -step)
    turtle.write( 'x', font = FONT) #, True, 'left')

#   Draw the y axis.
def drawYAxis(turtle, a, b, step) :
    turtle.color('lightgray')
    turtle.penup()
    turtle.goto(0, a)
    turtle.pendown()
    turtle.goto(0, b)
    turtle.penup()
    turtle.goto(-2 * step, .9* b)
    turtle.write('y', font = FONT) #, True, 'right')



def drawLine(turtle, percentList, n, title):
	turtle.goto(50, 5)
	turtle.write(title, font=("Arial", 16, "normal"), align = 'center')
	turtle.penup()
	turtle.goto(10, percentList[n][10])
	turtle.pendown()
	for i in range(10, 99):
		turtle.goto(i, percentList[n][i])
	turtle.penup()
	
xMin = 0
xMax = 100
yMin = 0
yMax = 5
screen = turtle.Screen()
turtle.setworldcoordinates(xMin, yMin, xMax, yMax)
turtle.speed(0)
drawGrid(turtle, xMin, xMax, yMin, yMax, 0)
# drawLine(turtle, ftpercentList, 1, "Graph of First Two Digits (Percentages vs. Counts)")
drawLine(turtle, ltpercentList, 3, "Graph of Last Two Digits (Percentages vs. Counts)")
screen.mainloop()






