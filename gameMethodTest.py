def methodOne():
    print("This is method one.")
    methodTwo()

def methodTwo():
    print("This is method two.")

methodOne()

#Quick test. Prints out two sentences as it should

def methodThree():
    global fileName
    fileName = "testFile.json"

methodThree()

def methodFour():
    print(fileName)

methodFour()