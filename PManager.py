from PManLib import PMan_util
# Debug option 1 for on 
debug = 0

def debugOption(x, debug):
    if debug == 1:
        print(x)



# Functions for .txt manipulation

# Adds string to text document
def writeToText(y, debug):
    try:
        with open('text.txt', 'a') as file:
            try:
                file.write(y 
                           + '\n')
            except:
                print("file.write error")
    except Exception as e: 
        print(f"An Error occured: {e}")

    # Print veriable if debug is on
    debugOption("Text appended", debug)

# Overwrites string to text document 
def overwriteToText(y,debug):
    try:
        with open('text.txt', 'w') as file:
            try:
                file.write(y 
                           + '\n')
            except:
                print("file.write error")
    except Exception as e: 
        print(f"An Error occured: {e}")

    # Print veriable if debug is on
    debugOption("Text appended", debug)

# Erase text document content 
def eraseText():
    try:
        with open('text.txt', 'w') as file:
            try:
                pass
            except:
                print("pass error")
    except Exception as e: 
        print(f"An Error occured: {e}")  

# Read text to memory 
def textToMemory(debug):
    try:
        with open('text.txt', 'r') as file:
            try:
                line = file.readlines()
            except: 
                print("file.redlines error")
    except Exception as e:
        print(f"An Error occured: {e}")

    # Print veriable if debug is on
    debugOption(line, debug)

    return line
# Un-used feature for future implimentation
def textEditer(x, text, debug):
    try:
        with open('text.txt', 'r') as file:
             line = file.readlines()
    
        # Print veriable if debug is on
        debugOption(line,debug)

        line[x-1] = text + '\n'
        with open('text.txt', 'w') as file:
             file.writelines(line) 
    except Exception as e:
        print(f"An Error occured: {e}") 

# Functions for Security
# ROT cipher from string 
def stringToRot(string, debug):
    try:
        # Assigns encrypted string to veriable 
        y = PMan_util.cipher(string, 1, debug)
        # Adds encrypted string to .txt
        writeToText(y, debug)
        # Print veriable if debug is on
        debugOption(y, debug)
    except Exception as e:
        print(f"An Error occured: {e}")
    

# Prints credentials with labels
def printText(text):
    count = 1
    try:
        listLen = len(text)
    except: 
        print("len() error occured") 
    else:
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

def storeCred(x,confirm, debug):
    print(x)
    try:
        password = input()
    except: 
        print("input error")
    else:
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
    try:
        confirm = 0
        try:
            while confirm == 0:
                confirm = storeCred("Enter Username", confirm, debug)
        except:
            print("storeCred error")
        else:
            confirm = 0
            try: 
                while confirm == 0:
                    confirm = storeCred("Enter Password", confirm, debug)
            except:
                print("storeCred error")
            else:
                confirm = 0
                try:
                    while confirm == 0:
                        confirm = storeCred("Enter URL", confirm, debug)
                except:
                    print("storeCred error")
    except Exception as e:
        print(f"An Error occured: {e}")
# View Credentials
def viewCred(debug):
    print("-----------------------")
    print("    Login Details")
    print("-----------------------")
    try:
        text1 = PMan_util.textDecipher(debug)
    except: 
        print("textDecipher error")
    else:
        printText(text1)

def edit(debug):
    print("-----------0-----------")
    print("-----------0-----------")
    print("-----------0-----------")
    try:
        option = 1
        while option == 1:
            print("Enter Line to edit")
            print("-----------------------")
            lineToEdit = input()
            print("-----------------------")
            try: 
                lineInt = int(lineToEdit)
            except:
                print("line to int error")
            else:
                option = 0
            finally:
                option 
    except:
        print("input error")
        print("-----------------------")
    else:    
            print("Enter new text")
            print("-----------------------")
            try:
                newtext = input()
            except:
                print("input error")
            print("-----------------------")
            cipheredText = PMan_util.cipher(newtext, 1,debug )
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
    try:
        secretMenu = input()
        print("-----------------------")
    except:
        print("input error")
        print("-----------------------")
    else:
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
    try: 
        optionMenu = input()
        print("-----------------------")
    except:
        print("input error")
        print("-----------------------")
    else:
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
try:
    while exit != True:
        exit = optionMenu(exit, debug)
except Exception as e:
    print(f"An Error occured: {e}")


