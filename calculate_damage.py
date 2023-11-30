"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def calculate_damage(source_entity, source_action, recipient_entity):
    recipient_block = recipient_entity["stats"]["mentality"]
    source_attack = source_entity["stats"]["intelligence"]
    source_defense = source_entity["stats"]["mentality"]
    light_attack_range = random.choice(range(source_attack - 1, source_attack + 2))
    heavy_attack_range = random.choice(range(source_attack * 1.2 - 4, source_defense * 1.2 + 1))
    if source_action == "light_attack":
        recipient_entity["stats"]["current_hp"] -= light_attack_range - recipient_block
    elif source_action == "heavy_attack":
        recipient_entity["stats"]["current_hp"] -= heavy_attack_range - recipient_block
    elif source_action == "unique_skill":
        pass
