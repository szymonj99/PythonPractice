#!/usr/bin/env python3 //Runs on Python 3

def mainMenu():
    playerLevel = input("What's your level?")
    playerRequiredExperience = round(((int(playerLevel)+2) ** 4),-1)
    print(playerRequiredExperience)
    mainMenu()

mainMenu()


#Example experienceRequired:
#Level 1: 80
#Level 2: 260
#Level 3: 620
#Level 4: 1300