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
    """

    while True:
        user_class = input("choose a class\n1: front-end developer\n2: back-end developer\n3: full-stack developer\n")
        if user_class in ["1", "2", "3"]:
            break
        else:
            print("Invalid input. Please choose a valid class number.")
    if user_class == "1":
        user_class = "front_end_developer"
    elif user_class == "2":
        user_class = "back_end_developer"
    elif user_class == "3":
        user_class = "full_stack_developer"

    return user_class
