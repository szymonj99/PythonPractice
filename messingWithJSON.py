#!/usr/bin/env python3 //Runs on Python 3

#What this module will do:
#Open a test JSON file, or create an empty one if it doesn't exit
#Ask the end user for name and surname
#Store this data in the JSON database
#Possible data redundancy check before the new input data is stored

import os
import webbrowser
import json
import time
from colour import Color


fileName = "testJSONFile.json" #Used for testing, referenced later in code
errorMessage = "Cancelling operation."

def makeTextFile(): #Define function
    open(fileName,"w+") #Write permission, creating a file if it doesn't exist
    open(fileName,"w+").close() #closes the file

if os.path.exists(fileName):
    print(fileName,"already exists.")
else:
    makeTextFile()

#makeTextFile() #Have to change this to checking if file ezists first, or else it overwrites information

userName = input("What's your name?")
userSurname = input("What's your surname?")

print("Welcome,",userName,userSurname, "!")

def mainMenuFunc():
    mainMenuOptions = input("What do you want to do? You can save, open, or quit.")
    if mainMenuOptions == "save":
        storageQuestion = input("Do you want to store this information?")
        if storageQuestion == "yes":
            open(fileName,"w").write(userName)
            print(fileName,"was saved.")
            mainMenuFunc()
        else:
            print(errorMessage)
            mainMenuFunc()
        
    if mainMenuOptions == "open":
        openQuestion = input("Do you want to open your JSON file?")
        if openQuestion == "yes":
            webbrowser.open(fileName)
            print(fileName,"was opened.")
            mainMenuFunc()
        else:
            print(errorMessage)
            mainMenuFunc()
            
    if mainMenuOptions == "quit":
        quitQuestion = input("Do you want to quit?")
        if quitQuestion == "yes":
            print("Program will exit in 2 seconds.")
            time.sleep(1)
            print("Program will exit in 1 second.")
            time.sleep(1)
            exit()
        else:
            print(errorMessage)
            mainMenuFunc()

    else:
        print(errorMessage)
        mainMenuFunc()

mainMenuFunc()    