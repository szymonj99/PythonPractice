#!/usr/bin/env python3 //Runs on Python 3

#What this module will do:
#Open a test JSON file, or create an empty one if it doesn't exit
#Ask the end user for name and surname
#Store this data in the JSON database
#Possible data redundancy check before the new input data is stored
#Need to check amount of lines present in text file, and create a new entry on a new line.
#only allow current session/same data to be saved once

import os
import webbrowser
import json
import time
from colour import Color
import datetime

now = datetime.datetime.now()
fileName = "testJSONFile.json" #Used for testing, referenced later in code
errorMessage = "Cancelling operation." #Convenience to change error code. Used when no correct phrase is entered.
timesFileSaved = 0 #Will be used to only allow user to save once per session.

def makeTextFile(): #Define function
    open(fileName,"w+") #Write permission, creating a file if it doesn't exist
    open(fileName,"a").write("User Log In History\n")
    open(fileName,"w+").close() #closes the file. Possibly makes previous line redundant

if os.path.exists(fileName): #Checks if JSON file exists
    print(fileName,"already exists.")
else:
    print(fileName,"does not exist, but has now been created.\n")
    makeTextFile() #only create a new file if no file exists.

userName = input("What's your name?\n")
userSurname = input("What's your surname?\n")

print("Welcome,",userName,userSurname, "!")

def mainMenuFunc(): #Function used for the main menu.
    mainMenuOptions = input("What do you want to do? You can save, open, or quit.\n")
    if mainMenuOptions == "save":
        storageQuestion = input("Do you want to store this information?\n")
        if storageQuestion == "yes":
#            open(fileName,"w").write(userName) #"w" replaces the whole file. Must change.
            open(fileName,"a").write(userName+" "+userSurname+" "+str(now)+"\n") #Appends the file instead. Writes user name and user surname with new line to make sure records don't overlap.
            print(fileName,"was saved.")
#            timesFileSaved += 1 #Incrementally add 1 to prevent saving more than once. Currently tried to call before variable is set.
            mainMenuFunc() #Referenced to repeat the code
        else:
            print(errorMessage)
            mainMenuFunc()
        
    if mainMenuOptions == "open":
        openQuestion = input("Do you want to open your JSON file?\n")
        if openQuestion == "yes":
            webbrowser.open(fileName)
            print(fileName,"was opened.")
            mainMenuFunc()
        else:
            print(errorMessage)
            mainMenuFunc()
            
    if mainMenuOptions == "quit": #Need to change. Currently hard coded, want to make the quit timer adjustable.
        quitQuestion = input("Do you want to quit?\n")
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