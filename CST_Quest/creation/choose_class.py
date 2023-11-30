"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def choose_class():
    """
    Let player choose a class

    This function ask player to choose one class from three classes

    postcondition: no invalid input is accepted
    :return: the chosen user class stored as string
    :raises ValueError: if user input is not string 1, 2 ,or 3
    """

    while True:
        user_class = (input("choose a class\n1: front-end developer\n2: back-end developer\n3: full-stack developer\n")
                      .strip())
        try:
            if user_class not in ["1", "2", "3"]:
                raise ValueError("Invalid input. Please choose a valid class number")
            if user_class == "1":
                return "front_end_developer"
            elif user_class == "2":
                return "back_end_developer"
            elif user_class == "3":
                return "full_stack_developer"
        except ValueError as error:
            print(error)


def main():
    choose_class()


if __name__ == '__main__':
    main()
