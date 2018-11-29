#!/usr/bin/env python3 //Runs on Python 3

import random
import time
import math
import sys
from colorama import Fore, Back, Style

######SETTING GAME VARIABLES######

diceLowerLimit = 1
diceHigherLimit = 6
currentDiceRoll = 2
grannyCurrentPosition = 1
yourCurrentPosition = 1
grannyLandedOnSnakes = 0
grannyLandedOnLadders = 0
youLandedOnSnakes = 0
youLandedOnLadders = 0
yourDiceRollTotal = 0
grannyDiceRollTotal = 0

######SETTING UP SNAKES######

snakeOneStart = 13
snakeOneFinish = 7
snakeTwoStart = 27
snakeTwoFinish = 15
snakeThreeStart = 69
snakeThreeFinish = 57
snakeFourStart = 75
snakeFourFinish = 43
snakeFiveStart = 94
snakeFiveFinish = 76

######SETTING UP LADDERS######

ladderOneStart = 18
ladderOneFinish = 38
ladderTwoStart = 45
ladderTwoFinish = 55
ladderThreeStart = 52
ladderThreeFinish = 62
ladderFourStart = 63
ladderFourFinish = 73
ladderFiveStart = 77
ladderFiveFinish = 87

#####QUICK STRING USED FOR USER INPUT RECOGNITION#####

yes = ("Y", "y", "yes", "Yes")
no = ("N", "n", "no", "No")

#Granny will have two dice, ONLY TWO numbers on each.
#You will also have two dice, ONLY TWO numbers on each.

def startDiceRollsSelection():
    grannyDiceOneNumberOneChoice()

########THIS IS FOR THE GRANNY PICKING DICE########

def grannyDiceOneNumberOneChoice():
    global grannyDiceOneNumberOne
    print("Granny Dice 1, Number 1:")
    grannyDiceOneNumberOne = int(input())

    if (grannyDiceOneNumberOne < 1) or (grannyDiceOneNumberOne > 6):
        print("Invalid number selected.")
        grannyDiceOneNumberOneChoice()

    elif (grannyDiceOneNumberOne > 0) and (grannyDiceOneNumberOne < 7):
        grannyDiceOneNumberTwoChoice()

def grannyDiceOneNumberTwoChoice():
    global grannyDiceOneNumberTwo
    print("Granny Dice 1, Number 2:")
    grannyDiceOneNumberTwo = int(input())

    if (grannyDiceOneNumberTwo < 1) or (grannyDiceOneNumberTwo > 6):
        print("Invalid number selected.")
        grannyDiceOneNumberTwoChoice()

    elif (grannyDiceOneNumberTwo > 0) and (grannyDiceOneNumberTwo < 7):
        grannyDiceTwoNumberOneChoice()

def grannyDiceTwoNumberOneChoice():
    global grannyDiceTwoNumberOne
    print("Granny Dice 2, Number 1:")
    grannyDiceTwoNumberOne = int(input())

    if (grannyDiceTwoNumberOne < 1) or (grannyDiceTwoNumberOne > 6):
        print("Invalid number selected.")
        grannyDiceTwoNumberOneChoice()

    elif (grannyDiceTwoNumberOne > 0) and (grannyDiceTwoNumberOne < 7):
        grannyDiceTwoNumberTwoChoice()

def grannyDiceTwoNumberTwoChoice():
    global grannyDiceTwoNumberTwo
    print("Granny Dice 2, Number 2:")
    grannyDiceTwoNumberTwo = int(input())

    if (grannyDiceTwoNumberTwo < 1) or (grannyDiceTwoNumberTwo > 6):
        print("Invalid number selected.")
        grannyDiceTwoNumberTwoChoice()

    elif (grannyDiceTwoNumberTwo > 0) and (grannyDiceTwoNumberTwo < 7):
        youDiceOneNumberOneChoice() #Select your dice after correctly picking granny's.

def printGrannyDice():
    print("Granny Dice 1: " + str(grannyDiceOneNumberOne) + "," + str(grannyDiceOneNumberTwo))
    print("Granny Dice 2: " + str(grannyDiceTwoNumberOne) + "," + str(grannyDiceTwoNumberTwo))

########THIS IS FOR YOU PICKING YOUR OWN DICE########

def youDiceOneNumberOneChoice():
    global youDiceOneNumberOne
    print("Your Dice 1, Number 1:")
    youDiceOneNumberOne = int(input())

    if (youDiceOneNumberOne < 1) or (youDiceOneNumberOne > 6):
        print("Invalid number selected.")
        youDiceOneNumberOneChoice()

    elif (youDiceOneNumberOne > 0) and (youDiceOneNumberOne < 7):
        youDiceOneNumberTwoChoice()

def youDiceOneNumberTwoChoice():
    global youDiceOneNumberTwo
    print("Your Dice 1, Number 2:")
    youDiceOneNumberTwo = int(input())

    if (youDiceOneNumberTwo < 1) or (youDiceOneNumberTwo > 6):
        print("Invalid number selected.")
        youDiceOneNumberTwoChoice()

    elif (youDiceOneNumberTwo > 0) and (youDiceOneNumberTwo < 7):
        youDiceTwoNumberOneChoice()

def youDiceTwoNumberOneChoice():
    global youDiceTwoNumberOne
    print("Your Dice 2, Number 1:")
    youDiceTwoNumberOne = int(input())

    if (youDiceTwoNumberOne < 1) or (youDiceTwoNumberOne > 6):
        print("Invalid number selected.")
        youDiceTwoNumberOneChoice()

    elif (youDiceTwoNumberOne > 0) and (youDiceTwoNumberOne < 7):
        youDiceTwoNumberTwoChoice()

def youDiceTwoNumberTwoChoice():
    global youDiceTwoNumberTwo
    print("Your Dice 2, Number 2:")
    youDiceTwoNumberTwo = int(input())

    if (youDiceTwoNumberTwo < 1) or (youDiceTwoNumberTwo > 6):
        print("Invalid number selected.")
        youDiceTwoNumberTwoChoice()

    elif (youDiceTwoNumberTwo > 0) and (youDiceTwoNumberTwo < 7):
        printBothDice() #Code should be changed to let the computer randomise the dice rolls.
        diceRollRandomisationDecision() #Executes method defined later.

def printYourDice():
    print("Your Dice 1: " + str(youDiceOneNumberOne) + "," + str(youDiceOneNumberTwo))
    print("Your Dice 2: " + str(youDiceTwoNumberOne) + "," + str(youDiceTwoNumberTwo))

###QUICK CODE TO PRINt BOTH DICE CHOICES###

def printBothDice():
    print() #Leaves a space before dice output. Looks cleaner in the terminal.
    printGrannyDice()
    print() #Leaves a space before dice output. Looks cleaner in the terminal.
    printYourDice()

###DICE ROLLS RANDOMISATION###
#Use modulus of 2 to see if number is odd or even.
#N = Roll number. Will start at 2, or any even number. Can't start at 2, 0%2. 
#If the modulus 2 of N = 0, Granny rolls randomly, one number from both dice. Add 1 to N.
#If the modulus 2 of N = 1, You roll randomly, one number from both dice. Add 1 to N.

def diceRollRandomisationDecision():
    global currentDiceRoll
    print("Roll again? [Yes/No]")
    userWantsNextRoll = input()

    if userWantsNextRoll in yes:

        if (currentDiceRoll % 2) == 0:
            grannyRandomRoll()

        elif (currentDiceRoll % 2) == 1:
            youRandomRoll()

    elif userWantsNextRoll in no:
        sys.exit(0)

    else:
        print("Command not recognized.")
        diceRollRandomisationDecision()

def checkForWinner():

    if (grannyCurrentPosition >= 100):
        print(Fore.MAGENTA)
        print("Granny Won!")
        print("Granny stepped on snakes" , grannyLandedOnSnakes , "times, and" , grannyLandedOnLadders , "times on ladders.")
        print("Granny Total Dice Rolls:" , grannyDiceRollTotal)
        print("Your Dice Roll Total:" , yourDiceRollTotal)
        print(Fore.GREEN)
        print("You stepped on snakes" , youLandedOnSnakes , "times, and" , youLandedOnLadders , "times on ladders.")
        print(Fore.WHITE)
        sys.exit(2)

    elif (yourCurrentPosition >= 100):
        print(Fore.GREEN)
        print("You won!")
        print("You stepped on snakes" , youLandedOnSnakes , "times, and" , youLandedOnLadders , "times on ladders.")
        print("Granny Total Dice Rolls:" , grannyDiceRollTotal)
        print("Your Dice Roll Total:" , yourDiceRollTotal)
        print(Fore.MAGENTA)
        print("Granny stepped on snakes" , grannyLandedOnSnakes , "times, and" , grannyLandedOnLadders , "times on ladders.")
        print(Fore.WHITE)
        sys.exit(2)

    else:
        diceRollRandomisationDecision()

def grannyRandomRoll():
    global grannyDiceRollTotal, grannyStartingPosition, grannyCurrentPosition, currentDiceRoll, grannyDiceOneNumberOne, grannyDiceOneNumberTwo, grannyDiceTwoNumberOne, grannyDiceTwoNumberTwo
    diceOneRandomSelection = random.randint(1,2)
    diceTwoRandomSelection = random.randint(1,2)
    print(Fore.MAGENTA)

    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 1):
        grannyTotal = grannyDiceOneNumberOne + grannyDiceTwoNumberOne
        print("Granny rolled:" , grannyTotal)
        grannyCurrentPosition = grannyCurrentPosition + grannyTotal
        didGrannyLandOnSnakeOrLadder()

    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 2):
        grannyTotal = grannyDiceOneNumberOne + grannyDiceTwoNumberTwo
        print("Granny rolled:" , grannyTotal)
        grannyCurrentPosition = grannyCurrentPosition + grannyTotal
        didGrannyLandOnSnakeOrLadder()

    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 1):
        grannyTotal = grannyDiceOneNumberTwo + grannyDiceTwoNumberOne
        print("Granny rolled:" , grannyTotal)
        grannyCurrentPosition = grannyCurrentPosition + grannyTotal
        didGrannyLandOnSnakeOrLadder()

    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 2):
        grannyTotal = grannyDiceOneNumberTwo + grannyDiceTwoNumberTwo
        print("Granny rolled:" , grannyTotal)
        grannyCurrentPosition = grannyCurrentPosition + grannyTotal
        didGrannyLandOnSnakeOrLadder()

    print(Fore.WHITE)
    grannyDiceRollTotal += 1
    currentDiceRoll += 1
    checkForWinner()

def didGrannyLandOnSnakeOrLadder():
    global grannyCurrentPosition, grannyLandedOnLadders, grannyLandedOnSnakes

    if (grannyCurrentPosition == snakeOneStart):
        grannyCurrentPosition = snakeOneFinish
        print("Granny landed on a snake!" , snakeOneStart, "to" , snakeOneFinish)
        grannyLandedOnSnakes += 1
    
    if (grannyCurrentPosition == snakeTwoStart):
        grannyCurrentPosition = snakeTwoFinish
        print("Granny landed on a snake!" , snakeTwoStart, "to" , snakeTwoFinish)
        grannyLandedOnSnakes += 1

    if (grannyCurrentPosition == snakeThreeStart):
        grannyCurrentPosition = snakeThreeFinish
        print("Granny landed on a snake!" , snakeThreeStart, "to" , snakeThreeFinish)
        grannyLandedOnSnakes += 1

    if (grannyCurrentPosition == snakeFourStart):
        grannyCurrentPosition = snakeFourFinish
        print("Granny landed on a snake!" , snakeFourStart, "to" , snakeFourFinish)
        grannyLandedOnSnakes += 1

    if (grannyCurrentPosition == snakeFiveStart):
        grannyCurrentPosition = snakeFiveFinish
        print("Granny landed on a snake!" , snakeFiveStart, "to" , snakeFiveFinish)
        grannyLandedOnSnakes += 1

    if (grannyCurrentPosition == ladderOneStart):
        grannyCurrentPosition = ladderOneFinish
        print("Granny landed on a ladder!" , ladderOneStart, "to" , ladderOneFinish)
        grannyLandedOnLadders += 1

    if (grannyCurrentPosition == ladderTwoStart):
        grannyCurrentPosition = ladderTwoFinish
        print("Granny landed on a ladder!" , ladderTwoStart, "to" , ladderTwoFinish)
        grannyLandedOnLadders += 1

    if (grannyCurrentPosition == ladderThreeStart):
        grannyCurrentPosition = ladderThreeFinish
        print("Granny landed on a ladder!" , ladderThreeStart, "to" , ladderThreeFinish)
        grannyLandedOnLadders += 1
    
    if (grannyCurrentPosition == ladderFourStart):
        grannyCurrentPosition = ladderFourFinish
        print("Granny landed on a ladder!" , ladderFourStart, "to" , ladderFourFinish)
        grannyLandedOnLadders += 1

    if (grannyCurrentPosition == ladderFiveStart):
        grannyCurrentPosition = ladderFiveFinish
        print("Granny landed on a ladder!" , ladderFiveStart, "to" , ladderFiveFinish)
        grannyLandedOnLadders += 1

    print(Fore.MAGENTA)
    print("Granny is on position:" , grannyCurrentPosition)
    print(Fore.WHITE)

def youRandomRoll():
    global yourDiceRollTotal, playerDiceRollTotal, yourStartingPosition, yourCurrentPosition, currentDiceRoll, youDiceOneNumberOne, youDiceOneNumberTwo, youDiceTwoNumberOne, youDiceTwoNumberTwo
    diceOneRandomSelection = random.randint(1,2)
    diceTwoRandomSelection = random.randint(1,2)
    print(Fore.GREEN)

    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 1):
        yourTotal = youDiceOneNumberOne + youDiceTwoNumberOne
        print("You rolled:" , yourTotal)
        yourCurrentPosition = yourCurrentPosition + yourTotal
        didYouLandOnSnakeOrLadder()

    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 2):
        yourTotal = youDiceOneNumberOne + youDiceTwoNumberTwo
        print("You rolled:" , yourTotal)
        yourCurrentPosition = yourCurrentPosition + yourTotal
        didYouLandOnSnakeOrLadder()

    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 1):
        yourTotal = youDiceOneNumberTwo + youDiceTwoNumberOne
        print("You rolled:" , yourTotal)
        yourCurrentPosition = yourCurrentPosition + yourTotal
        didYouLandOnSnakeOrLadder()

    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 2):
        yourTotal = youDiceOneNumberTwo + youDiceTwoNumberTwo
        print("You rolled:" , yourTotal)
        yourCurrentPosition = yourCurrentPosition + yourTotal
        didYouLandOnSnakeOrLadder()

    print(Fore.WHITE)
    yourDiceRollTotal += 1
    currentDiceRoll += 1
    checkForWinner()

def didYouLandOnSnakeOrLadder():
    global yourCurrentPosition, youLandedOnLadders, youLandedOnSnakes

    if (yourCurrentPosition == snakeOneStart):
        yourCurrentPosition = snakeOneFinish
        print("You landed on a snake!" , snakeOneStart, "to" , snakeOneFinish)
        youLandedOnSnakes += 1
    
    if (yourCurrentPosition == snakeTwoStart):
        yourCurrentPosition = snakeTwoFinish
        print("You landed on a snake!" , snakeTwoStart, "to" , snakeTwoFinish)
        youLandedOnSnakes += 1

    if (yourCurrentPosition == snakeThreeStart):
        yourCurrentPosition = snakeThreeFinish
        print("You landed on a snake!" , snakeThreeStart, "to" , snakeThreeFinish)
        youLandedOnSnakes += 1

    if (yourCurrentPosition == snakeFourStart):
        yourCurrentPosition = snakeFourFinish
        print("You landed on a snake!" , snakeFourStart, "to" , snakeFourFinish)
        youLandedOnSnakes += 1

    if (yourCurrentPosition == snakeFiveStart):
        yourCurrentPosition = snakeFiveFinish
        print("You landed on a snake!" , snakeFiveStart, "to" , snakeFiveFinish)
        youLandedOnSnakes += 1

    if (yourCurrentPosition == ladderOneStart):
        yourCurrentPosition = ladderOneFinish
        print("You landed on a ladder!" , ladderOneStart, "to" , ladderOneFinish)
        youLandedOnLadders += 1

    if (yourCurrentPosition == ladderTwoStart):
        yourCurrentPosition = ladderTwoFinish
        print("You landed on a ladder!" , ladderTwoStart, "to" , ladderTwoFinish)
        youLandedOnLadders += 1

    if (yourCurrentPosition == ladderThreeStart):
        yourCurrentPosition = ladderThreeFinish
        print("You landed on a ladder!" , ladderThreeStart, "to" , ladderThreeFinish)
        youLandedOnLadders += 1
    
    if (yourCurrentPosition == ladderFourStart):
        yourCurrentPosition = ladderFourFinish
        print("You landed on a ladder!" , ladderFourStart, "to" , ladderFourFinish)
        youLandedOnLadders += 1

    if (yourCurrentPosition == ladderFiveStart):
        yourCurrentPosition = ladderFiveFinish
        print("You landed on a ladder!" , ladderFiveStart, "to" , ladderFiveFinish)
        youLandedOnLadders += 1

    print(Fore.GREEN) #Changes terminal colour to green
    print("You are on position:" , yourCurrentPosition)
    print(Fore.WHITE) #changes terminal colour to white

###PROGRAM EXECUTION###

startDiceRollsSelection() #Starts the program.