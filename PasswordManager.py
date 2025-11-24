from PManLib import PMan_util

# Global Veriables 
# rot number
rot_value = 3
debug = 0

def debug_option(x, debug):
    if debug == 1:
        print(x)

# Adds string to text document
def write_to_text(y, debug):
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
    debug_option("Text appended", debug)

# Overwrites string to text document 
def overwrite_string_to_text(y,debug):
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
    debug_option("Text Overwriten", debug)

# Overwrites lines to text document 
def overwrite_lines_to_text(y,debug):
    try:
        with open('text.txt', 'w') as file:
            try:
                file.writelines(y)
            except:
                print("file.write error")
    except Exception as e: 
        print(f"An Error occured: {e}")
    # Print veriable if debug is on
    debug_option("Text Overwriten", debug)

# Erase text document content 
def erase_text():
    try:
        with open('text.txt', 'w') as file:
            try:
                pass
            except:
                print("pass error")
    except Exception as e: 
        print(f"An Error occured: {e}")  

# Edit line of text document 
def text_editer(x, text, debug):
    try:
        # Assigns .txt content to a list of lines
        lines = PMan_util.text_to_memory(debug)
        # Print veriable if debug is on
        debug_option(lines,debug)

        # Replaces desired line with text veriab;e 
        lines[x-1] = text + '\n'
        overwrite_lines_to_text(lines, debug)
    except Exception as e:
        print(f"An Error occured: {e}") 

# ROT cipher from string 
def string_to_rot(string, debug):
    try:
        # Assigns encrypted string to veriable 
        y = PMan_util.cipher_list(string, 1, rot_value, debug)
        # Adds encrypted string to .txt
        write_to_text(y, debug)
        # Print veriable if debug is on
        debug_option(y, debug)
    except Exception as e:
        print(f"An Error occured: {e}")
    
# Prints name and password with indicators
def print_text(text):
    count = 1
    try:
        list_len = len(text)
    except: 
        print("len() error occured") 
    else:
        # loop to add specification
        for i in range(list_len):
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

def input_confirm(x):
    confirm = 0
    while confirm == 0:
        print("-----------------------")
        print(x)
        print("-----------------------")
        try:
            credential = input()
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
                confirm = 1
                return credential

def input_cipher(x, debug):
    credential = input_confirm(x)
    string_to_rot(credential, debug)

# Edit specific line of text  
def edit(debug):
    print("-----------------------")
    print("   Edit Login Details")
    print("-----------------------")
    try:
        # Lines that needs to be edited
        line_int = int(input_confirm("Enter Line to edit")) 
    except:
        print("int() error")
        print("-----------------------")
    else:
        try:
            new_text = input_confirm("Enter new string")
        except:
            print("input error")
            print("-----------------------")
        else: 
            ciphered_text = PMan_util.cipher_list(new_text, 1, 
                                                  rot_value, debug)
            text_editer(line_int, ciphered_text, debug)
        
# Version 2 options
def secret_menu(debug):
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
        secret_menu = input()
        print("-----------------------")
    except:
        print("input error")
        print("-----------------------")
    else:
        match secret_menu:
            case "1":
                edit(debug)
            case "2":
                    erase_text()
            case _:
                print("Invalid Option")

# Options 
def option_menu(exit, debug):
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
        option_menu = input()
        print("-----------------------")
    except:
        print("input error")
        print("-----------------------")
    else:
        match option_menu:
            case "1":
                store_cred_loop(debug)
            case "2":
                view_cred(debug)
            case "0":
                exit = True
            case "000":
                secret_menu(debug)
            case _:
                print("Invalid Option try 0, 1, or 2")
        return exit

# View Credentials
def view_cred(debug):
    print("-----------------------")
    print("    Login Details")
    print("-----------------------")
    try:
        text = PMan_util.text_decipher(debug)
    except: 
        print("text_decipher error")
    else:
        print_text(text)

# Store Credentials
def store_cred_loop(debug):
    try:
        try:
            input_cipher("Enter Username", debug)
        except:
            print("storeCred error")
        else:
            try: 
                input_cipher("Enter Password", debug)
            except:
                print("storeCred error")
            else:
                try:
                    input_cipher("Enter URL", debug)
                except:
                    print("storeCred error")
    except Exception as e:
        print(f"An Error occured: {e}")




# Main
exit = False
try:
    while exit != True:
        exit = option_menu(exit, debug)
except Exception as e:
    print(f"An Error occured: {e}")