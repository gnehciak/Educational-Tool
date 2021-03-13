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
                if int(record[subject]) >= level_no:
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
        try:
            number = int(input(message))
            if restriction[0] <= number <= restriction[1]:
                return number
            print(error_message)
        except ValueError:
            print(error_message)
