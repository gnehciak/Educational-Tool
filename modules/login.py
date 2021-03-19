from modules.miscellaneous import *


def log_in():
    print("Welcome to Quizelot")
    print("Please log in with your details to continue.")

    # Keep asking for correct login credential until the correct one is entered.
    while True:
        # Ask for username
        ipt_username = input("Username: ")
        # Open the login.csv file to check if username instance exists
        with open('data/csv/login.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            # Attempt to find username line by line
            for row in reader:
                # Make sure that the row has a value
                if row:
                    if ipt_username == row[0]:
                        user_found = True
                        break
                    else:
                        user_found = False
            # If found, ask for password.
            if user_found:
                ipt_password = input("Password: ")
                # If password is correct, return True.
                if ipt_password == row[1]:
                    shared.activeUser = ipt_username
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
                if parse_input_int([1, 2], "[1] Retry\n[2] Register\n", "Please Enter a valid value.") == 2:
                    clear()
                    register()


def register():
    # Ask for new username and password.
    print("Register your account (case sensitive)")

    with open('data/csv/login.csv') as f:
        existing_users = f.readlines()
        for i in existing_users:
            existing_users[existing_users.index(i)] = i.split(',')[0]

    while True:
        ipt_username = input("Username: ")
        if ipt_username not in existing_users:
            break
        else:
            print("User already exists.")
            if parse_input_int([1,2], "[1] Retry\n[2] Login\n", "Please Enter a valid value.") == 2:
                clear()
                return 0

    ipt_password = input("Password: ")
    # Register the input into the login.csv file.
    with open('data/csv/login.csv', 'a') as f:
        f.writelines('\n' + ipt_username + ',' + ipt_password)
    with open('data/csv/user_data.csv', 'a') as f:
        f.writelines('\n' + ipt_username + ',' + '0:0' + ',' + '0:0' + ',' + '0:0')
    print("Registration Successful, press Enter to Login...")
    input()
    clear()
