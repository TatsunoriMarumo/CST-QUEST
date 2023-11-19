"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def make_floors():
    """
    Create a virtual game board.
    """

    room_types = ["enemy", "puzzle", "event", "loot"]
    "generate random number, if it is in range, assign room_types[0], room_types[1]"

    number_of_floors = 6
    return {(floor, row, column): f"{random.choice(room_types)} room"
            for floor in range(1, number_of_floors + 1) for row in range(0, 5) for column in range(0, 5)}


print(make_floors())
