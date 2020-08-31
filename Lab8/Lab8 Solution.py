# Lab7: Design software to illustrate Benford's law. 
# By Jacob Bollinger and Samantha Anderson 

from urllib.request import urlopen
import math, turtle

# Constants
#DATA_SET = open('/Users/hackerman/Documents/VSCode/CS-112/Lab7/lab7_data.txt')
WEB_FILE = urlopen('http://facstaff.cbu.edu/~yanushka/py/lab7/lj.txt')
TRUMPTWEET = urlopen('http://facstaff.cbu.edu/~yanushka/py/lab7/rtTrmp.txt')

FONT = ( 'Arial', 12, 'normal' )
HORIZONTAL_PIXELS = 400

# Reads the file and calls the other functions
def processFile(fIn) :
    firstDigitList = [0] * 10
    first2DigitsList = [0] * 100
    lastDigitList = [0] * 10
    last2DigitsList = [0] * 100
    count = 0
    for line in fIn :
        line = line.decode('utf-8').strip()
        count += 1
        if count > 2 :
            firstDigit = int(line[0])
            first2Digits = int(line[:2])
            lastDigit = int(line[-1])
            last2Digits = int(line[-2:])
            firstDigitList[firstDigit] += 1
            first2DigitsList[first2Digits] += 1
            lastDigitList[lastDigit] += 1
            last2DigitsList[last2Digits] += 1
    firstDigitListPercent = getPercent(firstDigitList)
    first2DigitsListPercent = getPercent(first2DigitsList)
    lastDigitListPercent = getPercent(lastDigitList)
    last2DigitsListPercent = getPercent(last2DigitsList)
     
    returnTables(firstDigitList, firstDigitListPercent, 1,10,"First Digit Distribution")
    returnTables(lastDigitList, lastDigitListPercent, 1, 10,"Last Digit Distribution")
    returnTables(first2DigitsList, first2DigitsListPercent, 0,100,"First Digit Pair Distribution")
    returnTables(last2DigitsList, last2DigitsListPercent,10, 100,"Last Digit Pair Distribution")

#function to create percentage for any data set 
def getPercent(list1) :
    percent = []
    for n in list1 :
        percent.append(round(n / sum(list1) * 100, 2))
    return percent

#takes two lists and creates corresponding tables
def returnTables(rawCount, percCount, low, high, title) :

    num_tables = math.ceil((high - low) / 10)
    print(title, end="\n")
    for i in range(num_tables):
        table_low = low + i * 10
        table_high = min(table_low + 10, high)

        print("  Digit:", end="\t")
        for digit in range(table_low, table_high):
            print(digit, end = '\t')
        print('')
        print("  Count:", end="\t")
        for count in rawCount[table_low:table_high] :
            print(count, end = '\t')
        print('')
        print("Percent:", end="\t")
        for percent in percCount[table_low:table_high] :
            print(percent, end = '\t')
        print('')
    print("")

#Wikipedia function testing benford's law  
def powersOfTwo(n):
    oldpower = 1
    firstDigitList = [0] * 10
    first2DigitsList = [0] * 100
    lastDigitList = [0] * 10
    last2DigitsList = [0] * 100
    firstDigitListPercent = []
    first2DigitsListPercent = []
    lastDigitListPercent = []
    last2DigitsListPercent = []
    for i in range(n):
        number = str(oldpower)
        oldpower = oldpower * 2
        
        firstDigit = int(number[0])
        first2Digits = int(number[:2])
        lastDigit = int(number[-1])
        last2Digits = int(number[-2:])

        firstDigitList[firstDigit] += 1
        first2DigitsList[first2Digits] += 1
        lastDigitList[lastDigit] += 1
        last2DigitsList[last2Digits] += 1

    firstDigitListPercent = getPercent(firstDigitList)
    first2DigitsListPercent = getPercent(first2DigitsList)
    lastDigitListPercent = getPercent(lastDigitList)
    last2DigitsListPercent = getPercent(last2DigitsList)

    
    returnTables(firstDigitList, firstDigitListPercent, 1,10,"First Digit Distribution")
    returnTables(lastDigitList, lastDigitListPercent, 1, 10,"Last Digit Distribution")
    returnTables(first2DigitsList, first2DigitsListPercent, 10,100,"First Digit Pair Distribution")
    returnTables(last2DigitsList, last2DigitsListPercent,10, 100,"Last Digit Pair Distribution")



#   Draw a grid for the graph in the window xMin to xMax by yMin to yMax.
#   Places indicate the number of decimals in the x and y labels.

#   Draw the x axis if yMin < 0 < yMax.

#   Draw the y axis.


# Outputs

# processFile(WEB_FILE)
# processFile(TRUMPTWEET)
# powersOfTwo(10000)
