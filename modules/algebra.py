# Import the miscellaneous module, for functions such as get_subject_menu()
from modules.miscellaneous import *


# The algebra() function, takes care of the menu navigation as well as an overview of the player's score.
def algebra():
    # os.system("mode con cols=80 lines=40")
    # Set the current subject to 1:Algebra
    shared.currentSubject = 1
    # Print the main interface
    print("""
  █████  ██       ██████  ███████ ██████  ██████    █████ 
 ██   ██ ██      ██       ██      ██   ██ ██   ██  ██   ██
 ███████ ██      ██   ███ █████   ██████  ██████   ███████
 ██   ██ ██      ██    ██ ██      ██   ██ ██   ██  ██   ██
 ██   ██ ███████  ██████  ███████ ██████  ██    ██ ██   ██
""")
    # Print the total point returned from the get_score function for Algebra
    print(" >>> Total points for Algebra:", get_score())
    # Print the subject menu
    print(get_subject_menu())

    # Ask for valid value from 1 to 3
    selection = parse_input([1, 3], " >>> ", "Please enter a value between 1-3.")
    # Return the selection
    return selection


# Takes care of the learning section of algebra, displays a sequence of information about the subject and unlocks level
# 1 by writing the file if the level is still locked.
def algebra_learn():
    # Displays the algebra learn text
    with open('data/txt/algebra_learn.txt') as f:
        for line in f:
            # Print the individuals lines from the file and wrap the text.
            print_wrap(line, 80)
            # Pause to wait for user input.
            pause()
    # Set the level to 1, unlocks the first level.
    unlock_first_level()
    return 0


# Takes care of the levels pages, displays the 5 levels, and shows if they are locked or not. Loops the
# algebra_levels_questions function and manages the score.
def algebra_levels():

    # Get the level selection from user
    while True:
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
        print("Finish the learn section to unlock the first level.") if check_level(shared.currentSubject,
                                                                                    1) == '█' else ''
        level = parse_input([0, 5], ' >>> ', "Please enter a value between 1-5.")
        if level is None:
            continue
        # If input is 0 then return and go back to previous menu
        if int(level) == 0:
            return False
        # If level is unlocked then break the loop
        if check_level(shared.currentSubject, level) == level:
            break
        # Else print the level is locked
        print("Level locked!")
        pause()
        clear()

    clear()

    # Set the score to 0
    score = 0
    # Ask the set question_amt var amount of questions and add 1 to score if the algebra_levels_questions returns 1
    for i in range(1, shared.question_amt + 1):
        # Call the algebra_levels_questions function and add the returned value to the score
        score += algebra_levels_questions(level, i, score)
        # Pause
        pause()
        clear()

    # Print the final finishing score
    print(f"You finished with a score of {score}/{shared.question_amt}!")

    # Add the final score to the total score for algebra
    with open('data/csv/user_data.csv', 'r+') as f:
        text = f
        text = ''.join(text.readlines()).split('\n')
        # Find the current user's data.
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
    # Write the new score into the File
    with open('data/csv/user_data.csv', 'w') as f:
        f.writelines(text)

    # If score < question amount, then print not enough score to unlock next level.
    if score < shared.question_amt and check_level(shared.currentSubject, level + 1) == '█' and level < 5:
        print(f"You will need to score {shared.question_amt} scores to unlock the next level!")
    # If user acquired full score, the next level is locked, and the level attempted is not 5, print congratulations and
    # write the new data to the files.
    elif score == shared.question_amt and check_level(shared.currentSubject, level + 1) == '█' and level < 5:
        # Displays Unlock the next level message.
        unlock_next_level()
        # Unlocks the next level.
        add_level()

    pause()
    clear()
    return True


# Takes care of the question generation and answer checking.
def algebra_levels_questions(level, current_question, score):
    # Open the file containing the questions and choose a random line from the file.
    with open('data/txt/algebra_levels_questions.txt') as f:
        line = f.readlines()
        while True:
            selected_question = random.choice(line)
            selected_question = selected_question.split(';')
            if int(selected_question[0]) <= level <= int(selected_question[1]):
                break

    # Set the question that will be displayed to the use to the third range of the line.
    question = selected_question[2]
    # Generates the numbers which will get bigger when the level increases.
    exc = str(random.randrange(0, 5 ** level)) if level < 4 else str(random.randrange(-2 ** level, 5 ** level))
    at = str(random.randrange(2, 2 ** level)) if level != 1 else ''
    has = str(random.randrange(1, 5 ** level))
    # Replace the place holders in the question with the randomly generated numbers.
    question = question.replace('!', exc).replace('@', at).replace('#', has)
    # Evaluate the answer from the formula given on the fourth range of the selected question.
    answer = eval(selected_question[3].replace('!', exc).replace('@', at).replace('#', has))
    # Remove the decimal place if the answer does not need it.
    answer = round(answer, 2) if answer != int(answer) else int(answer)

    # Establish the selection for random generated wrong answers.
    selection = []
    # Generate 3 random answers.
    for i in range(1, 4):
        # Generate random numbers
        exc = str(random.randrange(0, 5 ** level)) if level < 4 else str(random.randrange(-2 ** level, 5 ** level))
        at = str(random.randrange(2, 2 ** level)) if level != 1 else ''
        has = str(random.randrange(1, 5 ** level))
        # Replace the place holder in the question.
        ran_answer = selected_question[3].replace('!', exc).replace('@', at).replace('#', has)
        # While the question is found in already generated answers, repeat the process to generate a new answer.
        while eval(ran_answer) in selection or eval(ran_answer) == answer:
            exc = str(random.randrange(0, 5 ** level)) if level < 4 else str(random.randrange(-2 ** level, 5 ** level))
            at = str(random.randrange(2, 2 ** level)) if level != 1 else ''
            has = str(random.randrange(1, 5 ** level))
            ran_answer = selected_question[3].replace('!', exc).replace('@', at).replace('#', has)
        # Evaluate the random answer
        ran_answer = round(eval(ran_answer), 2)
        ran_answer = ran_answer if ran_answer != int(ran_answer) else int(ran_answer)
        selection.append(ran_answer)

    # Print the selection list
    return print_selection_list(selection, current_question, question, answer, score)