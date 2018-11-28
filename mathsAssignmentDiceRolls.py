#!/usr/bin/env python3 //Runs on Python 3

import random
import time
import math
import sys

#Input Granny numbers.
#Input Your numbers
#Generate random Granny Numbers
#Generate your random nuber

diceLowerLimit = 1
diceHigherLimit = 6
currentDiceRoll = 2

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

def grannyRandomRoll():
    global currentDiceRoll, grannyDiceOneNumberOne, grannyDiceOneNumberTwo, grannyDiceTwoNumberOne, grannyDiceTwoNumberTwo
    diceOneRandomSelection = random.randint(1,2)
    diceTwoRandomSelection = random.randint(1,2)
    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 1):
        grannyTotal = grannyDiceOneNumberOne + grannyDiceTwoNumberOne
        print("Granny rolled:" , grannyTotal)
    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 2):
        grannyTotal = grannyDiceOneNumberOne + grannyDiceTwoNumberTwo
        print("Granny rolled:" , grannyTotal)
    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 1):
        grannyTotal = grannyDiceOneNumberTwo + grannyDiceTwoNumberOne
        print("Granny rolled:" , grannyTotal)
    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 2):
        grannyTotal = grannyDiceOneNumberTwo + grannyDiceTwoNumberTwo
        print("Granny rolled:" , grannyTotal)
    currentDiceRoll += 1
    diceRollRandomisationDecision()

def youRandomRoll():
    global currentDiceRoll, youDiceOneNumberOne, youDiceOneNumberTwo, youDiceTwoNumberOne, youDiceTwoNumberTwo
    diceOneRandomSelection = random.randint(1,2)
    diceTwoRandomSelection = random.randint(1,2)
    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 1):
        yourTotal = youDiceOneNumberOne + youDiceTwoNumberOne
        print("You rolled:" , yourTotal)
    if (diceOneRandomSelection == 1 and diceTwoRandomSelection == 2):
        yourTotal = youDiceOneNumberOne + youDiceTwoNumberTwo
        print("You rolled:" , yourTotal)
    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 1):
        yourTotal = youDiceOneNumberTwo + youDiceTwoNumberOne
        print("You rolled:" , yourTotal)
    if (diceOneRandomSelection == 2 and diceTwoRandomSelection == 2):
        yourTotal = youDiceOneNumberTwo + youDiceTwoNumberTwo
        print("You rolled:" , yourTotal)
    currentDiceRoll += 1
    diceRollRandomisationDecision()

###PROGRAM EXECUTION###

startDiceRollsSelection() #Starts the program.