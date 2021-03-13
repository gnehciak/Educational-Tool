import csv
import os
import textwrap
import time

from modules import shared


def clear():
    os.system('CLS')


def pause():
    input("Press Enter to Continue...")


def print_wrap(text, length):
    print(textwrap.fill(text, length))


def check_level(subject, level_no):
    with open('data/csv/user_data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for record in reader:
            if record[0] == shared.activeUser:
                if int(record[subject]) >= level_no:
                    return level_no
        return '█'


def sleep(t):
    time.sleep(t)


def parse_input_int(restriction, message, error_message) -> int:
    while True:
        try:
            number = int(input(message))
            if number in restriction:
                return number
            print(error_message)
        except ValueError:
            print(error_message)
