import csv
import os
import sys
import textwrap
import time
import random

# Import variable from shared. (activeUser)
from modules import shared
# Import colorama
from modules.colorama import init

# Initialise colorama
init()


# Move the cursor to y, x
def move(y, x):
    print(f"\033[%d;%dH" % (y, x))


# Print a message at y, x
def printp(y, x, txt):
    move(y, x)
    print(txt, end='')


# Get input from y, x
def inputp(y, x, txt):
    move(y, x)
    return input(txt)


# Clears the screen, only works when launched in Command Line.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Displays 'Press Enter to Continue...', postponing the program until user confirmation (presses Enter).
def pause(msg = "Press Enter to Continue..."):
    input(msg)


# Prints a long single line of text into multiple shortened lines.
def print_wrap(text, length):
    print(textwrap.fill(text, length))


# Checks if a particular user has unlocked a level or not.
# *Used to display levels in the level selector as well as at the end of each quiz.
def check_level(subject, level_no):
    with open('data/csv/user_data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for record in reader:
            if record[0] == shared.activeUser:
                if int(record[subject].split(':')[0]) >= level_no:
                    # If the level requested is smaller than or equal to the level the user is currently in
                    # (from the user_date.csv file), then return the level number.

                    return level_no
        # If the level requested is bigger than the level the user is currently in
        # (from the user_date.csv file), then return the level number.
        return '█'


# Puts the program to sleep for 't' seconds.
def sleep(t):
    time.sleep(t)


# Keeps asking for a valid int within a restriction and returns a valid input.
def parse_input(restriction, message, error_message):
    # Try to parse the input to int
    try:
        number = int(input(message))
        # If the valid int entered is within the restriction, when return the valid input.
        if restriction[0] <= number <= restriction[1]:
            return number
        print(error_message)
        pause("Press Enter to try again...")
        clear()
        return None
    # When cannot parse, print error message and loop again.
    except ValueError:
        print(error_message)
        pause("Press Enter to try again...")
        clear()
        return None


# Returns the total score for a particular subject
def get_score():
    with open('data/csv/user_data.csv', 'r+') as f:
        text = f
        text = ''.join(text.readlines()).split('\n')
        for i in text:
            if i.split(',')[0] == shared.activeUser:
                new = i.split(',')
                return new[shared.currentSubject].split(':')[1]


# Print the menu
def get_subject_menu():
    return """
\t┌───┐  ╦  ┌─┐┌─┐┬─┐┌┐┌
\t│ 1 │  ║  ├┤ ├─┤├┬┘│││
\t└───┘  ╩═╝└─┘┴ ┴┴└─┘└┘

\t┌───┐  ╔═╗┌─┐┬  ┌─┐┌─┐┌┬┐  ╦  ┌─┐┬  ┬┌─┐┬  
\t│ 2 │  ╚═╗├┤ │  ├┤ │   │   ║  ├┤ └┐┌┘├┤ │  
\t└───┘  ╚═╝└─┘┴─┘└─┘└─┘ ┴   ╩═╝└─┘ └┘ └─┘┴─┘

\t┌───┐  ╔╗ ┌─┐┌─┐┬┌─
\t│ 3 │  ╠╩╗├─┤│  ├┴┐
\t└───┘  ╚═╝┴ ┴└─┘┴ ┴
"""


# Prints the message "Congratulations!..."
def unlock_next_level():
    with open('data/csv/user_data.csv') as f:
        reader = csv.reader(f)
        for record in reader:
            if record[0] == shared.activeUser:
                if int(record[shared.currentSubject].split(':')[0]) <= 5:
                    print("Congratulations! You've unlocked the next level:")
                    print("Level", int(record[shared.currentSubject].split(':')[0]) + 1, 'unlocked.')
                    break


# Unlocks the next level
def add_level():
    with open('data/csv/user_data.csv', 'r+') as f:

        text = f
        text = ''.join(text.readlines()).split('\n')
        for i in text:
            if i.split(',')[0] == shared.activeUser:
                new = i.split(',')
                new[shared.currentSubject] = ':'.join(
                    [str(int(new[shared.currentSubject].split(':')[0]) + 1),
                     new[shared.currentSubject].split(':')[1]])
                new = ','.join(new)
                text[text.index(i)] = new
        text = '\n'.join(text)

    with open('data/csv/user_data.csv', 'w') as f:
        f.writelines(text)


# Generate random number for geometry.
def gen_rand_geometry(level):
    return str(random.randrange(1, 2 ** level) + random.choice([0, 0.5, 1, 1.5]) if level < 3 else str(
        random.randrange(1, 3 ** level) + random.choice([0, 0.25, 0.5, 0.75])))


# Set the window size.
def set_window_size(x, y):
    if os.name == 'nt':
        os.system(f"mode con cols={x} lines={y}")
    else:
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=y, cols=x))
    return 0


# Unlocks the first level.
def unlock_first_level():
    with open('data/csv/user_data.csv', 'r+') as f:
        text = f
        text = ''.join(text.readlines()).split('\n')
        for i in text:
            if i.split(',')[0] == shared.activeUser and i.split(',')[shared.currentSubject].split(':')[0] == '0':
                new = i.split(',')
                new[shared.currentSubject] = '1:0'
                new = ','.join(new)
                text[text.index(i)] = new
        text = '\n'.join(text)
    # Write the File
    with open('data/csv/user_data.csv', 'w') as f:
        f.writelines(text)
    return 0


# Print the answer selection list in questions and check if selection is correct.
def print_selection_list(selection, current_question, question, answer, score):
    selection.append(round(answer, 2))
    random.shuffle(selection)
    alpha = ['a', 'b', 'c', 'd']

    answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    while True:
        # Print the current questions number
        print(f"Question: {current_question}/{shared.question_amt}")
        # Print the current score
        print(f"Score: {score}")
        # Print out the question
        print(f"{current_question}) {question}")
        # Print the answews
        for i in range(1, 5):
            print('\t', alpha[i - 1] + ')', selection[i - 1])
        try:
            user_answer = input("---> ").lower()
            # If the valid int entered is within the restriction, when return the valid input.
            if user_answer in answers:
                if answers[user_answer] in range(1, 5):
                    break
            else:
                print("Please Enter a value from A to D")
                pause("Press Enter to try again...")
                clear()
        # When cannot parse, print error message and loop again.
        except ValueError:
            print("Please Enter a value from A to D")
            pause("Press Enter to try again...")
            clear()

    if selection[answers[user_answer] - 1] == answer:
        print("Correct!")
        return 1

    print("Incorrect.")
    return 0


def print_login():
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
    printp(14, 1, "| \t- Enter 'help' for information about the program.")
    printp(15, 1, "| \t- Enter 'exit' to close.")
    printp(18, 1, "| Username: ")
    printp(21, 1, "| Password: ")

