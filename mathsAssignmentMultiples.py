#!/usr/bin/env python3 //Runs on Python 3

import random
import math

boardLimit = 100
twoDiceLowerLimit = 7
twoDiceUpperLimit = 12

def userDecidesNumber():
    global userNumber, boardLimit, howManyTimesUserInputGoesIntoBoardLimit
    userNumber = input()
    if (int(userNumber) > 6 and int(userNumber) < 13):
        multipleTimes = round((boardLimit / int(userNumber)))
        print(userNumber, "goes into", boardLimit, ",", multipleTimes, "times.")
        for i in range (int(userNumber),(boardLimit+1),+int(userNumber)): #Ensures boardLimit is inclusive.
            print(i)
        userDecidesNumber()
    else:
        print("Input must be a number between", twoDiceLowerLimit, "and", twoDiceUpperLimit, "inclusive.")
        userDecidesNumber()

print("What would you like to find the multiples of?")
userDecidesNumber()