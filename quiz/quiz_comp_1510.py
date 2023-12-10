"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random
import sys


def ask_quiz_week_one():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 4, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("Which ONE of the following is NOT a Python keyword?\n"
                        "1: in\n2: continue\n3: assert\n4: false\n").strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "4"


def ask_quiz_week_two():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 2, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("The flowchart symbol for making a choice is:\n"
                        "1: A sheared parallelogram\n2: A diamond\n3: A pill-shaped oval\n4: A rectangle\n").strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "2"


def ask_quiz_week_three():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 3, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input('If word = "I love Fridays!", what is word[-3]?\n'
                        '1: This will cause an interpreter error\n2: "a"\n3: "y"\n4: "o"\n').strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "3"


def ask_quiz_week_four():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 4, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input('What word do we use to describe two variables that are bound to the same object in the heap?\n'
                        '1: concatenated\n2: immutable\n3: references\n4: aliases\n').strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "4"


def ask_quiz_week_five():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 2, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("Which ONE of these reads the tokens generated from our source code using syntax rules?\n"
                        "1: compiler\n2: parser\n3: interpreter\n4: lever\n").strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "2"


def ask_quiz_week_six():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 1, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("What does the try block in a try-except statement do?\n"
                        "1: It runs a block of code and handles any exceptions that are thrown\n"
                        "2: It tries different blocks of code until one without an error is found\n"
                        "3: It attempts to execute a block of code and retries if an error occurs\n"
                        "4: It tries to execute a block of code and exits if it fails.\n").strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "1"


def ask_quiz_week_seven():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 1, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("What does short-circuiting mean in the context of logical operations in Python?\n"
                        "1: The second operand is not evaluated if the first operand is sufficient to determine the result\n"
                        "2: The logical operation is bypassed entirely\n"
                        "3: The code execution stops due to an error\n"
                        "4: The operation takes a shortcut to return a default value\n").strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "1"


def ask_quiz_week_eight():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 3, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("What is the purpose of the os.remove() function in Python?\n"
                        "1: To remove a specified directory\n"
                        "2: To remove a variable from memory\n"
                        "3: To delete the specified file\n"
                        "4: To uninstall a Python package\n").strip()
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "3"


def ask_quiz_week_nine():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 2, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("What is a characteristic of recursive functions in Python\n"
                        "1: They cannot have more than one base case\n"
                        "2: They are functions that call themselves\n"
                        "3: They require an additional module to be imported\n"
                        "4: They always execute faster than equivalent iterative solutions\n")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "2"


def ask_quiz_week_ten():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 2, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("What is a closure in Python?\n"
                        "1: A feature that closes a file after its execution\n"
                        "2: A function that remembers the environment in which it was created\n"
                        "3: A function returned by another function\n"
                        "4: An error that occurs when a function is not closed properly\n")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "2"


def ask_bonus_quiz():
    """
    Prompt user with basic programming questions based on the python language.

    :postcondition: validate user input and check if answer is correct
    :return: Boolean True if answer is 1, else function will return False
    :raises ValueError: if user input is not an integer between 1 and 4 inclusive
    """
    user_answer = input("Bonus question!!\nChris is a good teacher\n1: True\n2: False\n")
    if user_answer not in ["1", "2"]:
        raise ValueError("Please answer with number between 1 and 2")
    elif user_answer == "1":
        return True
    else:
        pass
        # die()


def pick_quiz():
    """
    Select a quiz from a pool of quizzes.

    Select a function, randomly, that will quiz the user.

    :precondition: a list containing all the quiz functions must exist
    :postcondition: select a quiz function
    :return: a quiz function
    """
    quiz_list = [ask_quiz_week_one, ask_quiz_week_two, ask_quiz_week_three, ask_quiz_week_four, ask_quiz_week_five,
                 ask_quiz_week_six, ask_quiz_week_seven, ask_quiz_week_eight, ask_quiz_week_nine, ask_quiz_week_ten]

    copy_quiz_list = quiz_list.copy()

    if copy_quiz_list:
        index = random.randint(0, len(copy_quiz_list) - 1)
        return copy_quiz_list.pop(index)
    else:
        copy_quiz_list = quiz_list.copy()
        index = random.randint(0, len(copy_quiz_list) - 1)
        return copy_quiz_list.pop(index)


def check_answer(character, answer):
    """
    Change character's intelligence stat.

    Change character's intelligence stat based on if their answer to the quiz is correct.

    :param character: a dictionary with key-value pairs() representing character details
    :param answer: a Boolean value
    :precondition character: must be a dictionary with key-value pairs() representing character details
    :precondition answer: must be a Boolean value
    :return: None
    """
    if answer:
        character["status"]["intelligence"]["value"] += 1
    else:
        character["status"]["intelligence"]["value"] -= 1
    return


def display_result(answer):
    """
    Notify the user about their intelligence stat changing.

    :param answer: is a Boolean value
    :postcondition: print a message notifying the user of an increase or a decrease in the intelligence stat
    :return: None
    """
    if answer:
        return print(f"{answer}: Your intelligence has increased by 1")
    else:
        return print(f"{answer}: Your intelligence has decreased by 1")


def ask_quiz(quiz):
    """
    Execute a quiz function.

    :param quiz: a function that simulates a simple quiz through the console
    :preconditon: quiz function must work
    :postcondition: invoke the quiz function
    :return: invoking the function
    """
    while True:
        try:
            return quiz()
        except ValueError as e:
            print("{}".format(str(e)), file=sys.stderr)


def run_quiz(character):
    """
    Invoke helper functions to similate a quiz for the player.

    :param character: a dictionary with key-value pairs representing character details
    :postcondition: simulate a quiz for the player
    :return: None
    """
    print("QUIZ!!")
    answer = ask_quiz(pick_quiz())
    check_answer(character, answer)
    display_result(answer)


def main():
    pass


if __name__ == '__main__':
    main()
