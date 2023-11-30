"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def use_quiz_week_1():
    while True:
        user_answer = input("Which ONE of the following is NOT a Python keyword?\n"
                            "1: in\n2: continue\n3: assert\n4: false")
        if user_answer not in ["1", "2", "3", "4"]:
            raise ValueError("Please answer with number between 1 to 4")
        else:
            return user_answer == "1"


def use_quiz_week_2():
    while True:
        user_answer = input("The flowchart symbol for making a choice is:\n"
                            "1: A sheared parallelogram\n2: A diamond\n3: A pill-shaped oval\n4: A rectangle")
        if user_answer not in ["1", "2", "3", "4"]:
            raise ValueError("Please answer with number between 1 to 4")
        else:
            return user_answer == "2"



def main():
    use_quiz_week_1()


if __name__ == '__main__':
    main()
