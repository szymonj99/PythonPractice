#!/usr/bin/env python3 //Runs on Python 3

import json
import os
import pprint
import random
import time
import math
from colorama import Fore, Back, Style

fileName = "saveFile.json"
errorMessage = "Error. Unknown or unexpected input."
characterName = "startOfGamePlaceholderName" #global variable, not used correctly. Later function only changes value for local variable in function.
characterClass = "startOfGamePlaceholderClass"
confirmationYesInput = ("Yes", "yes", "Y", "y")
confirmationNoInput = ("No", "no", "N", "n")
confirmationWarriorInput = ("Warrior", "warrior")
confirmationArcherInput = ("Archer", "archer")
confirmationMageInput = ("Mage", "mage")
fight = ("fight", "Fight", "f", "F")
sleep = ("sleep", "Sleep", "S", "s")
flee = ("Flee", "flee")
attack = ("a", "A", "Attack", "attack", "att", "Att")
info = ("i", "I", "Info", "info")
invalidClassInput = "You can only pick to be a Warrior, Archer, or Mage, Try again."
playerDecidedToFightMessage = "You encountered an enemy!"
playerDecidedToSleepMessage = "You have decided to rest, and recover your health..."
playerDecidedToFleeMessage = "You flee! Coward!"
playerDecidedToAttackMessage = "You gather your strength, and are ready to strike!"
playerDecidedToSaveMessage = "Do you wish to save your progress?"
playerDecidedToLoadMessage = "Do you wish to load your progress?"
victoryMessage = "You won!"
#nextMoveMessage = "What is your next move?"
#fightBeginMessage = "You are fighting!"
#fightWinMessage = "You won!"
#fightLossMessage = "You lost..."
playerLevel = 15 #Used for debugging
playerStrength = 15
playerHealth = playerLevel + round(playerStrength/2)
playerDamageMultiplier = 1.125 + playerLevel/100
playerDamageLowerRange = playerStrength + 5
playerDamageUpperRange = (playerStrength + 5) * playerDamageMultiplier
playerHitChance = 90 #%
playerCurrentExperience = 0 #Should set up an XP table, or think of a formula.
playerRequiredExperience = round((playerLevel+5) ** 2)#The total Experience points the player needs to level up.
playerGold = 0 #Sample currency, Proof Of Concept.
playerInFight = False
playerDidHit = False
playerDidMiss = False

def makeSaveFile(): #Define function
    open(fileName,"w+") #Write permission, creating a file if it doesn't exist
    open(fileName,"w+").close() #closes the file. Possibly makes previous line redundant

def makeCharacterMenu():
    global characterName, characterClass
    characterName = input("What would you like to be called?\n")
    pickCharacterClass()

def playerPickedWarrior():
    characterClassConfirmation = input("You have chosen Warrior. Are you sure? [Yes/Y/No/N]\n")
    if characterClassConfirmation in confirmationYesInput:
        classConfirmation()
        global characterClass
        characterClass = "Warrior"
        gameInterface()
    else:
        makeCharacterMenu()

def playerPickedArcher():
    characterClassConfirmation = input("You have chosen Archer. Are you sure?\n")
    if characterClassConfirmation in confirmationYesInput:
        classConfirmation()
        global characterClass
        characterClass = "Archer"
        gameInterface()
    else:
        makeCharacterMenu()

def playerPickedMage():
    characterClassConfirmation = input("You have chosen Mage. Are you sure?\n")
    if characterClassConfirmation in confirmationYesInput:
        classConfirmation()
        global characterClass
        characterClass = "Mage"
        gameInterface()
    else:
        makeCharacterMenu()

def classConfirmation():
        print("Class confirmed.")
        time.sleep(1)

def pickCharacterClass():
    global invalidClassInput
    characterClass = input("What class would you like to be? [Warrior/Archer/Mage]\n")
    if characterClass in confirmationWarriorInput:
        playerPickedWarrior()           
    elif characterClass in confirmationArcherInput:
        playerPickedArcher()        
    elif characterClass in confirmationMageInput:
        playerPickedMage()
    else:
        print(invalidClassInput)
        pickCharacterClass()

def playerNextAction():
    global playerInFight
    playerInFight = False
    nextAction = input("What would you like to do now? [" + Fore.BLUE + "Sleep" + Fore.WHITE + "/" + Fore.RED + "Fight" + Fore.WHITE + "/" + Fore.YELLOW + "Flee" + Fore.WHITE + "/" + Fore.GREEN + "Info" + Fore.WHITE + "]\n")
    if nextAction in fight:
        playerPickedFight()
    elif nextAction in sleep:
        playerPickedSleep()
    elif nextAction in flee:
        playerPickedFlee()
    elif nextAction in info:
        playerPickedInfo()
    else:
        print(errorMessage)
        playerNextAction()

def playerPickedFight():
    print(playerDecidedToFightMessage+"\n")
    enemyStatsGenerator()

def didPlayerHit():
    global playerHitChance, playerDidHit, playerDidMiss
    if (playerHitChance >= random.randint(0,100)):
        playerDidHit = True
    else:
        playerDidMiss = True

def playerPickedSleep():
    global playerHealth
    print(playerDecidedToSleepMessage)
    playerHealth = playerLevel + round(playerStrength/2)
    playerNextAction()

def playerLosingGold():
    global playerRequiredExperience, goldPlayerLoses, playerGold
    goldPlayerLoses = round(playerRequiredExperience/5)
    if (goldPlayerLoses >= playerGold):
        playerGold = 0
    else:
        playerGold = playerGold - goldPlayerLoses

def playerPickedFlee(): #This will be used in combat only.
    global playerInFight
    if playerInFight == True:
        playerLosingGold()
        print(playerDecidedToFleeMessage)
        if (goldPlayerLoses >= playerGold):
            print("You lost all your gold!")
        else:
            print("You lost", goldPlayerLoses, "gold!")
        playerNextAction()
    else:
        print("You can only flee when fighting.")
        playerNextAction()

def printPlayerStatistics():
    print(
        "   Name:", characterName,"\n",
        "  Class:", characterClass,"\n",
        "  Level:", playerLevel,"\n",
        "  Strength:", playerStrength,"\n",
        "  Health:", playerHealth,"\n",
        "  Hit Multiplier:", playerDamageMultiplier,"\n",
        "  Experience:", playerCurrentExperience,"\n",
        "  XP To Level Up:", playerRequiredExperience - playerCurrentExperience,"\n",
        "  Gold:", playerGold,"\n",
        "  Hit Chance:", playerHitChance,"\n",
        "  Damage Range:", playerDamageLowerRange, "-", playerDamageUpperRange, "\n",
        "  Avg. Damage:", round((playerDamageLowerRange + playerDamageUpperRange)/2),"\n",
        )

def playerPickedInfo():
    print("Your current player statisctics are:")
    printPlayerStatistics()
    playerNextAction()

def enemyLevelGenerator():
    global playerLevel, enemyLevel
    if (playerLevel == 1): #Adding some level 1-3 enemy variations.
        enemyLevel = random.randint(playerLevel,playerLevel+2) #Enemy level is somewhere within -2 to +5 levels within player. Trouble when player level is 1-3. Need to fix.
    elif (playerLevel == 2):
        enemyLevel = random.randint(playerLevel-1,playerLevel+3)
    elif (playerLevel == 3):
        enemyLevel = random.randint(playerLevel-2,playerLevel+4)
    elif (playerLevel >= 75):
        enemyLevel = 75 #Max. Level for now is 75, else the random number gen for enemyEvasionChance would break.
    else:
        enemyLevel = random.randint(playerLevel-2,playerLevel+5)

def enemyStatsGenerator():
    enemyLevelGenerator()
    global enemyLevel, enemyHealth, enemyDamageReduce, enemyArmour, enemyStrength
    enemyStrength = round(random.uniform(enemyLevel+5,(enemyLevel+5)*1.35)) #
    enemyHealth = enemyLevel + round(enemyStrength/2)
    enemyArmour = round(random.uniform(enemyLevel*3,enemyLevel*7))
    enemyDamageReduce = round(math.sqrt(enemyArmour) + enemyLevel)
    printEnemyStatistics()
    playerFightChoice()

def printEnemyStatistics():
    print(
        "   Enemy Level:", enemyLevel,"\n",
        "  Enemy Strength:", enemyStrength,"\n",
        "  Enemy Health:", enemyHealth,"\n",
        "  Enemy Armour:", enemyArmour,"\n",
        "  Enemy Damage Reduce:", enemyDamageReduce,"\n",
        )

def playerFightChoice():
    global playerInFight
    playerInFight = True
    playerAttackOrFlee = input("What do you wish to do? [Attack/Flee]\n")
    if playerAttackOrFlee in attack:
        playerPickedAttack()
    elif playerAttackOrFlee in flee:
        playerPickedFlee()
    else:
        print(errorMessage)
        playerFightChoice()

def playerPickedAttack():
    global enemyHealth, playerDidHit, playerDidMiss
    print(playerDecidedToAttackMessage)
    time.sleep(1) #Need to further develop this method and fightCalculations()
    didPlayerHit()
    playerDamageGeneratorDuringFight()
    if playerDidHit == True:
        enemyHealth = enemyHealth - playerDamageToDeal
        print("You " + Fore.GREEN + "hit " + Fore.WHITE + "the enemy for", playerDamageToDeal, "damage.")
        if (enemyHealth > 0):
            print("The enemy has" + Fore.GREEN, enemyHealth, Fore.WHITE + "health left.")
    elif playerDidMiss == True:
        print("You missed!")
    enemyAttacksPlayer()

def playerDamageGeneratorDuringFight():
    global playerDamageToDeal
    playerDamageToDeal = round(random.uniform(playerDamageLowerRange,playerDamageUpperRange))

def enemyAttacksPlayer():
    global enemyHealth, playerGold, enemyLevel, playerCurrentExperience, enemyStrength, playerHealth
    if (enemyHealth > 0):
        print("The enemy strikes back!")
        playerDamageTaken = round(enemyStrength/2)
        playerHealth = playerHealth - playerDamageTaken
        print("You took" + Fore.YELLOW, playerDamageTaken, Fore.WHITE + "damage.")        
        if (playerHealth > 0):
            print("You have" + Fore.GREEN, playerHealth, Fore.WHITE + "health left.")
            playerFightChoice()
        else:
            print(Fore.RED +"You Died..." + Fore.WHITE)
    else:
        playerGold = playerGold + enemyLevel
        playerCurrentExperience = playerCurrentExperience + enemyLevel
        print(Fore.GREEN + victoryMessage,"\nYou have gained",enemyLevel,"gold and experience." + Fore.WHITE)
        playerNextAction()

def clearTerminal():  #Not my piece of code
    if os.name == "nt": #Used if system is windows
        _ = os.system("cls") #Windows-specific
    else: 
        _ = os.system("clear") #Mac or linux
  
def saveCharacter(): #not functional right now
#    with open(fileName) as saveFile:    
#        saveData = json.load(saveFile)
#        pprint.pprint(saveData)
    with open(fileName, 'w') as saveFile:
        json.dump(saveFile, fileName)

def gameInterface():
    clearTerminal()
    print("Welcome,",characterName,".\n""You have chosen to be a",characterClass,".")
    playerNextAction()
#    nextAction = input("What would you like to do?[Fight/Sleep/Gather/Shop]\n")
#    if nextAction == "Fight":

if os.path.exists(fileName): #Checks if JSON file exists
    print("Your save file,",fileName,"already exists.\nYour game will begin in 2 seconds.")
    time.sleep(2)
#    with open(fileName) as saveFile:     #Prints save data for testing.
#        saveData = json.load(saveFile)
#        pprint.pprint(saveData)

else:
    print("A save file",fileName,"does not exist, but has now been created.\n")
    makeSaveFile() #only create a new file if no file exists.

makeCharacterMenu()