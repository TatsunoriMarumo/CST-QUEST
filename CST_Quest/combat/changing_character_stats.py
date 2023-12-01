"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def calculate_hp_loss(attacking, attack_type, defending):
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
    for item in item:
        character_instance[f"status"][f"{item['buff']['value']}"] += item[f"value"]
        character_instance[f"status"][f"{item['buff']['count']}"] += item[f"count"]
        return character_instance


def heal_character_with_item(character, item):
    character[f"status"][f"{item['heal']}"] += item[f"value"]


def heal_character_with_block(character):
    character[f"status"][f"current_hp"] += 2


def decrement_buff_count(character_instance):
    possible_buffs = {character_instance["status"].fromkeys("intelligence", "luck", "typing_speed", "mentality")}
    for status in possible_buffs:
        if character_instance[f"{status}"][f"count"] == 0:
            continue
        else:
            character_instance[f"{status}"][f"count"] -= 1
