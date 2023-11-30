"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def determine_turn_order(character, foe):
    player_speed = character["stats"]["typing_speed"]
    foe_speed = foe["stats"]["typing_speed"]
    if player_speed > foe_speed:
        return "player"
    else:
        return "foe"
