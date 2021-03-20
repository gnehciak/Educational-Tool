import csv
import os
import textwrap
import time
# Import variable from shared. (activeUser)
from modules import shared


# Clears the screen, only works when launched in Command Line.
def clear():
    os.system('CLS')


# Displays 'Press Enter to Continue...', postponing the program until user confirmation (presses Enter).
def pause():
    input("Press Enter to Continue...")


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
def parse_input_int(restriction, message, error_message) -> int:
    while True:
        # Try to parse the input to int
        try:
            number = int(input(message))
            # If the valid int entered is within the restriction, when return the valid input.
            if restriction[0] <= number <= restriction[1]:
                return number
            print(error_message)
        # When cannot parse, print error message and loop again.
        except ValueError:
            print(error_message)


def get_score():
    with open('data/csv/user_data.csv', 'r+') as f:
        text = f
        text = ''.join(text.readlines()).split('\n')
        for i in text:
            if i.split(',')[0] == shared.activeUser:
                new = i.split(',')
                return new[shared.currentSubject].split(':')[1]


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
