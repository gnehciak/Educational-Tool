import csv
import os
import time
import textwrap
import random

activeUser = ''
question_amt = 2

def useless():
    print("""
                                                              |                                                                                                                   ░░  
                                                              |                                                                                                                 ░░▓▓██
                                                              |                                                                                  ░░                            ░░▒▒▓▓██
                                                              |                                                                             ░░░░░░░░▒▒                      ░░░░▒▒▓▓░░
                                                              |                                                                         ░░░░░░▒▒░░▒▒▓▓░░░░                ░░▒▒▓▓▒▒    
                                                              |                                                                      ░░▒▒░░▒▒▓▓░░░░░░░░▒▒▓▓░░          ▒▒░░░░▓▓▒▒      
                                                              |                                                                   ░░░░▒▒░░░░░░░░░░░░▓▓▒▒▓▓▓▓▒▒░░    ░░▒▒▓▓▒▒░░        
                                                              |                                                               ░░░░░░░░▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓            
                                                              |                                                             ░░░░░░░░░░░░░░░░▒▒▓▓▓▓██▓▓▓▓▓▓    ░░▒▒▒▒▒▒░░              
                                                              |                                             ░░          ░░░░▒▒░░░░░░▒▒▓▓▒▒▓▓▒▒▒▒▓▓██▓▓▓▓▓▓        ▒▒                  
                                                              |                                         ░░░░▒▒▒▒  ░░░░░░░░▓▓▒▒░░░░░░░░▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒██                            
                      ### LOGIN ###                           |                                         ░░▓▓▓▓░░░░░░░░░░░░  ░░░░░░▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒                            
                                                              |                                     ░░░░░░▒▒░░░░░░▒▒▒▒▓▓░░░░░░▒▒██▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒                            
                      Username                                |                                 ░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓██▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒                            
                      |----------------------|                |                                 ▒▒▒▒░░░░░░░░▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒                              
                      |                      |                |                                 ▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▒▒                              
                      |----------------------|                |                                 ▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓██▓▓▒▒██▓▓▓▓▓▓▒▒▓▓▓▓▒▒                              
                      Password                                |                                 ░░░░░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▒▒                              
                      |----------------------|                |                                 ▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓                              
                      |                      |                |                                 ▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▒▒▓▓░░      ▒▒▒▒▒▒▒▒▓▓▓▓                              
                      |----------------------|                |                                 ░░▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒              ▒▒▒▒▓▓▒▒                              
                                                              |                                     ░░▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  ░░                                  
                                                              |                                                 ░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒                                                      
                                                              |                                                 ░░██▒▒▒▒▒▒▒▒▒▒▓▓                                                      
                                                              |                                                   ▒▒▒▒▓▓▒▒▒▒▒▒▓▓                                                      
                                                              |                                                   ▒▒▒▒▓▓▓▓▒▒▒▒▓▓                                                      
                                                              |                                                     ░░▒▒▒▒▒▒▓▓▓▓                                                      
                                                              |                                                         ░░▒▒▓▓░░                                                      
""")

# Miscellaneous
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
            if record[0] == activeUser:
                if int(record[subject]) >= level_no:
                    return level_no
        return '█'

def sleep(t):
    time.sleep(t)

# Initialisation
def logIn():
    print("Welcome to Quizelot")
    print("Please log in with your details to continue.")

    # Keep asking for correct login credential until the correct one is entered.
    while True:
        # Ask for username
        ipt_Username = input("Username: ")
        # Open the login.csv file to check if username instance exists
        with open('login.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            # Attempt to find username line by line
            for row in reader:
                # Make sure that the row has a value
                if row:
                    if ipt_Username == row[0]:
                        user_found = True
                        break
                    else:
                        user_found = False
            # If found, ask for password.
            if user_found:
                ipt_Password = input("Password: ")
                # If password is correct, return True.
                if ipt_Password == row[1]:
                    global activeUser
                    activeUser= ipt_Username
                    print("Login Successful!")
                    pause()
                    return True
                # Else loop back and try again.
                else:
                    print("Incorrect password, please try again.")
                    continue
            # If username not found, give options to retry or register.
            else:
                print("Account not found.")
                print("[1] Retry")
                print("[2] Register")
                if int(input()) == 2:
                    clear()
                    register()
def register():
    # Ask for new username and password.
    print("Register your account")
    ipt_Username = input("Username: ")
    ipt_Password = input("Password: ")
    # Register the input into the login.csv file.
    with open('login.csv', 'a') as f:
        f.writelines('\n' + ipt_Username + ',' + ipt_Password)
    with open('user_data.csv', 'a') as f:
        f.writelines('\n' + ipt_Username + ',' + '0' + ',' + '0' + ',' + '0')
    print("Registration Successful, press Enter to Login...")
    input()
    clear()
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

    while True:
        try:
            selection = int(input("Select a Topic to Begin!\n---> "))
            break
        except ValueError:
            print("Please enter a valid selection.")
    if (selection == 1):
        algebra()

    return 0




# Algebra
def algebra():
    print("""
  █████   ██       ██████   ███████  ██████   ██████     █████ 
 ██   ██  ██      ██        ██       ██   ██  ██   ██   ██   ██
 ███████  ██      ██   ███  █████    ██████   ██████    ███████
 ██   ██  ██      ██    ██  ██       ██   ██  ██   ██   ██   ██
 ██   ██  ███████  ██████   ███████  ██████   ██    ██  ██   ██
""")


    print("""
┌───┐  ╦  ┌─┐┌─┐┬─┐┌┐┌
│ 1 │  ║  ├┤ ├─┤├┬┘│││
└───┘  ╩═╝└─┘┴ ┴┴└─┘└┘""")

    print("""
┌───┐  ╔═╗┌─┐┬  ┌─┐┌─┐┌┬┐  ╦  ┌─┐┬  ┬┌─┐┬  
│ 2 │  ╚═╗├┤ │  ├┤ │   │   ║  ├┤ └┐┌┘├┤ │  
└───┘  ╚═╝└─┘┴─┘└─┘└─┘ ┴   ╩═╝└─┘ └┘ └─┘┴─┘""")

    print("""
┌───┐  ╔╗ ┌─┐┌─┐┬┌─
│ 3 │  ╠╩╗├─┤│  ├┴┐
└───┘  ╚═╝┴ ┴└─┘┴ ┴
""")

    while True:
        try:
            selection = int(input("---> "))
            if selection in range(1, 4):
                break
            else:
                print("Please enter a value between 1-3.")
        except ValueError:
            print("Please enter a value between 1-3.")
    if (selection == 1):
        clear()
        algebra_Learn()
    elif selection == 2:
        clear()
        algebra_Levels()
    elif selection == 3:
        clear()
        return 0
    else:
        raise Exception("Fatal Error.")

    clear()



    return 0
def algebra_Learn():

    with open('algebra_learn.txt') as f:
        for line in f:
            printWrap(line, 100)
            pause()

    return 0
def algebra_Levels():

    print("Choose a level to begin: ")

    print(f"""
    ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
    │ {check_level(1, 1)} │   │ {check_level(1, 2)} │   │ {check_level(1, 3)} │   │ {check_level(1, 4)} │   │ {check_level(1, 5)} │
    └───┘   └───┘   └───┘   └───┘   └───┘
""")

    print("( █ indicates that the level is still locked.)")

    while True:
        try:
            level = int(input("---> "))
            if level in range(1, 6):
                break
            else:
                print("Please enter a value between 1-5.")
        except ValueError:
            print("Please enter a value between 1-5.")

    score = 0
    for i in range(1, question_amt + 1):
        print(f"Question: {i}/{question_amt}")
        print(f"Score: {score}")
        score += algebra_Levels_Questions(level, i)
        pause()
        clear()

    print(f"You finished with a score of {score}/{question_amt}!")
    if score < question_amt - 1:
        print(f"You will need to score {question_amt} or above to unlock the next level!")
    elif score >= question_amt - 1:
        with open('user_data.csv', 'r+') as f:
            reader = csv.reader(f, delimiter=',')
            for record in reader:
                if record[0] == activeUser:
                    if int(record[1]) <= 5:

                        print("Congratulations! You've unlocked the next level:")
                        print("Level", int(record[1]) + 1, 'unlocked.')

        with open('user_data.csv', 'r+') as f:
            lines = list(f)
            for i in lines:
                if i[0] == activeUser:
                    lines[lines.index(i[0])][1] += 1
            writer = csv.writer(f)
            writer.writerows(lines)


    return 0



def algebra_Levels_Questions(level, current_question):
    with open('algebra_levels_questions.txt') as f:
        line = f.readlines()
        while True:
            selected_question = random.choice(line)
            selected_question = selected_question.split(';')
            if int(selected_question[0]) <= level and int(selected_question[1]) >= level:
                break

    question = selected_question[2]
    exc = str(random.randrange(0, 5 ** level)) if level < 4 else str(random.randrange(-2 ** level, 5 ** level))
    at = str(random.randrange(2, 2 ** level)) if level != 1 else ''
    has = str(random.randrange(1, 5 ** level))
    question = question.replace('!', exc).replace('@', at).replace('#', has)
    print(f"{current_question}) {question}")
    answer = eval(selected_question[3].replace('!', exc).replace('@', at).replace('#', has))
    print(answer)

    selection = []
    for i in range(1, 4):
        selection.append(eval(selected_question[3].replace('!', str(random.randrange(-8*level, 15*level))).replace('@', str(random.randrange(-8*level, 15*level))).replace('#', str(random.randrange(-8*level, 15*level)))))

    selection.append(answer)
    # Shuffle the answers.
    random.shuffle(selection)
    alpha = ['a', 'b', 'c', 'd']
    for i in range(1, 5):
        print('\t', alpha[i-1] + ')', selection[i-1])

    answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    while True:
        try:
            user_Answer = input("---> ").lower()
            if user_Answer in answers:
                if answers[user_Answer] in range(1, 5):
                    break
            else:
                print("Please enter a value from A to D")
        except ValueError:
            print("Please enter a value from A to D")

    if selection[answers[user_Answer] - 1] == answer:
        print("Correct!")
        return 1

    print("Incorrect.")
    return 0



# Geometry
def geometry():
    return 0

# Trigonometry
def trigonometry():
    return 0



activeUser = "Kevin"
algebra_Levels()


"""
if logIn():
    clear()
    mainMenu()
    
check_level(1,1)

algebra_Levels_Questions(3, 3)
    
algebra()



"""

