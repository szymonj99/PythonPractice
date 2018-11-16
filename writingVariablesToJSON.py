#!/usr/bin/env python3 //Runs on Python 3

import json
import os

#Declaring Variables

fileName = "writingVariablesToJSON.json"
variableToWrite = "Szymon Janusz"
openFileName = open(fileName,"w+")

#Defining Methods

def doesJSONFileExist(): #checks if the json file exists
    if os.path.exists(fileName): #Checks if JSON file exists
        print(fileName,"already exists.")
    else:
        print(fileName,"does not exist, but has now been created.\n")
        makeTextFile() #only create a new file if no file exists.

def makeTextFile(): #Makes empty text file
#    openFileName #Write permission, creating a file if it doesn't exist
    openFileName.write("""{
        "variableOne" : """ + '"' + variableToWrite + '"' + "," "\n"
        "}")
#    openFileName.close() #closes the file. Possibly makes previous line redundant
#    open(fileName,"a").write("Testing Out Writing Variables To JSON.\n")
#    open(fileName,"a").close()

def writingDataToJSON(): #overwrites data in json
    openFileName.write("""{
        "variableOne" : """ + '"' + variableToWrite + '"' + "," "\n"
        "}")

#with open(fileName, "r") as jsonFile:
#    testJSONData = json.load(jsonFile)
#print(testJSONData)

#        {    "variableOne"  :  variableToWrite, 
#        "variableTwo"   :  "This is a second Variable", 
#        "variableThree"      :  variableToWrite + " wrote this code.",
#        }
#    )

#doesJSONFileExist()
makeTextFile()