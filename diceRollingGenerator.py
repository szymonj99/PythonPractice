#!/usr/bin/env python3 //Runs on Python 3

import random

diceLowerLimit = 1
diceUpperLimit = 6

def diceThrow():
    diceResult = random.randint(diceLowerLimit,diceUpperLimit)
    print("You threw:",diceResult,".")
    diceAnotherThrow = input("Do you wish to throw again?\n")
    if diceAnotherThrow == "yes" or diceAnotherThrow == "y":
        diceThrow()
    else:
        exit()

diceThrow()