"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def determine_foe_action(foe):
    if foe["stats"]["current_hp"] == foe["stats"]["max_hp"]:
        attack_type = ("light_attack", "heavy_attack")
        foe_action = random.choice(range(1, 100))
        if foe_action > 70:
            return attack_type[1]
        else:
            return attack_type[0]
    else:
        action_type = ("light_attack", "heavy_attack", "block")
        foe_action = random.choice(range(100))
        if foe_action > 80:
            return action_type[2]
        elif 60 < foe_action < 80:
            return action_type[1]
        else:
            return action_type[0]
