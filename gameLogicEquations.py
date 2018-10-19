#!/usr/bin/env python3 //Runs on Python 3

#This python module is used to test possible implementations of formulas and logic the game will use to determine damage dealt etc.

import json
import os
import pprint
import random
import time
import math

#Should use JSON file to store the character values
playerLevel = 1
playerHealth = 50
playerStrength = 5
playerDamageMultiplier = 1.1 + playerLevel/100
playerDamageLowerRange = playerStrength + 5
playerDamageUpperRange = (playerStrength + 5) * playerDamageMultiplier
playerHitChance = 90
enemyLevel = 1
enemyArmour = 3
enemyDamageReduce = math.sqrt(enemyArmour) + enemyLevel

#Used for testing to display proper rounding of numbers and proper and well-scaling logic.

n = 10
testTotal = 0
totalMisses = 0

for i in range (n,0,-1):
    enemyHitEvasion = random.randint(0,100)
    if (playerHitChance > enemyHitEvasion):
        playerDamage = random.uniform(playerDamageLowerRange-enemyDamageReduce,playerDamageUpperRange-enemyDamageReduce)
        testTotal = testTotal + (round(playerDamage))
#        print(round(playerDamage))
    else:
        totalMisses += 1


averageDamage = testTotal/n
print("Total misses:",totalMisses,".")
print("The total damage dealt over",n,"tries, was",testTotal)
print("The average damage dealt was",(round(averageDamage)),".")

