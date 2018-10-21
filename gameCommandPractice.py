#!/usr/bin/env python3 //Runs on Python 3

import json
import os
import pprint
import random
import time
import math

#Commands to include are sleep, fight.
#Sleeping will heal player
#Fighting will damage player and provide money

fight = ("fight", "Fight", "f", "F")
sleep = ("sleep", "Sleep", "S", "s")

#Character and enemy stats. Taken from gameLogicEquations.py

playerLevel = 45
playerStrength = 70
playerHealth = playerLevel + round(playerStrength/2)
playerDamageMultiplier = 1.45 + playerLevel/100
playerDamageLowerRange = playerStrength + 5
playerDamageUpperRange = (playerStrength + 5) * playerDamageMultiplier
playerHitChance = 85
enemyLevel = 37
enemyStrength = 41
enemyHealth = enemyLevel + round(enemyStrength/2)
enemyArmour = 150
enemyDamageReduce = math.sqrt(enemyArmour) + enemyLevel

nextMoveMessage = "What is your next move?"

def mainMenu():
    global fight
    global sleep
    global nextMoveMessage
#    print("What is your next move?") #Could change into playerChoice = input("What is your next move?")
    playerChoice = input() #Not necessary. Could use input() without assigning local variable.
    if playerChoice in fight:
        print("You are fighting!")
        print(playerLevel) #Test to see if import gameLogicEquations will output correct value for one character stat.
        print(nextMoveMessage)
        mainMenu()
    elif playerChoice in sleep:
        print("You rest and feel refreshed...\n"+nextMoveMessage)
        mainMenu()
    else:
        print("Unknown command. Try again.")
        mainMenu()

print(nextMoveMessage)
mainMenu()