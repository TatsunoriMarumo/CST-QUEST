"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def create_board():
    """
    Create a virtual game board.

    :postcondition: create a dictionary that represents a virtual game board
    :return: a dictionary that represents a virtual game board
    """

    game_board = {(row, column): random.randint(0, 4) for row in range(13) for column in range(13)}
    return game_board


def main():
    print(create_board())


if __name__ == "__main__":
    main()
