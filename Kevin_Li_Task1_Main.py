from modules.algebra import *
from modules.login import *


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
                    algebra_Levels()
                elif select == 3:
                    break
                clear()
        elif subject == 2:
            continue
        elif subject == 3:
            continue
