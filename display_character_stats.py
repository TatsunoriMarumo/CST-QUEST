"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def display_character_stats(character):
    user_class = character["class"]
    current_hp = character["current_hp"]
    max_hp = character["max_hp"]
    typing_speed = character["status"]["typing_speed"]
    mentality = character["status"]["mentality"]
    intelligence = character["status"]["intelligence"]
    luck = character["status"]["luck"]
    print(f"User Class: {user_class}\nH(ope for coo)P: {current_hp}/{max_hp}\n"
          f"Typing Speed(attack):{typing_speed}\nMentality(defense): {mentality}\n"
          f"Intelligence(speed): {intelligence}\nLuck: {luck}")
