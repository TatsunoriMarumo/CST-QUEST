"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import actions
import changing_character_stats
import level_up
from creation import create_foe


def run_combat(character):
    foe = create_foe.assign_foe(character)
    print(f"A {foe['name']} appeared!!")
    while True:
        player_action = actions.determine_player_attack_type()
        foe_action = actions.determine_foe_action(foe)
        if player_action == "skill":
            actions.display_skills(character)
            player_choice_skill = actions.get_user_skill_choice(character)
            if player_choice_skill == str(len(character["skills"]) + 1):
                player_action = actions.determine_player_attack_type()
        first_turn = actions.determine_turn_order(character, foe)
        if first_turn == character:
            if player_action == "block":
                changing_character_stats.heal_character_with_block(character)
            else:
                damage = changing_character_stats.calculate_damage(character, player_action, foe)
                changing_character_stats.calculate_hp_loss(foe, damage)
                changing_character_stats.display_damage(foe, damage)

            if changing_character_stats.check_death(foe):
                print(f"You win!\nYou got {foe['exp']}")
                character["exp"] += foe["exp"]
                break

            if foe_action == "block":
                changing_character_stats.heal_character_with_block(foe)
            else:
                damage = changing_character_stats.calculate_damage(foe, foe_action, character)
                changing_character_stats.calculate_hp_loss(damage, foe)
                changing_character_stats.display_damage(damage, foe)

            if changing_character_stats.check_death(character):
                print("You died")
                break

        elif first_turn == foe:
            if foe_action == "block":
                changing_character_stats.heal_character_with_block(foe)
            else:
                changing_character_stats.calculate_damage(foe, foe_action, character)

            if changing_character_stats.check_death(character):
                print("You died")
                break

            if player_action == "block":
                changing_character_stats.heal_character_with_block(character)
            else:
                changing_character_stats.calculate_damage(character, player_action, foe)

            if changing_character_stats.check_death(foe):
                print(f"You win!\nYou got {foe['exp']}")
                character["exp"] += foe["exp"]
                break
    return


def combat_with_boss(character):
    boss = create_foe.assign_boss(character)
    print("⚠️⚠️⚠️⚠️You have reached the required level to fight the BOSS!⚠️⚠️⚠️⚠️")
    print(f"⚠️⚠️⚠️⚠️Battle with {boss['name']}!!⚠️⚠️⚠️⚠️")
