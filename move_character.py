"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def move_character(character, user_choice):
    if user_choice == "north":
        character["X-coordinate"] += -1
    elif user_choice == "south":
        character["X-coordinate"] += 1
    elif user_choice == "east":
        character["Y-coordinate"] += 1
    else:
        character["Y-coordinate"] += -1
    return character
