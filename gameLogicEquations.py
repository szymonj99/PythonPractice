#!/usr/bin/env python3 //Runs on Python 3

#This python module is used to test possible implementations of formulas and logic the game will use to determine damage dealt etc.

import json
import os
import pprint
import random
import time
import math

#Should use JSON file to store the character values
playerLevel = 45
playerHealth = 50
playerStrength = 70
playerDamageMultiplier = 1.45 + playerLevel/100
playerDamageLowerRange = playerStrength + 5
playerDamageUpperRange = (playerStrength + 5) * playerDamageMultiplier
playerHitChance = 85
enemyLevel = 37
enemyArmour = 150
enemyDamageReduce = math.sqrt(enemyArmour) + enemyLevel

n = 50000
testTotal = 0 
totalMisses = 0 
noLoot = 0 # 70%
commonLoot = 0 #17%
uncommonLoot = 0 #9%
rareLoot = 0 # 3%
specialLoot = 0 # 1%

for i in range (n,0,-1):
    enemyHitEvasion = random.randint(0,100)
    if (playerHitChance > enemyHitEvasion):
        playerDamage = random.uniform(playerDamageLowerRange-enemyDamageReduce,playerDamageUpperRange-enemyDamageReduce)
        testTotal = testTotal + (round(playerDamage))
        lootGenerator = random.uniform(0,100)
        if (lootGenerator <= 70):
            noLoot += 1
        elif (lootGenerator <= 87) and (lootGenerator > 70):
            commonLoot += 1
        elif (lootGenerator <= 96) and (lootGenerator > 87):
            uncommonLoot += 1
        elif (lootGenerator <= 99) and (lootGenerator > 96):
            rareLoot += 1
        else:
            specialLoot += 1

#        print(round(playerDamage)) #Used for testing to display proper rounding of numbers and proper and well-scaling logic. Works correctly, so disabled.
    else:
        totalMisses += 1

totalLoot = commonLoot + uncommonLoot + rareLoot + specialLoot
lootPercentage = (totalLoot/n)*100
averageDamage = testTotal/n
percentageMiss = (totalMisses/n)*100
print("Average miss rate was",(round(percentageMiss, 2)),"%")
print("Total misses:",totalMisses,".")
print("The total damage dealt over",n,"tries, was",testTotal)
print("The average damage dealt was",(round(averageDamage)),".")
print("Total loot received is",totalLoot)
print("No Loot:", noLoot)
print("Common Loot:", commonLoot)
print("Uncommon Loot:", uncommonLoot)
print("Rare Loot:", rareLoot)
print("Special Loot:", specialLoot)
print("Loot drop percentage was",(round(lootPercentage,2)),"%.")

