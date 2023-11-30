"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def use_quiz_week_one():
    user_answer = input("Which ONE of the following is NOT a Python keyword?\n"
                        "1: in\n2: continue\n3: assert\n4: false\n")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "4"


def use_quiz_week_two():
    user_answer = input("The flowchart symbol for making a choice is:\n"
                        "1: A sheared parallelogram\n2: A diamond\n3: A pill-shaped oval\n4: A rectangle\n")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "2"


def use_quiz_week_three():
    user_answer = input('If word = "I love Fridays!", what is word[-3]?\n'
                        '1: This will cause an interpreter error\n2: "a"\n3: "y"\n4: "o"\n')
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "3"


def use_quiz_week_four():
    user_answer = input('What word do we use to describe two variables that are bound to the same object in the heap?\n'
                        'concatenated\nimmutable\nreferences\naliases')
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "4"


def use_quiz_week_five():
    user_answer = input("Which ONE of these reads the tokens generated from our source code using syntax rules?\n"
                        "1: compiler\n2: parser\n3: interpreter\n4: lever")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "2"


def use_quiz_week_six():
    user_answer = input("What does the try block in a try-except statement do?"
                        "1: It runs a block of code and handles any exceptions that are thrown"
                        "2: It tries different blocks of code until one without an error is found"
                        "3: It attempts to execute a block of code and retries if an error occurs"
                        "4: It tries to execute a block of code and exits if it fails.")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "1"


def use_quiz_weak_seven():
    user_answer = input("What does short-circuiting mean in the context of logical operations in Python?"
                        "1: The second operand is not evaluated if the first operand is sufficient to determine the result"
                        "2: The logical operation is bypassed entirely"
                        "3: The code execution stops due to an error"
                        "4: The operation takes a shortcut to return a default value")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "1"


def use_quiz_weak_eight():
    user_answer = input("What is the purpose of the os.remove() function in Python?"
                        "1: To remove a specified directory."
                        "2: To remove a variable from memory."
                        "3: To delete the specified file."
                        "4: To uninstall a Python package")
    if user_answer not in ["1", "2", "3", "4"]:
        raise ValueError("Please answer with number between 1 and 4")
    else:
        return user_answer == "3"


def use_bonus_quiz():
    user_answer = input("Chris is a good teacher\n1: True\n2: False")
    if user_answer not in ["1", "2"]:
        raise ValueError("Please answer with number between 1 to 2")
    elif user_answer == "1":
        return True
    else:
        pass
        # die()


def main():
    while True:
        try:
            a = use_quiz_week_one()
        except ValueError as e:
            print(e)
        else:
            print(a)
            return


if __name__ == '__main__':
    main()
