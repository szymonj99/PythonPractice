#!/usr/bin/env python3 //Runs on Python 3

import json
import os
import pprint
import random
import time

fileName = "saveFile.json"
errorMessage = "Error. Unknown or unexpected input."
characterName = "startOfGamePlaceholderName" #global variable, not used correctly. Later function only changes value for local variable in function.
characterClass = "startOfGamePlaceholderClass"


def makeSaveFile(): #Define function
    open(fileName,"w+") #Write permission, creating a file if it doesn't exist
    open(fileName,"w+").close() #closes the file. Possibly makes previous line redundant

def makeCharacterMenu():
    global characterName
    global characterClass
    characterName = input("What would you like to be called?\n")
    characterClass = input("What class do you want to be? [Warrior/Archer/Mage]\n")
    
    if characterClass == "Warrior":
        characterClassConfirmation = input("You have chosen Warrior. Are you sure? [Yes/Y/No]\n")
        if characterClassConfirmation == "Yes" or characterClassConfirmation == "y":
            print("Class confirmed.")
            gameInterface()
        else:
            makeCharacterMenu()
    
    if characterClass == "Archer":
        characterClassConfirmation = input("You have chosen Archer. Are you sure?\n")
        if characterClassConfirmation == "Yes" or characterClassConfirmation == "y":
            print("Class confirmed.")
            gameInterface()
        else:
            makeCharacterMenu()

    if characterClass == "Mage":
        characterClassConfirmation = input("You have chosen Mage. Are you sure?\n")
        if characterClassConfirmation == "Yes" or characterClassConfirmation == "y":
            print("Class confirmed.")
            gameInterface()
        else:
            makeCharacterMenu()

def clearTerminal(): 
    if os.name == "nt": #Used if system is windows
        _ = os.system("cls") #Windows-specific
  
    else: 
        _ = os.system("clear") #Mac or linux
  

def saveCharacter():
#    with open(fileName) as saveFile:    
#        saveData = json.load(saveFile)
#        pprint.pprint(saveData)
    with open(fileName, 'w') as saveFile:
        json.dump(saveFile, fileName)

def gameInterface():
    clearTerminal()
    print("Welcome,",characterName,".\n""You have chosen to be a",characterClass,".")
#    nextAction = input("What would you like to do?[Fight/SleepGather/Shop]\n")
#    if nextAction == "Fight":


if os.path.exists(fileName): #Checks if JSON file exists
    print("Your save file,",fileName,"already exists.\nYour game will begin in 2 seconds.")
    time.sleep(2)
    with open(fileName) as saveFile:    
        saveData = json.load(saveFile)
        pprint.pprint(saveData)

else:
    print("A save file",fileName,"does not exist, but has now been created.\n")
    makeSaveFile() #only create a new file if no file exists.

makeCharacterMenu()
