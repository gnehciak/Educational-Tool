import csv
import os
import time
import textwrap
import random
import shared

def clear():
    os.system('CLS')


def pause():
    input("Press Enter to Continue...")


def printWrap(text, length):
    print(textwrap.fill(text, length))


def check_level(subject, level_no):
    with open('user_data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for record in reader:
            if record[0] == shared.activeUser:
                if int(record[subject]) >= level_no:
                    return level_no
        return '█'