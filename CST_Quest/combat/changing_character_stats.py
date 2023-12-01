"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def calculate_attack_vs_defense(attacking, attack_type, defending):
    attack_stat = attacking["stats"]["intelligence"]
    block_stat = defending["stats"]["intelligence"]
    if attack_type == "heavy_attack":
        true_damage = random.choice(range(attack_stat * 1.2 - 3, attack_stat * 1.2)) - block_stat
        if true_damage > 0:
            defending["stats"]["current_hp"] -= true_damage
        else:
            print("Attack was blocked!")
    else:
        true_damage = random.choice(range(attack_stat - 1, attack_stat + 2))
        if true_damage > 0:
            defending["stats"]["current_hp"] -= true_damage
        else:
            print("Attack was blocked!")


def buff_character(character, item):
    character_instance = character.deepcopy()
    character_instance[f"status"][f"{item['buff']}"] += item["value"]
    return character_instance
