# Lab9: Design software to play a game called Flip on the console.
# By Jacob Bollinger and David Huang

from random import randint, sample

# Initializes the three list required to play and sorts them.
def intitializeLists():
    rDice = []
    mDice = []
    pDice = []
    rFDice = [False] * 5
    hFDice = [False] * 5
    for i in range(5):
        rDice.append(randint(1, 6))
        pDice.append(randint(1, 6))
    rDice.sort()
    mDice.sort()
    pDice.sort()
    return rDice, mDice, pDice, rFDice, hFDice

# Displays the three lists.
def displayLists(robotList, middleList, humanList):
    print('Robot List:', robotList)
    print('Middle List:', middleList)
    print('Human List:', humanList)

# Returns an input from the keyboard.
def moveHuman(r, m, h):
    displayLists(r, m, h)
    # move = input('Please enter a move with fD or tD where D is a digit')
    
    moveChoice = ['f', 't']
    digitChoice = [1, 2, 3, 4, 5]
    move = sample(moveChoice, 1)
    if(move[0] == 'f'):
        digitChoice = digitChoice[0:len(h)]
    else:
        digitChoice = digitChoice[0:len(r)]
    digit = sample(digitChoice, 1)
    return move[0], digit[0]
    
    # return move

# returns a random move and digit for the robot.
def moveRobot(r, m, h):
    displayLists(r, m, h)
    moveChoice = ['f', 't']
    digitChoice = [1, 2, 3, 4, 5]
    move = sample(moveChoice, 1)
    if(move[0] == 'f'):
        digitChoice = digitChoice[0:len(r)]
    else:
        digitChoice = digitChoice[0:len(h)]
    digit = sample(digitChoice, 1)
    return move[0], digit[0]

# Takes input from human and executes it.
def humanTurn(move, r, m, h, robotForbiddenList, humanForbiddenList):
    if(move[0] == 'f'):
        flip(move[1], h, True, humanForbiddenList)
    elif(move[0] == 't'):
        humanForbiddenList = trash(move[1], r, m, h, True, robotForbiddenList, humanForbiddenList)
    return humanForbiddenList

# Takes input from robot and executes it.
def robotTurn(move, r, m, h, robotForbiddenList, humanForbiddenList):
    if(move[0] == 'f'):
        flip(move[1], r, False, robotForbiddenList)
    elif(move[0] == 't'):
        robotForbiddenList = trash(move[1], r, m, h, False, robotForbiddenList, humanForbiddenList)
    return robotForbiddenList

# Executes the trash move for a digit in a list.
def trash(digit, r, m, h, isHuman, robotForbiddenList, humanForbiddenList):
    if isHuman:
        digit = int(digit)
        m.append(r[digit - 1])
        trashed = r[digit - 1]
        robotForbiddenList.remove(robotForbiddenList[digit - 1])
        r.remove(r[digit - 1])
        takes = 'nothing'
        # if((len(m) > 2) and ((m[0] + m[1]) <= m[-1])):
        if((len(m) > 2) and (m[0] <= m[-1])):
            r.append(m[0])
            robotForbiddenList.append(False)
            takes = m[0]
            m.remove(m[0])
        print('Human trashes', trashed, '. Robot takes', takes)
    else:
        displayLists(r, m, h)
        m.append(h[digit - 1])
        trashed = h[digit - 1]
        humanForbiddenList.remove(humanForbiddenList[digit - 1])
        h.remove(h[digit - 1])
        takes = 'nothing'
        # if((len(m) > 2) and ((m[0] + m[1]) <= m[-1])):
        if((len(m) > 2) and (m[0] <= m[-1])):
            h.append(m[0])
            humanForbiddenList.append(False)
            takes = m[0]
            m.remove(m[0])
        print('Robot trashes', trashed, '. Human takes', takes)
    # r.sort()
    m.sort()
    # h.sort()
    forbiddenList = [False] * 5
    return forbiddenList

# Executes the flip move for a digit in a list.
def flip(digit, correctList, isHuman, forbiddenList):
    if isHuman:
        digit = int(digit)
        print('Human flips', correctList[digit - 1])
    else:
        print('Robot flips', correctList[digit - 1])
    correctList[digit - 1] = 7 - correctList[digit - 1]
    forbiddenList[digit -1] = True

# Calls all of the other functions and keeps the game running.
def main():
    playing = True
    hWins = 0
    rWins = 0
    i = 0
    while(i < 10000): # playing):
        robotList, middleList, humanList, robotForbiddenList, humanForbiddenList = intitializeLists()
        while(len(humanList) != 0 and len(robotList) != 0):
            found = False
            while(not found):
                move = moveHuman(robotList, middleList, humanList)
                if(move[0] == 't'):
                    found = True
                elif(humanForbiddenList[int(move[1]) - 1] == False):
                    found = True
                else:
                    print('You have already flipped this die. Choose a different move.')
            humanForbiddenList = humanTurn(move, robotList, middleList, humanList, robotForbiddenList, humanForbiddenList) 
            if(robotList == []):
                hWins += 1
                print('Player wins.')
                print('Robot: ', rWins)
                print('Human: ', hWins)
            else:
                found = False
                while(not found):
                    move = moveRobot(robotList, middleList, humanList)
                    if(move[0] == 't'):
                        found = True
                    elif(robotForbiddenList[move[1] - 1] == False):
                        found = True
                robotForbiddenList = robotTurn(move, robotList, middleList, humanList, robotForbiddenList, humanForbiddenList)
                if(humanList == []):
                    rWins += 1
                    print('Robot wins.')
                    print('Robot: ', rWins)
                    print('Human: ', hWins)
                    
        if(True): # input('Do you want to play again? Y/N').lower() == 'y'):
            playing = True
            i += 1
        else:
            playing = False
        

main()

# Look back
# In this lab we learned how to play the game flip.
# We learned how to design this game with certain moves and rules and convert it into code.
# We learned how to use the input command to take input from a person via the keyboard.
# We strengthened our understanding of python and problem solving.
