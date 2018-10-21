#!/usr/bin/env python3 //Runs on Python 3

#Importing dependencies

import json
import os
import pprint
import random
import time
import math

#Commands to include are sleep, fight.
#Sleeping will heal player
#Fighting will damage player and provide money

#Quick setting of variables to scan for answers to multiple choice user questions.

fight = ("fight", "Fight", "f", "F")
sleep = ("sleep", "Sleep", "S", "s")
flee = ("Flee", "flee")

#Character and enemy stats. Taken from gameLogicEquations.py

playerLevel = 1
playerStrength = 15
playerHealth = playerLevel + round(playerStrength/2)
playerDamageMultiplier = 1.125 + playerLevel/100
playerDamageLowerRange = playerStrength + 5
playerDamageUpperRange = (playerStrength + 5) * playerDamageMultiplier
playerHitChance = 85 #%
playerCurrentExperience = 0 #Should set up an XP table, or think of a formula.
playerRequiredExperience = round((playerLevel+5) ** 2)#The total Experience points the player needs to level up.

#Enemy scaling could potentially be adjusted. Need to create unique enemy every occurence of playerFight().
#enemyLevel = round(random.uniform(playerLevel-2,playerLevel+5)) #Enemy level is somewhere within -2 to +5 levels within player.
#enemyStrength = round(random.uniform(enemyLevel+5,(enemyLevel+5)*1.35)) #
#enemyHealth = enemyLevel + round(enemyStrength/2)
#enemyArmour = random.randint(enemyLevel*3.5,enemyLevel*7)
#enemyDamageReduce = math.sqrt(enemyArmour) + enemyLevel

#Example messages for convenience.

nextMoveMessage = "What is your next move?"
fightBeginMessage = "You are fighting!"
fightWinMessage = "You won!"
fightLossMessage = "You lost..."

#Methods

def mainMenu():
    global fight, sleep, nextMoveMessage
#    print("What is your next move?") #Could change into playerChoice = input("What is your next move?")
    playerChoice = input() #Not necessary. Could use input() without assigning local variable.
    if playerChoice in fight:
        playerFight()
    elif playerChoice in sleep:
        playerSleep()
    else:
        print("Unknown command. Try again.")
        mainMenu()

def playerFight():
    global flee, fight
    if (playerLevel == 1): #Adding some level 1-3 enemy variations.
        enemyLevel = random.randint(playerLevel,playerLevel+2) #Enemy level is somewhere within -2 to +5 levels within player. Trouble when player level is 1-3. Need to fix.
    elif (playerLevel == 2):
        enemyLevel = random.randint(playerLevel-1,playerLevel+3)
    elif (playerLevel == 3):
        enemyLevel = random.randint(playerLevel-2,playerLevel+4)
    else:
        enemyLevel = random.randint(playerLevel-2,playerLevel+5)
    enemyStrength = round(random.uniform(enemyLevel+5,(enemyLevel+5)*1.35)) #
    enemyHealth = enemyLevel + round(enemyStrength/2)
    enemyArmour = round(random.uniform(enemyLevel*3,enemyLevel*7))
    enemyDamageReduce = round(math.sqrt(enemyArmour) + enemyLevel)
    print(fightBeginMessage)

    #Instead of using multipel print commands, coud use one print with new lines \n \.

    print("Enemy statistics:")
    print("     Level:",enemyLevel)
    print("     Health:",enemyHealth)
    print("     Strength:",enemyStrength)
    print("     Armour:",enemyArmour)
    print("     Damage Reduce:",enemyDamageReduce)
    playerFightOrFlee = input("What do you wish to do?")
    if playerFightOrFlee in fight:
        print("You have decided to fight!")
    elif playerFightOrFlee in flee:
        print("You have decided to flee!")
    mainMenu()


def playerSleep():
    mainMenu()

#Code to be executed at launch, excluding initial setting of variables

print(nextMoveMessage)
mainMenu()