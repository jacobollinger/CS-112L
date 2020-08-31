# Lab9: Design software to play a game called Flip on the console.
# By Jacob Bollinger

from random import randint

def trashOrFlip():
    rand = randint(1, 2)
    if(rand == 1):
        n = 'trash'
    elif(rand == 2):
        n = 'flip'
    return n

def intitializeLists():
    rDice = []
    pDice = []
    mDice = []
    for i in range(6):
        rDice.append(randint(1, 6))
        pDice.append(randint(1, 6))

def trash(die, r, p, m):
    return 0

def flip(die):
    return 7 - die

def game():
    rWins = 0
    pWins = 0
    
    

    while(rDice != [] or pDice != []):
        print("Player's Dice: ", pDice)
        print("Robot's Dice: ", rDice)
        choice = trashOrFlip()
        if(choice == 'trash'):
            trash(rDice[randint(6)], rDice, pDice, mDice)
        elif(choice == 'flip'):
            flip(rDice[randint(6)])
            
    if(rDice == []):
        print('Robot wins.')
        rWins += 1
    elif(pDice == []):
        print('Player wins.')
        pWins += 1

game()