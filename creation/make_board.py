"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def make_board():
    """
    Create a virtual game board.

    :postcondition: create a dictionary that represents a virtual game board
    :return: a dictionary that represents a virtual game board
    """

    game_board = {(row, column): random.randint(0, 4) for row in range(11) for column in range(11)}
    return game_board


def main():
    print(make_board())


if __name__ == "__main__":
    main()
