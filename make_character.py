from choose_class import choose_class

"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def create_character():
    user_name = input("enter your name")
    user_class = choose_class()
    if user_class == "front_end_developer":
        character = {"name": user_name, "class": user_class, "level": 1, "status": {}, "coordinates": [0, 0],
                     "inventory": []}
    elif user_class == "back_end_developer":
        character = {"name": user_name, "class": user_class, "level": 1, "status": {}, "coordinates": [0, 0],
                     "inventory": []}
    else:
        character = {"name": user_name, "class": user_class, "level": 1, "status": {}, "coordinates": [0, 0],
                     "inventory": []}

    return character
