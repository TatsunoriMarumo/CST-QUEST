"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def choose_class():
    while True:
        user_class = input("choose a class\n1: front-end developer\n2: back-end developer\n3: full-stack developer")
        if user_class in ["1", "2", "3"]:
            break
    if user_class == "1":
        user_class = "front_end_developer"
    elif user_class == "2":
        user_class = "back_end_developer"
    elif user_class == "3":
        user_class = "full_stack_developer"

    return user_class
