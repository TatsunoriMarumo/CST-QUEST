"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import sys


def get_username():
    user_name = input("enter your name:\n")
    if not user_name:
        raise ValueError("username cannot be blank")
    else:
        return user_name


def choose_class():
    """
    Let player choose a class

    This function ask player to choose one class from three classes

    postcondition: no invalid input is accepted
    :return: the chosen user class stored as string
    :raises ValueError: if user input is not string 1, 2 ,or 3
    """
    while True:
        try:
            user_class = (input("choose a class\n1: front-end developer\n2: back-end developer\n3: full-stack developer\n")
                          .strip())

            if user_class not in ["1", "2", "3"]:
                raise ValueError("Invalid input: Please choose a valid class number")
            if user_class == "1":
                return "front_end_developer"
            elif user_class == "2":
                return "back_end_developer"
            elif user_class == "3":
                return "full_stack_developer"
        except ValueError as e:
            print("{}".format(str(e)), file=sys.stderr)


def assign_character_starting_stats(character, user_class):
    if user_class == "front_end_developer":
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": 5, "luck": 5, "typing_speed": 10, "mentality": 5}
    elif user_class == "back_end_developer":
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": 10, "luck": 5, "typing_speed": 5, "mentality": 5}
    else:
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": 7, "luck": 7, "typing_speed": 7, "mentality": 7}
    return character


def create_character():
    while True:
        try:
            user_name = get_username()
        except ValueError as e:
            print("{}".format(str(e)), file=sys.stderr)
        else:
            user_class = choose_class()
            character = {"name": user_name, "class": user_class, "level": 1, "exp": 0, "stats": None, "coordinates": [0, 0],
                         "inventory": []}

            assign_character_starting_stats(character, user_class)

            return character


def main():
    print(create_character())


if __name__ == '__main__':
    main()
