import random

from modules.miscellaneous import *


def algebra():
    # Set the current subject to 1:Algebra
    shared.currentSubject = 1
    # Print the main interface
    print("""
  █████   ██        ██████   ███████  ██████   ██████     █████ 
 ██   ██  ██       ██        ██       ██   ██  ██   ██   ██   ██
 ███████  ██       ██   ███  █████    ██████   ██████    ███████
 ██   ██  ██       ██    ██  ██       ██   ██  ██   ██   ██   ██
 ██   ██  ███████   ██████   ███████  ██████   ██    ██  ██   ██
""")
    # Print the total point returned from the get_score function for Algebra
    print(" >>> Total points for Algebra:", get_score())
    # Print the subject menu
    print(get_subject_menu())

    # Ask for valid value from 1 to 3
    selection = parse_input_int([1, 3], " >>> ", "Please enter a value between 1-3.")
    # Return the selection
    return selection


def algebra_learn():
    # Display the algebra learn text
    with open('data/txt/algebra_learn.txt') as f:
        for line in f:
            print_wrap(line, 100)
            pause()
    # Set the level to 1, unlocks the first level.
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


def algebra_levels():
    # Print the total point returned from the get_score function for Algebra
    print(" >>> Total points for Algebra:", get_score())
    print("Choose a level to begin: ")

    # Print out level boxes with the unlocked levels from check_level function.
    print(f"""
\t┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
\t│ {check_level(shared.currentSubject, 1)} │   │ {check_level(shared.currentSubject, 2)} │   │ {check_level(shared.currentSubject, 3)} │   │ {check_level(shared.currentSubject, 4)} │   │ {check_level(shared.currentSubject, 5)} │ 
\t└───┘   └───┘   └───┘   └───┘   └───┘
""")

    # Print helpful stuff
    print("( █ indicates that the level is still locked.)")
    print("Enter 0 to go back.")
    print("Finish the learn section to unlock the first level.") if check_level(shared.currentSubject, 1) == '█' else ''

    # Get the level selection from user
    while True:
        level = parse_input_int([0, 5], ' >>> ', "Please enter a value between 1-5.")
        # If input is 0 then return and go back to previous menu
        if level == 0:
            return 0
        # If level is unlocked then break the loop
        if check_level(shared.currentSubject, level) == level:
            break
        # Else print the level is locked
        print("Level locked!")

    clear()

    # Set the score to 0
    score = 0
    # Ask the set question_amt var amount of questions and add 1 to score if the algebra_levels_questions returns 1
    for i in range(1, shared.question_amt + 1):
        # Print the current questions number
        print(f"Question: {i}/{shared.question_amt}")
        # Print the current score
        print(f"Score: {score}")
        # Call the algebra_levels_questions function and add the returned value to the score
        score += algebra_levels_questions(level, i)
        # Pause
        pause()
        clear()

    # Print the final finishing score
    print(f"You finished with a score of {score}/{shared.question_amt}!")

    # Add the final score to the total score for algebra
    with open('data/csv/user_data.csv', 'r+') as f:
        text = f
        text = ''.join(text.readlines()).split('\n')
        for i in text:
            if i.split(',')[0] == shared.activeUser:
                new = i.split(',')
                new[shared.currentSubject] = ':'.join([new[shared.currentSubject].split(':')[0],
                                                       str(int(
                                                           new[shared.currentSubject].split(':')[1]) + score * level)])
                print()
                print('-------------------------')
                print(f"Total points for Algebra: {new[shared.currentSubject].split(':')[1]} ↑{score * level}")
                print('-------------------------')
                print()
                new = ','.join(new)
                text[text.index(i)] = new
    text = '\n'.join(text)
    # Write the File
    with open('data/csv/user_data.csv', 'w') as f:
        f.writelines(text)

    # If score < question amount, then print not enough score to unlock next level.
    if score < shared.question_amt and check_level(shared.currentSubject, level + 1) == '█':
        print(f"You will need to score {shared.question_amt} scores to unlock the next level!")
    # If user acquired full score, the next level is locked, and the level attempted is not 5, print congratulations and
    # write the new data to the files.
    elif score == shared.question_amt and check_level(shared.currentSubject, level + 1) == '█' and level < 5:

        #with open('data/csv/user_data.csv') as f:


        with open('data/csv/user_data.csv', 'r+') as f:

            reader = csv.reader(f)
            for record in reader:
                if record[0] == shared.activeUser:
                    if int(record[shared.currentSubject].split(':')[0]) <= 5:
                        print("Congratulations! You've unlocked the next level:")
                        print("Level", int(record[shared.currentSubject].split(':')[0]) + 1, 'unlocked.')
                        break



            text = f
            text = ''.join(text.readlines()).split('\n')
            for i in text:
                if i.split(',')[0] == shared.activeUser:
                    new = i.split(',')
                    new[shared.currentSubject] = ':'.join([str(int(new[shared.currentSubject].split(':')[0]) + 1),
                                                           new[shared.currentSubject].split(':')[1]])
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
    answer = round(answer, 2) if answer != int(answer) else int(answer)
    print(answer)

    selection = []
    for i in range(1, 4):
        ran_answer = selected_question[3].replace('!', str(random.randrange(-8 * level, 15 * level))).replace('@', str(
            random.randrange(-8 * level, 15 * level))).replace('#', str(random.randrange(-8 * level, 15 * level)))
        while eval(ran_answer) in selection or eval(ran_answer) == answer:
            ran_answer = selected_question[3].replace('!', str(random.randrange(-8 * level, 15 * level))).replace('@',
                                                                                                                  str(
                                                                                                                      random.randrange(
                                                                                                                          -8 * level,
                                                                                                                          15 * level))).replace(
                '#', str(random.randrange(-8 * level, 15 * level)))
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
