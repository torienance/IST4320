# This program encodes inputted information using the ROT13 cipher
# The ROT13 cipher substitutes each character for the character that is 13 places away

def encode(userInputList):

    for x in range(len(userInputList)):
        #get the ASCII value of the character to evaluate and change the value
        asciiValue = ord(userInputList[x])
        
        if asciiValue >= 65 and asciiValue <= 77:
            asciiValue += 13
        elif asciiValue >= 77 and asciiValue <= 90:
            asciiValue -= 13
        elif asciiValue >= 97 and asciiValue <= 109:
            asciiValue += 13
        elif asciiValue >= 109 and asciiValue <= 122:
            asciiValue -= 13
        else:
            asciiValue = asciiValue

        userInputList[x] = (chr(asciiValue))

    encodedOutput = ""
    for x in userInputList:
        encodedOutput += x
    
    print("Here is your input encoded according to ROT13: " + encodedOutput)

print("What do you want to encode?:")

#Get the string of what the user wants encoded and turn it into a list
userInputList = list(input())
encode(userInputList)