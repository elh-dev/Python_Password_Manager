# Global Veriables 
# rot number
rotValue = 3
# Debug option 1 for on 
debug = 0
def debugOption(x, debug):
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
def writeToText(y, debug):
    with open('text.txt', 'a') as file:
         file.write(y 
                    + '\n')
    # Print veriable if debug is on
    debugOption("Text appended", debug)
# Overwrites string to text document 
def overwriteToText(y,debug):
    with open('text.txt', 'w') as file:
         file.write(y 
                    + '\n') 
    # Print veriable if debug is on
    debugOption("Text appended", debug)
# Erase text document content 
def eraseText():
    with open('text.txt', 'w') as file:
         pass
# Read text to memory 
def textToMemory(debug):
    with open('text.txt', 'r') as file:
         line = file.readlines()
    # Print veriable if debug is on
    debugOption(line, debug)

    return line
# Un-used feature for future implimentation
def textEditer(x, text, debug):
    with open('text.txt', 'r') as file:
         line = file.readlines()
    # Print veriable if debug is on
    debugOption(line,debug)

    line[x-1] = text + '\n'
    with open('text.txt', 'w') as file:
         file.writelines(line) 

# Functions for Security
 
# Encode and decode using y as the string and t as the veraible to decide 1 = encrypt or else = decrypt 
def cipher(y, t, debug):
    #ecrypt
    if t == 1:
        rotValuePresent = rotValue
    #decrypt
    else: 
        rotValuePresent = -rotValue
    #Assigns characters to list 
    listCipher = stringToList(y)
    
    # Print veriable if debug is on
    debugOption(listCipher, debug)

    #Retrives length of list assigned to x 
    listLen = len(listCipher)
    #Iterates over each letter in list and changes it using rot3 
    for i in range(listLen):
        #transaltes charcater to number and Assigns to veriable 
        numberValue = ord(listCipher[i])
        # Print veriable if debug is on
        debugOption(numberValue, debug)
        #Assigns rot3 encoded value to veriable 
        numberValueNew = numberValue + rotValuePresent
        # Print veriable if debug is on
        debugOption(numberValueNew, debug)
        #Translates encoded number to character and Assigns to veriable 
        stringValue = chr(numberValueNew)
        listCipher[i] = stringValue
    # Print veriable if debug is on
    debugOption(listCipher, debug)
    string = listToString(listCipher)
    return string

# Proglem here with debug +++++++++++++++++++++++++++++++++++ 
def stringToRot(string, debug):
    # Assigns encrypted string to veriable 
    y = cipher(string, 1, 0)# fix debug
    # Adds encrypted string to .txt
    writeToText(y, 0)
    # Print veriable if debug is on
    debugOption(y, 0)# fix debug
# Deciphers entire text document in to memory 
def textDecipher(debug):
    lines = textToMemory(debug)
    listLen = len(lines)
    for i in range(listLen):
        lines[i] = cipher(lines[i], 0, debug)
        # Print veriable if debug is on
        debugOption(lines[i], debug)
    # Print veriable if debug is on
    debugOption(lines, debug)

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

#
def storeCred(x,confirm, debug):
    print(x)
    password = input()
    print("-----------------------")
    print("Enter 1 to Confirm")
    print("Enter 0 to Retry")
    print("-----------------------")
    option = input()
    print("-----------------------")

    if option == "1":
        stringToRot(password, debug)
        confirm = 1
    return confirm


# Store Credentials
def storeCredLoop(debug):
    confirm = 0
    while confirm == 0:
        confirm = storeCred("Enter Username", confirm, debug)
    
    confirm = 0
    while confirm == 0:
        confirm = storeCred("Enter Password", confirm, debug)

    confirm = 0
    while confirm == 0:
        confirm = storeCred("Enter URL", confirm, debug)

# View Credentials
def viewCred(debug):
    print("-----------------------")
    print("    Login Details")
    print("-----------------------")
    text1 = textDecipher(debug)
    printText(text1)

def edit(debug):
    print("-----------0-----------")
    print("-----------0-----------")
    print("-----------0-----------")
    
    print("Enter Line to edit")
    print("-----------------------")
    lineToEdit = input()
    print("-----------------------")
        
    lineInt = int(lineToEdit)
    print("Enter new text")
    print("-----------------------")
    newtext = input()
    print("-----------------------")
    cipheredText = cipher(newtext, 1,debug )
    textEditer(lineInt, cipheredText, debug)

def secretMenu(debug):
    print("_______________________")
    print()
    print("     Secret Menu")
    print("_______________________")
    print("-----------------------")
    print("1: Edit Log In Details")
    print("2: Erase Text Document")
    print("0:        Exit")
    print("-----------------------")
    secretMenu = input()
    print("-----------------------")
    match secretMenu:
        case "1":
            edit(debug)
        case "2":
            eraseText()
        case _:
            print("Invalid Option")

# Option Menu
def optionMenu(exit, debug):
    print("_______________________")
    print()
    print(" ELH Password Manager")
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
            storeCredLoop(debug)
        case "2":
            viewCred(debug)
        case "0":
            exit = True
        case "000":
            secretMenu(debug)
        case _:
            print("Invalid Option try 0, 1, or 2")
    return exit
    


    
# Main
exit = False
while exit != True:
    exit = optionMenu(exit, debug)


