#!/usr/bin/env python3 //Runs on Python 3

import json

def makeTextFile(): #Define function
    open("testFile.txt","w+") #Write permission, creating a file if it doesn't exist
    open("testFile.txt","w+").close() #closes the file
    
makeTextFile()