from modules.miscellaneous import *

def logIn():
    print("Welcome to Quizelot")
    print("Please log in with your details to continue.")

    # Keep asking for correct login credential until the correct one is entered.
    while True:
        # Ask for username
        ipt_Username = input("Username: ")
        # Open the login.csv file to check if username instance exists
        with open('data/csv/login.csv', 'r') as f:
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
    with open('data/csv/login.csv', 'a') as f:
        f.writelines('\n' + ipt_Username + ',' + ipt_Password)
    with open('data/csv/user_data.csv', 'a') as f:
        f.writelines('\n' + ipt_Username + ',' + '0' + ',' + '0' + ',' + '0')
    print("Registration Successful, press Enter to Login...")
    input()
    clear()
