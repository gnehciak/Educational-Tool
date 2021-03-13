# Import the algebra Module, to allow the functions algebra etc. to be called.
from modules.algebra import *
# Import the login Module, to allow the function login() to be called.
from modules.login import *


# Main menu function, contains the navigation for different topics and logout.
def main_menu():
    # Prints out awesome stuff!
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

    # Keep asking for a valid value between 0-3 until a valid one is entered.
    while True:
        try:
            selection = int(input("Select a Topic to Begin!\n---> "))
            if selection in range(0, 4):
                break
            else:
                print("Please enter a value between 0-3.")
        except ValueError:
            print("Please enter a valid selection.")

    # If the value entered is 1, then return 1, which will be used in the main function to call the algebra() function.
    if selection == 1:
        return 1
    # If the value entered is 0, then return 0, which will be used to go back to the login screen.
    elif selection == 0:
        return 0


# Keep asking for a valid login detail until the a existing one is entered.
while log_in():
    # Clear the screen
    clear()
    # Keep the user in the main menu until break is called.
    while True:
        # The main menu returns the selection from 0-3, which will be used to call different functions here.
        subject = main_menu()
        clear()
        # If the selection from main_menu() is 0, then it will break the main menu loop and go back to the login screen.
        if subject == 0:
            break
        # If the selection is 1, the call the algebra function.
        elif subject == 1:
            # Keep the user in the Algebra menu until break is called.
            while True:
                # Get the selection for 'learn', 'level', or 'back'.
                select = algebra()
                # Clear the screen after selection to get ready for the next function to be called.
                clear()
                # If the selection is one, then call the algebra_learn() function. After finishing the learning process,
                # algebra_learn() will return 0 and go back into the algebra loop.
                if select == 1:
                    algebra_learn()
                # If the selection is 2, then call the algebra_levels() function.
                elif select == 2:
                    algebra_levels()
                # If the seleciton is 3 (back), then break the algebra loop and go back to the main menu.
                elif select == 3:
                    break
                # Clear the screen before going back to the main menu.
                clear()
        elif subject == 2:
            continue
        elif subject == 3:
            continue
