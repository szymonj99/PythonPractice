#!/usr/bin/env python3 //Runs on Python 3

import random #Will be used for random numbers
import time

lowerRange = 1 #Defines the lower range for user to guess from
upperRange = 10 #Defines the upper range for user to guess to

randomNumber = random.randint(lowerRange,upperRange) #randomNumber is picked between 1 and 10
userTries = 1 #Give the user only one try

print(randomNumber) #Used for debugging. Comment out later!!
userName = input("Hi! What's your name?") #Prompt the end user for their name

print("Welcome," + userName + "!")

startQuestion = input("Want to play a game? [Yes/No]")
if startQuestion == "no":
    print("Okay, bye!")
    time.sleep(2)
    exit()
#elif startQuestion == "edit" or "e": #Here to later add the ability to change the guessing limits

elif startQuestion == "yes":
    print("Sweet!")
    time.sleep(0.100)
    print("I'm thinking of a number between",lowerRange,"and",upperRange,".")
    userGuess = int(input("Your guess: "))
    if userGuess > randomNumber:
        print("Guess lower!")
if userGuess < randomNumber:
    print("Guess higher!")
while userGuess != randomNumber: #on every failed guess
    userTries += 1 #Add 1 to user tries after every failed attempt
    userGuess = int(input("Try again!"))
    if userGuess < randomNumber:
        print("Guess higher!")
    if userGuess > randomNumber:
        print("Guess lower!")
if userGuess == randomNumber:
    print("You are correct! The number was",randomNumber, \
    "and it took you",userTries,"tries!")