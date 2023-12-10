"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import copy
import random
from instance_display import delayed_print

def calculate_damage(attacking, attack_type, defending):
    attack_stat = attacking["status"]["intelligence"]["value"]
    block_stat = defending["status"]["mental_fortitude"]["value"]
    if attack_type == "heavy_attack":
        true_damage = random.choice(range(round(attack_stat * 0.8), round(attack_stat * 1.2))) - block_stat
        return true_damage
    elif attack_type == "light_attack":
        true_damage = random.choice(range(attack_stat - 2, attack_stat + 2))
        return true_damage
    else:
        skill = attacking["level"]
        true_damage = ((attacking["status"]["luck"]["value"] + random.randint((0 - skill), skill)
                       - (defending["status"]["luck"]["value"] + random.randint((0 - skill), skill))))
        return true_damage


def calculate_hp_loss(defending, true_damage):
    defending["status"]["current_hp"] -= true_damage
    if defending["status"]["current_hp"] < 0:
        defending["status"]["current_hp"] = 0
    return


def display_damage(character, true_damage):
    if true_damage > 0:
        delayed_print(f"{character['name']} got {true_damage} damage!")
        delayed_print(f"{character['name']}'s HP is now {character['status']['current_hp']}/{character['status']['max_hp']}")
    else:
        delayed_print("Attack was blocked!")


def buff_character(character, item):
    character_instance = character.deepcopy()
    for item in item:
        character_instance[f"status"][f"{item['buff']['value']}"] += item[f"value"]
        character_instance[f"status"][f"{item['buff']['count']}"] += item[f"count"]
        return character_instance


def heal_character_with_item(character, item):
    character[f"status"][f"{item['heal']}"] += item[f"value"]


def heal_character_with_block(character):
    heal_amount = round(character["status"]["max_hp"] / 4)
    hp_before_block = character["status"]["current_hp"]
    character["status"]["current_hp"] += heal_amount
    if character["status"]["max_hp"] < character["status"]["current_hp"]:
        character["status"]["current_hp"] = character["status"]["max_hp"]
    hp_after_block = copy.copy(character["status"]["current_hp"])
    heal_amount = hp_after_block - hp_before_block
    delayed_print(f"{character['name']} has healed {heal_amount}!")
    delayed_print(f"{character['name']}'s HP is now {character['status']['current_hp']}/{character['status']['max_hp']}")


def decrement_buff_count(character_instance):
    possible_buffs = {character_instance["status"].fromkeys("intelligence", "luck", "typing_speed", "mentality")}
    for status in possible_buffs:
        if character_instance[f"{status}"][f"count"] == 0:
            continue
        else:
            character_instance[f"{status}"][f"count"] -= 1


def check_death(defending):
    return defending["status"]["current_hp"] <= 0
