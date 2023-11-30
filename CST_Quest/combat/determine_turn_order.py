"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def determine_turn_order(character, foe):
    if character["stats"]["typing_speed"] > foe["stats"]["typing_speed"]:
        return "player"
    elif character["stats"]["typing_speed"] == foe["stats"]["typing_speed"]:
        return random.choice(["player", "foe"])
    else:
        return "foe"
