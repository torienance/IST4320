# This program creates a one time use pad by generating random numbers
# and shifting the characters by that many characters

import random

def userChoice():
    print("Would you like to encrypt or decrypt a message?:")
    print("Type 1 for encryption or 2 for decryption")
    choice = int(input())

    if choice == 1:
        preEncrypt()
    elif choice == 2:
        preDecrypt()
    else:
        print("Invalid input given. The program has been terminated.")

def preEncrypt():
    
    print("What do you want to encrypt?:")

    #get the string of what the user wants encrypted and turn it into a list
    userInputList = list(input())
    privateKey = encrypt(userInputList)

    print("Would you like to view the private key? Y/N:")

    answer = input()
    if answer == "Y":
        print("What is the password?:")
        password = input()

        if password == "NopeWasRobbedAtTheOSCARS":
            print("The private key is: " + privateKey)
        else:
            print("Access Denied!")
    else:
        print("Have a great day!")

def encrypt(userInputList):
    
    privateKey = []

    for x in range(len(userInputList)):
            privateKey.append(0)

    for x in range(len(userInputList)):

        #get the ASCII value of the character to make sure it's a letter
        asciiValue = ord(userInputList[x])

        #if the value of the character is a letter, then run the functions
        if (asciiValue >= 65 and asciiValue <= 90) or (asciiValue >= 97 and asciiValue <= 122):
            isLowerRange = randomRange()
            newAsciiValue = determineRange(isLowerRange)

            #subtract the new value from the original value and store it in the privateKey list so that the value added to the original value is logged for decoding purposes
            privateKey[x] = newAsciiValue - asciiValue 
            #replace the character with the character at the new ASCII value character
            userInputList[x] = (chr(newAsciiValue))
        else:
            privateKey[x] = 0 #if no change (ex. if it's punctuation) set the private key value to 0 since nothing is being added or subtracted to the original ASCII value
            userInputList[x] = (chr(asciiValue))
    
    encryptedOutput = ""
    for x in userInputList:
        encryptedOutput += x
    
    print("Encrypted message: " + encryptedOutput)

    #turn the private key list into a string list
    keyListToString = map(str, privateKey)
    
    #turn the list into a basic string to be returned and outputted for the user
    stringPrivateKey = ""
    for x in keyListToString:
        stringPrivateKey += (x + " ")
    
    return stringPrivateKey

#determine whether to use the upper or lower range
def randomRange():
   
    isLowerRange = False

    if random.randint(0,9) < 5:
        isLowerRange = True
    elif random.randint(0,9) >= 5:
        isLowerRange = False

    return isLowerRange

def determineRange(isLowerRange):
    
    #if isLowerRange is true then that means use the range from 65 to 90
    if isLowerRange:
        newAsciiValue = random.randint(65,90)
    #if isLowerRange is false then that means use the range from 97 to 122
    elif not isLowerRange:
        newAsciiValue = random.randint(97,122)


    return newAsciiValue

def preDecrypt():

    print("What do you want to decrypt?:")
   
    #get the string of what the user wants decrypted and turn it into a list
    userInputList = list(input())

    print("Do you have the private key assocaited with this? Y/N:")
    answer = input()

    if answer == "Y":
        decrypt(userInputList)
    else:
        print("The information cannot be decrypted without the key.")

def decrypt(userInputList):

    privateKey = []
    
    #initialize the privateKey list according to the amount of items in the userInputList
    for x in range(len(userInputList)):
        privateKey.append(0)

    #take user input as to what the entire key is so it can be reversed
    print("Please enter all of the values in the private key separated by spaces.")
    userInput = input()
    userList = userInput.split()

    for x in range(len(userList)):
        privateKey[x] = int(userList[x])

    #turn the private key list into a string list
    keyListToString = map(str, privateKey)

    #turn the list into a basic string to be returned and outputted for the user
    stringPrivateKey = ""
    for x in keyListToString:
        stringPrivateKey += (x + " ")

    print("Now decrypting using the private key of " + stringPrivateKey)

    asciiValue = 0
    #for each letter get the asciiValue and subtract by the privateKey value
    for x in range(len(userInputList)):
        asciiValue = ord(userInputList[x])
        
        # if the privateKey value is not 0 (meaning not a punctuation mark or spaces) continue
        if privateKey[x] != 0: 
            newAsciiValue = asciiValue - privateKey[x]
            userInputList[x] = (chr(newAsciiValue))
        else:
            userInputList[x] = userInputList[x]

    encryptedOutput = ""
    for x in userInputList:
        encryptedOutput += x
    
    print("Decrypted message: " + encryptedOutput)
    
#start of the program
userChoice()