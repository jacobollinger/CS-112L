# Lab9: Design software to play a game called Flip on the console.
# By Jacob Bollinger

from random import randint, sample
import turtle

def intitializeLists():
    rDice = []
    mDice = []
    pDice = []
    for i in range(5):
        rDice.append(randint(1, 6))
        pDice.append(randint(1, 6))
    rDice.sort()
    mDice.sort()
    pDice.sort()
    return rDice, mDice, pDice

def displayLists(robotList, middleList, humanList):
    print('Robot List:', robotList)
    print('Middle List:', middleList)
    print('Human List:', humanList)

def moveHuman(graphical, r, m, p):
    if(graphical):
        x=0
    else:
        displayLists(r, m, p)
        move = input('Please enter a move with fD or tD where D is a digit')
    return move

def moveRobot(r, m, p):
    moveChoice = ['f', 't']
    digitChoice = [1, 2, 3, 4, 5]
    digitChoice = digitChoice[0:len(p)]
    move = sample(moveChoice, 1)
    digit = sample(digitChoice, 1)
    return move, digit

def humanTurn(move, r, m, p):
    if(move[0] == 'f'):
        flip(move[1], p)
    elif(move[0] == 't'):
        trash(move[1], r, m, p, True)

def robotTurn(move, r, m, p):
    if(move[0] == 'f'):
        flip(move[1], r)
    elif(move[0] == 't'):
        trash(move[1], r, m, p, False)

def trash(digit, r, m, p, isHuman):
    digit = int(digit)
    if isHuman:
        m.append(r[digit - 1])
        r.remove(r[digit - 1])
        if((len(m) > 2) and ((m[0] + m[1]) <= m[-1])):
            p.append(m[0])
            p.append(m[1])
            m.remove(m[1])
            m.remove(m[0])
    else:
        displayLists()
        m.append(r[digit - 1])
        p.remove(p[digit - 1])
        if((len(m) > 2) and ((m[0] + m[1]) <= m[-1])):
            r.append(m[0])
            r.append(m[1])
            m.remove(m[1])
            m.remove(m[0])
    r.sort()
    m.sort()
    p.sort()

def flip(digit, correctList):
    digit = int(digit)
    correctList[digit - 1] = 7 - correctList[digit - 1]

def main(graphical):
    pWins = 0
    rWins = 0
    robotList, middleList, humanList = intitializeLists()
    while(len(humanList) != 0 and len(robotList) != 0):
        move = moveHuman(robotList, middleList, humanList)
        humanTurn(move, robotList, middleList, humanList)
        if(robotList == []):
            print('Player wins.')
            pWins += 1
        else:
            # displayLists(robotList, middleList, humanList)
            move = moveRobot(robotList, middleList, humanList)
            # print(move)
            robotTurn(move, robotList, middleList, humanList)

def graphicalGame():
    pWins = 0
    rWins = 0
    robotList, middleList, humanList = intitializeLists()
    while(len(humanList) != 0 and len(robotList) != 0):
        move = moveHuman(robotList, middleList, humanList)


main(True)
