"""
Tatsunori Marumo
A01327744
"""
import copy


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


def main():
    pass


if __name__ == '__main__':
    main()

