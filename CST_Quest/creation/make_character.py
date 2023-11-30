"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from CST_Quest.creation.choose_class import choose_class


def create_character(user_name):
    user_class = choose_class()
    if user_class == "front_end_developer":
        character = {"name": user_name, "class": user_class, "level": 1, "exp": 0,
                     "stats": {"max_hp": 1, "current_hp": 1, "intelligence": 1, "luck": 1,
                               "typing_speed": 1, "mentality": 1},
                     "coordinates": [0, 0], "inventory": []}
    elif user_class == "back_end_developer":
        character = {"name": user_name, "class": user_class, "level": 1, "exp": 0,
                     "stats": {"max_hp": 2, "current_hp": 2, "intelligence": 2, "luck": 2,
                               "typing_speed": 2, "mentality": 2},
                     "coordinates": [0, 0], "inventory": []}
    else:
        character = {"name": user_name, "class": user_class, "level": 1, "exp": 0,
                     "stats": {"max_hp": 3, "current_hp": 3, "intelligence": 3, "luck": 3,
                               "typing_speed": 3, "mentality": 3},
                     "coordinates": [0, 0], "inventory": []}
    return character
