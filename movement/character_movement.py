"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import copy


def get_user_choice():
    """
    Prompts the player to choose direction.

    Prompts the player to choose a cardinal direction.

    :postcondition: valiate player's chosen cardinal direction
    :return: a string representing the player's chosen cardinal direction
    :raises ValueError: if player's input is not valid
    """
    movements = {"1": "north", "2": "east", "3": "south", "4": "west",
                 "n": "north", "e": "east", "s": "south", "w": "west",
                 "north": "north", "east": "east", "south": "south", "west": "west"}

    while True:
        user_choice = input("Where do you wish to go?\n1: North\n2: East\n3: South\n4: West\n").strip().lower()
        try:
            return movements[user_choice]
        except KeyError:
            raise ValueError("Invalid input\nTry again")


def validate_move(board, character, direction):
    """
    Check if user's movement is valid

    This function checks if user crosses the boundaries of the game board when user moves

    :param board: the game board
    :param character: the character user plays
    :param direction: the direction user wants to go
    :precondition: board must be a dictionary that contains rows and columns as keys
    :precondition: character must be a dictionary that contains X-coordinate and Y-coordinate as keys
    :precondition: direction must be north, east, south, or west stored as string
    :postcondition: board and character are not modified
    :return: True if user does not cross the boundaries of the game board, False if user does so
    """

    copy_character = copy.deepcopy(character)

    if direction == "north":
        copy_character["coordinates"][0] += -1
    elif direction == "south":
        copy_character["coordinates"][0] += 1
    elif direction == "east":
        copy_character["coordinates"][1] += 1
    else:
        copy_character["coordinates"][1] += -1

    if not (copy_character["coordinates"][0], copy_character["coordinates"][1]) in board:
        raise ValueError("You cannot go that way")

    return (copy_character["coordinates"][0], copy_character["coordinates"][1]) in board


def move_character(character, user_choice):
    """

    :param character:
    :param user_choice:
    :return:
    """
    if user_choice == "north":
        character["coordinates"][0] += -1
    elif user_choice == "south":
        character["coordinates"][0] += 1
    elif user_choice == "east":
        character["coordinates"][1] += 1
    else:
        character["coordinates"][1] += -1
    return character
