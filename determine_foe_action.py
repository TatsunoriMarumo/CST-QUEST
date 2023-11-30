"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def determine_foe_action(foe):
    if foe["stats"]["current_hp"] == foe["stats"]["max_hp"]:
        foe_actions = {"1": "light_attack", "2": "heavy_attack"}
        foe_action = str(random.choice(range(1, 3)))
        return foe_actions[foe_action]
    else:
        foe_actions = {"1": "light_attack", "2": "heavy_attack", "3": "block"}
        foe_action = str(random.choice(range(1, 4)))
        return foe_actions[foe_action]
