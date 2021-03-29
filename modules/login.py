from modules.miscellaneous import *
import sys
#import stdiomask
from modules.fireworks import *
from modules.help import *

from modules import stdiomask


def log_in():
    if not sys.stdin.isatty():
        print("Please run in command line.")
        pause()
        return False
    set_window_size(80, 24)

    hor_border = "|______________________________________________________________________________|\n"
    ver_border = "|                                                                              |\n"
    flt_border = " ______________________________________________________________________________\n"
    box_border1 = flt_border + ver_border * 2 + hor_border
    box_border2 = hor_border + ver_border * 2 + hor_border

    print_login()

    # Keep asking for correct login credential until the correct one is entered.
    while True:
        # Ask for username
        ipt_username = inputp(18, 1, "| Username: ")
        if not ipt_username:
            clear()
            print_login()
            continue
        # Is the username entered is exit, then quit the program.
        if ipt_username.lower() == 'exit':
            os.system("mode con cols=110 lines=35")
            os.system('CLS')
            printp(11, 1, '\t\t\tBye~')
            print_firework()
            time.sleep(1)
            return False
        if ipt_username.lower() == "help":
            clear()
            help()
            clear()
            print_login()
            continue

        # Open the login.csv file to check if username instance exists
        with open('data/csv/login.csv', 'r') as f:
            users = f.readlines()
            # Attempt to find username line by line
            for user in users:
                user = user.split(',', 1)
                # Make sure that the row has a value
                if user:
                    if ipt_username == user[0]:
                        user_found = True
                        break
                    else:
                        user_found = False
            # If found, ask for password.
            if user_found:
                printp(21, 1, ver_border)
                move(21, 1)
                ipt_password = stdiomask.getpass("| Password: ")
                # If password is correct, return True.
                if ipt_password == user[1]:
                    shared.activeUser = ipt_username
                    printp(13, 1, ver_border)
                    printp(14, 1, ver_border)
                    printp(15, 1, ver_border)
                    printp(13, 1, "| Login Successful!")
                    inputp(15, 1, "| Press Enter to continue...")
                    return True
                # Else loop back and try again.
                else:
                    printp(21, 1, "| Password: Incorrect password, please try again.")
                    printp(18, 1, ver_border)
                    continue
            # If username not found, give options to retry or register.
            else:
                printp(13, 1, ver_border.strip())
                printp(14, 1, ver_border.strip())
                printp(15, 1, ver_border.strip())
                printp(13, 1, "| Account not found.")
                while True:
                    # Try to parse the input to int
                    try:
                        number = int(inputp(14, 1, "| [1] Retry  [2] Register\n| >>> "))
                        # If the valid int entered is within the restriction, when return the valid input.
                        if 1 <= number <= 2:
                            printp(18, 1, ver_border)
                            printp(12, 1, ver_border)
                            printp(13, 1, ver_border)
                            printp(14, 1, ver_border)
                            printp(15, 1, ver_border)
                            printp(13, 1, "| Please log in with your details to continue.")
                            printp(14, 1, "| \t- Enter 'help' for information about the program.")
                            printp(15, 1, "| \t- Enter 'exit' to close.")
                            printp(21, 1, ver_border)
                            printp(21, 1, "| Password: ")
                            break
                        printp(13, 1, ver_border.strip())
                        printp(13, 1, "| Please Enter a valid value.")
                        printp(15, 1, ver_border.strip())
                        # When cannot parse, print error message and loop again.
                    except ValueError:
                        printp(13, 1, ver_border.strip())
                        printp(13, 1, "| Please Enter a valid value.")
                        printp(15, 1, ver_border.strip())
                if number == 2:
                    clear()
                    register()
                    print_login()


def register():
    # Read the login file into a list
    with open('data/csv/login.csv') as f:
        existing_users = f.readlines()
        for i in existing_users:
            existing_users[existing_users.index(i)] = i.split(',', 1)[0]

    # Keep asking for a valid registration
    while True:
        print(" <<<Register your account>>>")
        print(" Enter 'exit' to go back.")
        print("\n Requirements:")
        print("\tUsername is case sensitive.")
        print("\t* Cannot contain any spaces.")
        print("\t* Must contain at least one letter.")
        print("\t* Only letters, numbers, commas, and underscores can be used.\n")

        # Get the username
        ipt_username = input("Username: ")
        # Replace period and underscore with spaces.
        ipt_username_alpha = ipt_username.replace('_', '').replace('.', '')
        # Remove numbers
        ipt_username_alpha = ''.join([i for i in ipt_username_alpha if not i.isdigit()])

        # If 'exit' is typed, exit to login.
        if ipt_username == 'exit':
            clear()
            return 0

        # If username contains a comma, ask for another valid username
        elif not ipt_username_alpha.isalpha():
            print("Invalid username format.")
            pause("Press Enter to try again...")
            clear()
        # If username is not already registered, proceed to registration.
        elif ipt_username not in existing_users:
            break
        # If username is found in the file, ask to login or retry.
        else:
            print("User already exists.")
            if parse_input([1, 2], "[1] Retry\n[2] Login\n", "Please Enter a valid value.") == 2:
                clear()
                return 0
            clear()

    # Get password
    ipt_password = input("Password: ")
    # Register the input into the login.csv file.
    with open('data/csv/login.csv', 'a') as f:
        f.writelines('\n' + ipt_username + ',' + ipt_password)
    # Register the user into the data file.
    with open('data/csv/user_data.csv', 'a') as f:
        f.writelines('\n' + ipt_username + ',' + '0:0' + ',' + '0:0' + ',' + '0:0')
    print("Registration Successful, press Enter to Login...")
    input()
    clear()