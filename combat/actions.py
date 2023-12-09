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


def determine_player_attack_type():
    possible_player_actions = {"1": "light_attack", "2": "heavy_attack"}
    player_action = input(f"What action would you like to perform? "
                          f"Please use please use integers 1 to 4, inclusive, to perform an action.\n\n"
                          f"1: Light Attack\n"
                          f"2: Heavy Attack\n"
                          f"Your choice: ").strip()
    try:
        return possible_player_actions[player_action]
    except KeyError:
        raise KeyError("Not a valid action, please use integers 1 to 2, inclusive, to perform an action.")
