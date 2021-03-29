from modules.miscellaneous import *

def help():
    # Displays the algebra learn text
    with open('data/txt/help.txt') as f:
        for line in f:
            # Print the individuals lines from the file and wrap the text.
            print_wrap(line, 80)
            print()
    pause()
    return 0