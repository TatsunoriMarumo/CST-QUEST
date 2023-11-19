"""
Tatsunori Marumo
A01327744
"""


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

    location = {"X-coordinate": character["coordinates"][0], "Y-coordinate": character["coordinates"][1]}

    if direction == "north" and location["Y-coordinate"] == 0:
        return False
    elif direction == "west" and location["X-coordinate"] == 0:
        return False
    elif direction == "south" and location["Y-coordinate"] >= sorted(board.keys())[-1][1]:
        return False
    elif direction == "east" and location["X-coordinate"] >= sorted(board.keys())[-1][2]:
        return False
    else:
        return True


def main():
    pass


if __name__ == '__main__':
    main()

