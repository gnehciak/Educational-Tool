import random

from modules.miscellaneous import *


def algebra():
    shared.currentSubject = 1
    while True:
        print("""
      █████  ██       ██████  ███████ ██████  ██████    █████ 
     ██   ██ ██      ██       ██      ██   ██ ██   ██  ██   ██
     ███████ ██      ██   ███ █████   ██████  ██████   ███████
     ██   ██ ██      ██    ██ ██      ██   ██ ██   ██  ██   ██
     ██   ██ ███████  ██████  ███████ ██████  ██    ██ ██   ██
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
        if selection == 1:
            return 1
        elif selection == 2:
            return 2
        elif selection == 3:
            return 3
        else:
            raise Exception("Fatal Error.")


def algebra_learn():
    with open('data/txt/algebra_learn.txt') as f:
        for line in f:
            print_wrap(line, 100)
            pause()

    with open('data/csv/user_data.csv', 'r+') as f:

        text = f
        text = ''.join(text.readlines()).split('\n')
        for i in text:
            if i.split(',')[0] == shared.activeUser and i.split(',')[shared.currentSubject] == '0':
                new = i.split(',')
                new[shared.currentSubject] = '1'
                new = ','.join(new)
                text[text.index(i)] = new

        text = '\n'.join(text)

    with open('data/csv/user_data.csv', 'w') as f:
        f.writelines(text)

    return 0


def algebra_levels():
    while True:
        print("Choose a level to begin: ")

        print(f"""
        ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
        │ {check_level(shared.currentSubject, 1)} │   │ {check_level(shared.currentSubject, 2)} │   │ {check_level(shared.currentSubject, 3)} │   │ {check_level(shared.currentSubject, 4)} │   │ {check_level(shared.currentSubject, 5)} │ 
        └───┘   └───┘   └───┘   └───┘   └───┘
    """)

        print("( █ indicates that the level is still locked.)")
        print("Enter 0 to go back.")
        print("Finish the learn section to unlock the first level.")

        while True:
            try:
                level = int(input("---> "))
                if level in range(1, 6):
                    if check_level(shared.currentSubject, level) == level:
                        break
                    print("Level locked!")
                elif level == 0:
                    return 0
                else:
                    print("Please enter a value between 1-5.")
            except ValueError:
                print("Please enter a value between 1-5.")

        clear()

        score = 0
        for i in range(1, shared.question_amt + 1):
            print(f"Question: {i}/{shared.question_amt}")
            print(f"Score: {score}")
            score += algebra_levels_questions(level, i)
            pause()
            clear()

        print(f"You finished with a score of {score}/{shared.question_amt}!")
        if score < shared.question_amt and check_level(shared.currentSubject, level + 1) == '█':
            print(f"You will need to score {shared.question_amt} scores to unlock the next level!")
        elif score == shared.question_amt and check_level(shared.currentSubject, level + 1) == '█' and level < 5:

            with open('data/csv/user_data.csv', 'r') as f:
                reader = csv.reader(f)
                for record in reader:
                    if record[0] == shared.activeUser:
                        if int(record[1]) <= 5:
                            print("Congratulations! You've unlocked the next level:")
                            print("Level", int(record[1]) + 1, 'unlocked.')
                            break

            with open('data/csv/user_data.csv', 'r+') as f:

                text = f
                text = ''.join(text.readlines()).split('\n')
                for i in text:
                    if i.split(',')[0] == shared.activeUser:
                        new = i.split(',')
                        new[shared.currentSubject] = str(int(new[shared.currentSubject]) + 1)
                        new = ','.join(new)
                        text[text.index(i)] = new
                        # print(int(i.split(',')[currentSubject]) + 1)

                text = '\n'.join(text)

            with open('data/csv/user_data.csv', 'w') as f:
                f.writelines(text)

        pause()
        clear()


def algebra_levels_questions(level, current_question):
    with open('data/txt/algebra_levels_questions.txt') as f:
        line = f.readlines()
        while True:
            selected_question = random.choice(line)
            selected_question = selected_question.split(';')
            if int(selected_question[0]) <= level <= int(selected_question[1]):
                break

    question = selected_question[2]
    exc = str(random.randrange(0, 5 ** level)) if level < 4 else str(random.randrange(-2 ** level, 5 ** level))
    at = str(random.randrange(2, 2 ** level)) if level != 1 else ''
    has = str(random.randrange(1, 5 ** level))
    question = question.replace('!', exc).replace('@', at).replace('#', has)
    print(f"{current_question}) {question}")
    answer = eval(selected_question[3].replace('!', exc).replace('@', at).replace('#', has))
    answer = answer if answer != int(answer) else int(answer)
    print(answer)

    selection = []
    for i in range(1, 4):
        ran_answer = selected_question[3].replace('!', str(random.randrange(-8 * level, 15 * level))).replace('@', str(
            random.randrange(-8 * level, 15 * level))).replace('#', str(random.randrange(-8 * level, 15 * level)))
        while eval(ran_answer) in selection or eval(ran_answer) == answer:
            ran_answer = selected_question[3].replace('!', str(random.randrange(-8 * level, 15 * level))).replace('@',
            str(random.randrange(-8 * level,15 * level))).replace('#', str(random.randrange(-8 * level, 15 * level)))
        ran_answer = round(eval(ran_answer), 2)
        ran_answer = ran_answer if ran_answer != int(ran_answer) else int(ran_answer)
        selection.append(ran_answer)

    selection.append(round(answer, 2))
    # Shuffle the answers.
    random.shuffle(selection)
    alpha = ['a', 'b', 'c', 'd']
    for i in range(1, 5):
        print('\t', alpha[i - 1] + ')', selection[i - 1])

    answers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    while True:
        try:
            user_answer = input("---> ").lower()
            if user_answer in answers:
                if answers[user_answer] in range(1, 5):
                    break
            else:
                print("Please enter a value from A to D")
        except ValueError:
            print("Please enter a value from A to D")

    if selection[answers[user_answer] - 1] == answer:
        print("Correct!")
        return 1

    print("Incorrect.")
    return 0
