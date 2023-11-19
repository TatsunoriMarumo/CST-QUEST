"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def assign_character_starting_stats(character, user_class):
    if user_class == "front_end_developer":
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": 5, "luck": 5, "typing_speed": 10, "mentality": 5}
    elif user_class == "back_end_developer":
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": 10, "luck": 5, "typing_speed": 5, "mentality": 5}
    else:
        character["status"] = {"max_hp": 10, "current_hp": 10,
                               "intelligence": 7, "luck": 7, "typing_speed": 7, "mentality": 7}
    return character
