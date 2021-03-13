import csv
import os
import time
import textwrap
import random

from algebra import *
import shared





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


# Miscellaneous



def sleep(t):
    time.sleep(t)


# Initialisation
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
                    shared.activeUser = ipt_Username
                    print("Login Successful!")
                    pause()
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
    # Ask for new username and password.
    print("Register your account")
    ipt_Username = input("Username: ")
    ipt_Password = input("Password: ")
    # Register the input into the login.csv file.
    with open('login.csv', 'a') as f:
        f.writelines('\n' + ipt_Username + ',' + ipt_Password)
    with open('user_data.csv', 'a') as f:
        f.writelines('\n' + ipt_Username + ',' + '0' + ',' + '0' + ',' + '0')
    print("Registration Successful, press Enter to Login...")
    input()
    clear()


def mainMenu():
    print("Welcome!")
    print("Choose a course below:")
    print("""
┌───┐  ┌─┐┬  ┌─┐┌─┐┌┐ ┬─┐┌─┐
│ 1 │  ├─┤│  │ ┬├┤ ├┴┐├┬┘├─┤
└───┘  ┴ ┴┴─┘└─┘└─┘└─┘┴└─┴ ┴                    
    """)
    print("""
┌───┐  ┌─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐┬─┐┬ ┬
│ 2 │  │ ┬├┤ │ ││││├┤  │ ├┬┘└┬┘
└───┘  └─┘└─┘└─┘┴ ┴└─┘ ┴ ┴└─ ┴ 
    """)
    print("""
┌───┐  ┌┬┐┬─┐┬┌─┐┌─┐┌┐┌┌─┐┌┬┐┬ ┬┌┬┐┬─┐┬ ┬
│ 3 │   │ ├┬┘││ ┬│ │││││ ││││└┬┘ │ ├┬┘└┬┘
└───┘   ┴ ┴└─┴└─┘└─┘┘└┘└─┘┴ ┴ ┴  ┴ ┴└─ ┴ 
    """)

    print("Enter 0 to sign out.")

    while True:
        try:
            selection = int(input("Select a Topic to Begin!\n---> "))
            if selection in range(0, 4):
                break
            else:
                print("Please enter a value between 0-3.")
        except ValueError:
            print("Please enter a valid selection.")

    if selection == 1:
        return 1
    elif selection == 0:
        return 0


# Algebra


# Geometry
def geometry():
    return 0


# Trigonometry
def trigonometry():
    return 0

while logIn():
    clear()
    while True:
        subject = mainMenu()
        clear()
        if subject == 0:
            break
        elif subject == 1:
            while True:
                select = algebra()
                clear()
                if select == 1:
                    algebra_Learn()
                elif select == 2:
                    print(shared.currentSubject)
                    algebra_Levels()
                elif select == 3:
                    break
                clear()
        elif subject == 2:
            select = geometry()
        elif subject == 3:
            select = trigonometry()

"""
currentSubject = 1
activeUser = "Kevin"
algebra_Levels()
    
shared.currentSubject = 1
shared.activeUser = "Kevin"
print(check_level(1,1))

algebra_Levels_Questions(3, 3)
    
algebra()



"""
