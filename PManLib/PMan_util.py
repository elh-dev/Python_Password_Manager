# Global Veriables 
# rot number
rotValue = 3

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

# Encode and decode using y as the string and t as the veraible to decide 1 = encrypt or else = decrypt 
def cipher(y, t, debug):
    try:
        #ecrypt
        if t == 1:
            rotValuePresent = rotValue
        #decrypt
        else: 
            rotValuePresent = -rotValue
    except:
        print("rotValue Error")
    #Assigns characters to list 
    listCipher = stringToList(y)
    
    # Print veriable if debug is on
    debugOption(listCipher, debug)

    #Retrives length of list assigned to x 
    listLen = len(listCipher)
    #Iterates over each letter in list and changes it using rot3 
    try:
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
    except Exception as e:
        print(f"An Error occured: {e}")
    else:
        return string

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


# Deciphers entire text document in to memory 
def textDecipher(debug):
    try:
        lines = textToMemory(debug)
    except:
        print("textToMemory Error")
    else:
        try:
            listLen = len(lines)
            for i in range(listLen):
                lines[i] = cipher(lines[i], 0, debug)
                # Print veriable if debug is on
                debugOption(lines[i], debug)
            # Print veriable if debug is on
            debugOption(lines, debug)
        except Exception as e:
            print(f"An Error occured: {e}")
        else:
            return lines 
