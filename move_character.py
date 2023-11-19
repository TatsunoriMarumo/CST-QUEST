"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def move_character(character, user_choice):
    if user_choice == "north":
        character["coordinates"][0] += -1
    elif user_choice == "south":
        character["coordinates"][0] += 1
    elif user_choice == "east":
        character["coordinates"][1] += 1
    else:
        character["coordinates"][1] += -1
    return character
