from modules.miscellaneous import *
import sys
import stdiomask
from modules.fireworks import *

if not sys.stdin.isatty():
    for i in range(1):
        print("Please run in command line.")
        time.sleep(0.2)

def log_in():
    os.system("mode con cols=80 lines=24")
    print("""
\t ██████╗ ██╗   ██╗██╗███████╗███████╗██╗      ██████╗ ████████╗ ™
\t██╔═══██╗██║   ██║██║╚══███╔╝██╔════╝██║     ██╔═══██╗╚══██╔══╝
\t██║   ██║██║   ██║██║  ███╔╝ █████╗  ██║     ██║   ██║   ██║   
\t██║█╗ ██║██║   ██║██║ ███╔╝  ██╔══╝  ██║     ██║   ██║   ██║   
\t╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗╚██████╔╝   ██║   
\t ╚══█╗═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝    ╚═╝   
\t\t\t\t\t\t     Copyleft © 2021 by Kevin""")
    hor_border = "|______________________________________________________________________________|\n"
    ver_border = "|                                                                              |\n"
    flt_border = " ______________________________________________________________________________\n"
    box_border1 = flt_border + ver_border * 2 + hor_border
    box_border2 = hor_border + ver_border * 2 + hor_border

    print(box_border1, 4*ver_border, box_border2, ver_border * 2, hor_border.strip(), sep='', end='')
    printp(10, 1, "|\t\t\t      Welcome to Quizelot")
    printp(13, 1, "| Please log in with your details to continue. Enter 'exit' to close.")
    printp(18, 1, "| Username: ")
    printp(21, 1, "| Password: ")

    # Keep asking for correct login credential until the correct one is entered.
    while True:
        # Ask for username
        ipt_username = inputp(18, 1, "| Username: ")
        if ipt_username == 'exit':
            os.system("mode con cols=110 lines=35")
            os.system('CLS')
            printp(11, 1, '\t\t\tBye~')
            print_firework()
            time.sleep(1)
            return False
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
                printp(21, 1, ver_border)
                move(21, 1)
                ipt_password = stdiomask.getpass("| Password: ")
                # If password is correct, return True.
                if ipt_password == row[1]:
                    shared.activeUser = ipt_username
                    printp(13, 1, ver_border)
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
                    print("""
\t ██████╗ ██╗   ██╗██╗███████╗███████╗██╗      ██████╗ ████████╗ ™
\t██╔═══██╗██║   ██║██║╚══███╔╝██╔════╝██║     ██╔═══██╗╚══██╔══╝
\t██║   ██║██║   ██║██║  ███╔╝ █████╗  ██║     ██║   ██║   ██║   
\t██║█╗ ██║██║   ██║██║ ███╔╝  ██╔══╝  ██║     ██║   ██║   ██║   
\t╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗╚██████╔╝   ██║   
\t ╚══█╗═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝    ╚═╝   
\t\t\t\t\t\t     Copyleft © 2021 by Kevin""")
                    hor_border = "|______________________________________________________________________________|\n"
                    ver_border = "|                                                                              |\n"
                    flt_border = " ______________________________________________________________________________\n"
                    box_border1 = flt_border + ver_border * 2 + hor_border
                    box_border2 = hor_border + ver_border * 2 + hor_border

                    print(box_border1, 4 * ver_border, box_border2, ver_border * 2, hor_border.strip(), sep='', end='')
                    printp(10, 1, "|\t\t\t      Welcome to Quizelot")
                    printp(13, 1, "| Please log in with your details to continue.")
                    printp(18, 1, "| Username: ")
                    printp(21, 1, "| Password: ")



def register():
    # Ask for new username and password.
    print("Register your account (case sensitive)")

    with open('data/csv/login.csv') as f:
        existing_users = f.readlines()
        for i in existing_users:
            existing_users[existing_users.index(i)] = i.split(',')[0]

    while True:
        ipt_username = input("Username: ")
        if ipt_username == 'exit':
            clear()
            return 0
        if ipt_username not in existing_users:
            break
        else:
            print("User already exists.")
            if parse_input_int([1, 2], "[1] Retry\n[2] Login\n", "Please Enter a valid value.") == 2:
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
