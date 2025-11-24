# Global Veriables 
# rot number
rot_value = 3

def debug_option(x, debug):
    if debug == 1:
        print(x)

# Functions for list manipulations

# String to List 
def string_to_list(s):
    l = list(s)
    return l
# List to String
def list_to_string(l):
    lts = "".join(l)
    return lts

# Cipher Fucntions
def cipher_character(list_cipher, i, direction, debug):
    #transaltes charcater to number and Assigns to veriable 
    number_value = ord(list_cipher[i])
    # Print veriable if debug is on
    debug_option(number_value, debug)
    #Assigns rot3 encoded value to veriable 
    number_value_new = number_value + direction
    # Print veriable if debug is on
    debug_option(number_value_new, debug)
    #Translates encoded number to character and Assigns to veriable 
    string_value = chr(number_value_new)
    list_cipher[i] = string_value
    return list_cipher

# Encode and decode using y as the string and t as the veraible to decide 1 = encrypt or else = decrypt 
def cipher_list(y, t, rot_value, debug):
    #ecrypt

    value = rot_value
    if t == 1:
        direction = value
    #decrypt
    else: 
        direction = -value
    
    #Assigns characters to list 
    list_cipher = string_to_list(y)
    # Print veriable if debug is on
    debug_option(list_cipher, debug)

    #Iterates over each letter in list and changes it using rot3 
    try:
        for i in range(len(list_cipher)):
            list_cipher = cipher_character(list_cipher, i, direction, debug)
        # Print veriable if debug is on
        debug_option(list_cipher, debug)

        string = list_to_string(list_cipher)
    except Exception as e:
        print(f"An Error occured: {e}")
    else:
        return string
    
# Read text to memory 
def text_to_memory(debug):
    try:
        with open('text.txt', 'r') as file:
            try:
                line = file.readlines()
            except: 
                print("file.redlines error")
    except Exception as e:
        print(f"An Error occured: {e}")

    # Print veriable if debug is on
    debug_option(line, debug)

    return line
    
# Deciphers entire text document in to memory 
def text_decipher(debug):
    try:
        lines = text_to_memory(debug)
    except:
        print("textToMemory Error")
    else:
        try:
            list_len = len(lines)
            for i in range(list_len):
                lines[i] = cipher_list(lines[i], 0, rot_value, debug)
                # Print veriable if debug is on
                debug_option(lines[i], debug)
            # Print veriable if debug is on
            debug_option(lines, debug)
        except Exception as e:
            print(f"An Error occured: {e}")
        else:
            return lines 