# Global Veriables 
# rot number
rotValue = 3
# Debug option 1 for on 
debug = 0
def debugOption(x,debug):
    if debug == 1:
        print(x)

# Functions for list manipulations

# String to List 
def stringToList(s):
    l = list(s)
    return l
# List to String
def listToString(l):
    lts = "".join(l)
    return lts


# Functions for .txt manipulation

# Adds string to text document
def writeToText(y,debug):
    with open('text.txt', 'a') as file:
        file.write(y + '\n')

    #debugOption("Text appended",debug)
# Overwrites string to text document 
def overwriteToText(y,debug):
    with open('text.txt', 'w') as file:
        file.write(y + '\n') 

    debugOption("Text appended",debug)
# Read text to memory 
def textToMemory(debug):
    with open('text.txt', 'r') as file:
        line = file.readlines()
    debugOption(line,debug)
    return line
# Un-used feature for future implimentation
def textEditer(x,text):
    with open('text.txt', 'r') as file:
        line = file.readlines()
    print(line)
    line[x-1] = text + '\n'
    with open('text.txt', 'w') as file:
        file.writelines(line) 

# Functions for Security
 
# Encode and decode using y as the string and t as the veraible to decide 1 = encrypt or else = decrypt 
def cipher(y,t):

    
    #ecrypty
    if t == 1:
        rotValuePresent = rotValue
    #decrypt
    else: 
        rotValuePresent = -rotValue
    #Assigns characters to list 
    listCipher = stringToList(y)
    
    #prints list
    debugOption(listCipher,debug)

    #Retrives length of list assigned to x 
    listLen = len(listCipher)
    #Iterates over each letter in list and changes it using rot3 
    for i in range(listLen):
        #transaltes charcater to number and Assigns to veriable 
        numberValue = ord(listCipher[i])

        debugOption(numberValue,debug)
        #Assigns rot3 encoded value to veriable 
        numberValueNew = numberValue + rotValuePresent

        debugOption(numberValueNew,debug)
        #Translates encoded number to character and Assigns to veriable 
        stringValue = chr(numberValueNew)
        listCipher[i] = stringValue
    #prints encoded list 
    debugOption(listCipher,debug)
    string = listToString(listCipher)
    return string
# 
def stringToRot(string,debug):
    if debug == 1:
        choice = 1
    else:
        print("Enter 1 to encrypt else decrypt")
        choice = input()
    # Assigns encrypted string to veriable 
    y = cipher(string,int(choice))
    # Adds encrypted string to .txt
    writeToText(y,debug)
    
    #debugOption(y,debug)
# Deciphers entire text document in to memory 
def textDecipher(debug):
    lines = textToMemory(debug)
    listLen = len(lines)
    for i in range(listLen):
        lines[i] = cipher(lines[i],0)
        debugOption(lines[i],debug)
    debugOption(lines,debug)
    return lines 
# Prints name and password with indicators
def printText(text):
    listLen = len(text)
    count = 1
    # loop to add specification
    for i in range(listLen):
        if count == 1:
            print("---------")
            print("UserName: ",text[i])
        
        if count == 2:
            print("Password: ",text[i])

        if count == 3:
            print("URL     : ",text[i])
            count =0
            print("---------")
        count += 1


# Funtions fore Option Menu

# Store Credentials
def storeCred():
    confirm = 0
    while confirm == 0:
        print("Enter UserName")
        password = input()
        print("-----------------------")
        print("Enter 1 to Confirm")
        print("Enter 0 to Retry")
        option = input()
        print("-----------------------")
        if option == "1":
            
            stringToRot(password, 1)
            confirm = 1
    
    confirm2 = 0
    while confirm2 == 0:
        
        print("Enter Password") 
        key = input()
        print("-----------------------")
        print("  Enter 1 to Confirm")
        print("  Enter 0 to Retry")
    
        option2 = input()
        print("-----------------------")
        if option2 == "1":
            stringToRot(key, 1)
            confirm2 = 1 

    confirm3 = 0
    while confirm3 == 0:
        
        print("Enter URL/resource") 
        url = input()
        print("-----------------------")
        print("  Enter 1 to Confirm")
        print("  Enter 0 to Retry")
        option3 = input()
        print("-----------------------")
        if option3 == "1":
            stringToRot(url, 1)
            confirm3 = 1 

# View Credentials
def viewCred(debug):
    print("-----------------------")
    print("    Login Details")
    print("-----------------------")
    text1 = textDecipher(debug)
    printText(text1)

def edit():
    print("Enter Line to edit")
    lineToEdit = input()
    lineInt = int(lineToEdit)
    print("Enter new text")
    newtext = input()
    cipheredText = cipher(newtext,1)
    textEditer(lineInt,cipheredText)

def secretMenu():
    print("_______________________")
    print()
    print("     Secret Menu")
    print("_______________________")
    print("-----------------------")
    print("1: edit Log In Details")
    print("0:        Exit")
    print("-----------------------")
    secretMenu = input()
    print("-----------------------")
    match secretMenu:
        case "1":
            edit()
        case _:
            print("Invalid Option")

# Option Menu
def optionMenu(exit,debug):
    print("_______________________")
    print()
    print(" ELV Password Manager")
    print("_______________________")
    print("-----------------------")
    print("1: Store Log In Details")
    print("2: View Log In Details")
    print("0:        Exit")
    print("-----------------------")
    optionMenu = input()
    print("-----------------------")
    match optionMenu:
        case "1":
            storeCred()
        case "2":
            viewCred(debug)
        case "0":
            exit = True
        case "000":
            secretMenu()
        case _:
            print("Invalid Option try 0, 1, or 2")
    return exit
    


    
# Main
exit = False
while exit != True:
    exit = optionMenu(exit,debug)






