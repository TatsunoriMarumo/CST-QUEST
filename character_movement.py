"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import copy
import sys
import instance_display


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
        except KeyError as e:
            print(f"Invalid input\nTry again {str(e)}", file=sys.stderr)


def validate_move(board, character, direction):
    """
    Validate a player's chosen cardinal direction.

    Determine if a player's chosen cardinal direction is valid based on character position on the board.

    :param board: a dictionary with key-value pairs of coordinates and an integer
    :param character: a dictionary with key-value pairs representing character details
    :param direction: a string representing the player's chosen cardinal direction
    :precondition: must be a dictionary with key-value pairs of coordinates and an integer
    :precondition: must be a dictionary with key-value pairs representing character details
    :precondition: must be a string representing the player's chosen cardinal direction
    :postcondition: determine if a player is allowed to move their character in a chosen direction
    :return: boolean value True
    :raises ValueError: if player's chosen cardinal direction will move the character out of bounds
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
    Move the player's character on the virtual game board

    Change the coordinates of the player's character to the coordinates of the room they have chosen to move into.

    :param character: a dictionary with key-value pairs representing character details
    :param user_choice: a string representing the player's chosen cardinal direction
    :precondition character: must be
    :precondition user_choice: must be
    :postcondition: change the value of the 'coordinates' key in the character dictionary to the new room's location.
    :return: a dictionary representing the player's character
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


def validate_boss_room_level_requirement(character):
    """
    Validate if player can enter boss room.

    :param character: a dictionary with key-pair values that represent character details
    :precondition character: must be a dictionary with key-pair values that represent character details
    :postcondition: validate the character level
    :return: a boolean value representing permission to enter boss room
    """
    if character["leve"] == 6:
        return True
    else:
        print("Level 6 is required to fight the final boss. You are too low level.")
        return False


def run_movement(character, game_board):
    while True:
        player_direction = get_user_choice()
        try:
            if validate_move(game_board, character, player_direction):
                move_character(character, player_direction)
                instance_display.describe_room(game_board, character)
                break
        except ValueError as e:
            print(f"{str(e)}", file=sys.stderr)
