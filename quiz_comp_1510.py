"""
Tatsunori Marumo
A01327744
"""


def use_quiz_week_1():
    while True:
        user_answer = input("Which ONE of the following is NOT a Python keyword?\n"
                            "1: in\n2: continue\n3: assert\n4: false")
        if user_answer not in ["1", "2", "3", "4"]:
            raise ValueError("Please answer with number between 1 to 4")
        else:
            return user_answer == "1"


def main():
    ask_quiz_week_1()


if __name__ == '__main__':
    main()
