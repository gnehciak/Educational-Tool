import csv
import os

activeUser = ''


def useless():
    print("""
                                                              |                                                                                                                   ░░  
                                                              |                                                                                                                 ░░▓▓██
                                                              |                                                                                  ░░                            ░░▒▒▓▓██
                                                              |                                                                             ░░░░░░░░▒▒                      ░░░░▒▒▓▓░░
                                                              |                                                                         ░░░░░░▒▒░░▒▒▓▓░░░░                ░░▒▒▓▓▒▒    
                                                              |                                                                      ░░▒▒░░▒▒▓▓░░░░░░░░▒▒▓▓░░          ▒▒░░░░▓▓▒▒      
                                                              |                                                                   ░░░░▒▒░░░░░░░░░░░░▓▓▒▒▓▓▓▓▒▒░░    ░░▒▒▓▓▒▒░░        
                                                              |                                                               ░░░░░░░░▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓            
                                                              |                                                             ░░░░░░░░░░░░░░░░▒▒▓▓▓▓██▓▓▓▓▓▓    ░░▒▒▒▒▒▒░░              
                                                              |                                             ░░          ░░░░▒▒░░░░░░▒▒▓▓▒▒▓▓▒▒▒▒▓▓██▓▓▓▓▓▓        ▒▒                  
                                                              |                                         ░░░░▒▒▒▒  ░░░░░░░░▓▓▒▒░░░░░░░░▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒██                            
                      ### LOGIN ###                           |                                         ░░▓▓▓▓░░░░░░░░░░░░  ░░░░░░▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒                            
                                                              |                                     ░░░░░░▒▒░░░░░░▒▒▒▒▓▓░░░░░░▒▒██▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒                            
                      Username                                |                                 ░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓██▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒                            
                      |----------------------|                |                                 ▒▒▒▒░░░░░░░░▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒                              
                      |                      |                |                                 ▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▒▒                              
                      |----------------------|                |                                 ▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓██▓▓▒▒██▓▓▓▓▓▓▒▒▓▓▓▓▒▒                              
                      Password                                |                                 ░░░░░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▒▒                              
                      |----------------------|                |                                 ▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓                              
                      |                      |                |                                 ▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▒▒▓▓░░      ▒▒▒▒▒▒▒▒▓▓▓▓                              
                      |----------------------|                |                                 ░░▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒              ▒▒▒▒▓▓▒▒                              
                                                              |                                     ░░▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  ░░                                  
                                                              |                                                 ░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒                                                      
                                                              |                                                 ░░██▒▒▒▒▒▒▒▒▒▒▓▓                                                      
                                                              |                                                   ▒▒▒▒▓▓▒▒▒▒▒▒▓▓                                                      
                                                              |                                                   ▒▒▒▒▓▓▓▓▒▒▒▒▓▓                                                      
                                                              |                                                     ░░▒▒▒▒▒▒▓▓▓▓                                                      
                                                              |                                                         ░░▒▒▓▓░░                                                      
""")


def clear():
    os.system('CLS')


def logIn():
    print("Welcome to Quizelot")
    print("Please log in with your details to continue.")

    # Keep asking for correct login credential until the correct one is entered.
    while True:
        # Ask for username
        ipt_Username = input("Username: ")
        # Open the login.csv file to check if username instance exists
        with open('login.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            # Attempt to find username line by line
            for row in reader:
                # Make sure that the row has a value
                if row:
                    if ipt_Username == row[0]:
                        user_found = True
                        break
                else:
                    user_found = False
            # If found, ask for password.
            if user_found:
                ipt_Password = input("Password: ")
                # If password is correct, return True.
                if ipt_Password == row[1]:
                    print("Login Successful!")
                    input("Press Enter to continue...")
                    return True
                # Else loop back and try again.
                else:
                    print("Incorrect password, please try again.")
                    continue
            # If username not found, give options to retry or register.
            else:
                print("Account not found.")
                print("[1] Retry")
                print("[2] Register")
                if int(input()) == 2:
                    clear()
                    register()


def register():
    print("Register your account")
    ipt_Username = input("Username: ")
    ipt_Password = input("Password: ")
    with open('login.csv', 'a') as f:
        f.write(ipt_Username + ',' +ipt_Password)


def mainMenu():
    print("Welcome!")
    return 0


if logIn():
    clear()
    mainMenu()
