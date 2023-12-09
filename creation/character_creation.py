"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import sys


def get_username():
    """
    Ask player for their username.

    :postcondition: assign variable to player's selected username
    :return: a string representing the player username
    :raises ValueError: if the user input only contains white space
    """
    user_name = input("Please enter your name:\n")
    if not user_name.strip():
        raise ValueError("Username must contain characters other than white space.")
    else:
        return user_name.strip()


def get_class():
    """
    Ask player to choose their character class.

    :precondition: player has chosen a username
    :postcondition: assign variable to player's selected class
    :return: a string representing the player's selecetd class
    :raises ValueError: if the user input is not 1, 2, or 3
    """
    while True:
        user_class = (input("1: front-end developer\n2: back-end developer\n"
                            "3: full-stack developer\nPlease choose a developer class using numbers: ").strip())

        if user_class not in ["1", "2", "3"]:
            raise ValueError("Invalid input, Please choose a valid class number.")
        if user_class == "1":
            return "front_end_developer"
        elif user_class == "2":
            return "back_end_developer"
        else:
            return "full_stack_developer"


def assign_character_starting_stats(character, character_class):
    """
    Change a character's stats.

    Change a character's stats based on the player's chosen class.

    :param character: is a dictionary
    :param character_class: is a string
    :precondition character: must be a dictionary containing key-value pair of 'status' and a dictionary representing
                             the character's stats
    :precondition user_class: must be a string representing the player's selected class
    :post condition: change a character's stats to specific default starting values based on class
    :return: a dictionary representing the player's character
    """
    if character_class == "front_end_developer":
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": {"value": 5, "turn_count": 0},
                               "mental_fortitude": {"value": 5, "turn_count": 0},
                               "typing_speed": {"value": 10, "turn_count": 0},
                               "luck": {"value": 5, "turn_count": 0}}

    elif character_class == "back_end_developer":
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": {"value": 10, "turn_count": 0},
                               "mental_fortitude": {"value": 5, "turn_count": 0},
                               "typing_speed": {"value": 5, "turn_count": 0},
                               "luck": {"value": 5, "turn_count": 0}}
    else:
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": {"value": 7, "turn_count": 0},
                               "mental_fortitude": {"value": 7, "turn_count": 0},
                               "typing_speed": {"value": 7, "turn_count": 0},
                               "luck": {"value": 7, "turn_count": 0}}
    return character


def create_character():
    while True:
        try:
            user_name = get_username()
        except ValueError as e:
            print("{}".format(str(e)), file=sys.stderr)
        else:
            user_class = get_class()
            character = {"name": user_name, "class": user_class, "level": 1, "exp": 0, "status": None,
                         "coordinates": [0, 0],
                         "inventory": []}

            assign_character_starting_stats(character, user_class)

            return character


def main():
    print(get_class())


if __name__ == '__main__':
    main()
