#!/usr/bin/env python3 //Runs on Python 3

import random

playerHitChance = 65

def didPlayerHitOrMiss():
    global playerHitChance
    randomNumGen0To100 = random.randint(0,100)
    if (playerHitChance >= randomNumGen0To100):
        print(playerHitChance, "is bigger than", randomNumGen0To100)
    else:
        print(randomNumGen0To100, "is bigger than", playerHitChance)

for i in range (10,0,-1):
    didPlayerHitOrMiss()