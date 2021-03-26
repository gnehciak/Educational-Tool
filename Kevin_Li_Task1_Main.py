# Import the algebra Module, to allow the functions algebra etc. to be called.
from modules.algebra import *
# Import the algebra Module, to allow the functions algebra etc. to be called.
from modules.geometry import *
# Import the fractions Module, to allow the functions algebra etc. to be called.
from modules.frac_n_dec import *
# Import the login Module, to allow the function login() to be called.
from modules.login import *


# Main menu function, contains the navigation for different topics and logout.
def main_menu():
    # Prints out awesome stuff!
    scores = []
    for i in range(1, 4):
        shared.currentSubject = i
        scores.append(int(get_score()))
    print()
    print(f" Welcome! {shared.activeUser}")
    print(" Choose a course below:")
    print("""
┌───┐  ┌─┐┬  ┌─┐┌─┐┌┐ ┬─┐┌─┐
│ 1 │  ├─┤│  │ ┬├┤ ├┴┐├┬┘├─┤
└───┘  ┴ ┴┴─┘└─┘└─┘└─┘┴└─┴ ┴""")
    print(" Score:", scores[0])
    print("""
┌───┐  ┌─┐┌─┐┌─┐┌┬┐┌─┐┌┬┐┬─┐┬ ┬
│ 2 │  │ ┬├┤ │ ││││├┤  │ ├┬┘└┬┘
└───┘  └─┘└─┘└─┘┴ ┴└─┘ ┴ ┴└─ ┴""")
    print(" Score:", scores[1])
    print("""
┌───┐  ┌─┐┬─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
│ 3 │  ├┤ ├┬┘├─┤│   │ ││ ││││└─┐
└───┘  └  ┴└─┴ ┴└─┘ ┴ ┴└─┘┘└┘└─┘""")
    print(" Score:", scores[2])
    print(" Total Score:", scores[0] + scores[1] + scores[2])
    print()
    print(" Enter 0 to sign out.")

    # Keep asking for a valid value between 0-3 until a valid one is entered.
    return parse_input_int([0, 3], " Select a Topic to Begin!\n---> ", " Please enter a valid selection.")



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
                    while algebra_levels():
                        pass
                # If the selection is 3 (back), then break the algebra loop and go back to the main menu.
                elif select == 3:
                    break
                # Clear the screen before going back to the main menu.
                clear()
        elif subject == 2:
            while True:
                # Get the selection for 'learn', 'level', or 'back'.
                select = geometry()
                # Clear the screen after selection to get ready for the next function to be called.
                clear()
                # If the selection is one, then call the geometry_learn() function. After finishing the learning
                # process, geometry_learn() will return 0 and go back into the algebra loop.
                if select == 1:
                    geometry_learn()
                # If the selection is 2, then call the geometry_learn() function.
                elif select == 2:
                    while geometry_levels():
                        pass
                # If the selection is 3 (back), then break the geometry loop and go back to the main menu.
                elif select == 3:
                    break
                # Clear the screen before going back to the main menu.
                clear()
        elif subject == 3:
            while True:
                # Get the selection for 'learn', 'level', or 'back'.
                select = frac_n_dec()
                # Clear the screen after selection to get ready for the next function to be called.
                clear()
                # If the selection is one, then call the geometry_learn() function. After finishing the learning
                # process, geometry_learn() will return 0 and go back into the algebra loop.
                if select == 1:
                    frac_n_dec_learn()
                # If the selection is 2, then call the geometry_learn() function.
                elif select == 2:
                    while frac_n_dec_levels():
                        pass
                # If the selection is 3 (back), then break the geometry loop and go back to the main menu.
                elif select == 3:
                    break
                # Clear the screen before going back to the main menu.
                clear()
            continue
