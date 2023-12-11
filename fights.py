"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import actions
import changing_character_stats
import create_foe
from instance_display import delayed_print


def run_combat(character):
    foe = create_foe.assign_foe(character)
    delayed_print(f"A {foe['name']} appeared!!")

    while True:
        player_action = actions.determine_player_attack_type()
        foe_action = actions.determine_foe_action(foe)
        if player_action == "run away":
            if actions.check_run_away(character, foe):
                delayed_print(f"{character['name']} has run away from {foe['name']}!")
                break
            else:
                delayed_print(f"{character['name']} failed to run away\nFace reality...")

        elif player_action == "skill":
            player_choice_skill = actions.get_user_skill_choice(character)
            if player_choice_skill == str(len(character["skills"]) + 1):
                player_action = actions.determine_player_attack_type()
            elif player_choice_skill == str(len(character["skills"])):
                delayed_print(f"{character['name']} uses {character['skills'][player_choice_skill]}!!")
        first_turn = actions.determine_turn_order(character, foe)
        if first_turn == character:
            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            elif player_action in ["light_attack", "heavy_attack", "skill"]:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, foe)
                changing_character_stats.calculate_hp_loss(foe, damage)
                changing_character_stats.display_damage(foe, damage)

            if changing_character_stats.check_death(foe):
                delayed_print(f"You win!\nYou got {foe['status']['exp']} exp")
                character["exp"] += foe["status"]["exp"]
                break

            if foe_action == "block":
                actions.display_action(foe, foe_action)
                changing_character_stats.heal_character_with_block(foe)
            else:
                actions.display_action(foe, foe_action)
                damage = changing_character_stats.calculate_damage(foe, foe_action, character)
                changing_character_stats.calculate_hp_loss(character, damage)
                changing_character_stats.display_damage(character, damage)

            if changing_character_stats.check_death(character):
                delayed_print("You died")
                break

        elif first_turn == foe:
            if foe_action == "block":
                actions.display_action(foe, foe_action)
                changing_character_stats.heal_character_with_block(foe)
            else:
                actions.display_action(foe, foe_action)
                damage = changing_character_stats.calculate_damage(foe, foe_action, character)
                changing_character_stats.calculate_hp_loss(character, damage)
                changing_character_stats.display_damage(character, damage)

            if changing_character_stats.check_death(character):
                delayed_print("You died")
                break

            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            elif player_action in ["light_attack", "heavy_attack", "skill"]:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, foe)
                changing_character_stats.calculate_hp_loss(foe, damage)
                changing_character_stats.display_damage(foe, damage)

            if changing_character_stats.check_death(foe):
                delayed_print(f"You win!\nYou got {foe['status']['exp']} exp")
                character["exp"] += foe["status"]["exp"]
                break
    return


def combat_with_boss(character):
    boss = create_foe.assign_boss(character)
    delayed_print("⚠️⚠️⚠️You have reached the required level to fight the BOSS!⚠️⚠️⚠️")
    delayed_print(f"⚠️⚠️⚠️Battle with {boss['name']}!!⚠️⚠️⚠️")
    while True:
        player_action = actions.determine_player_attack_type()
        boss_action = actions.determine_foe_action(boss)
        if player_action == "run away":
            delayed_print(f"You cannot run away from {boss['name']}!")

        elif player_action == "skill":
            player_choice_skill = actions.get_user_skill_choice(character)

            if player_choice_skill == str(len(character["skills"]) + 1):
                player_action = actions.determine_player_attack_type()
        first_turn = actions.determine_turn_order(character, boss)
        if first_turn == character:
            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            elif player_action in ["light_attack", "heavy_attack", "skill"]:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, boss)
                changing_character_stats.calculate_hp_loss(boss, damage)
                changing_character_stats.display_damage(boss, damage)

            if changing_character_stats.check_death(boss):
                delayed_print(f"{character['name']} win!")
                return True

            if boss_action == "block":
                actions.display_action(boss, boss_action)
                changing_character_stats.heal_character_with_block(boss)
            else:
                actions.display_action(boss, boss_action)
                damage = changing_character_stats.calculate_damage(boss, boss_action, character)
                changing_character_stats.calculate_hp_loss(character, damage)
                changing_character_stats.display_damage(character, damage)

            if changing_character_stats.check_death(character):
                delayed_print("You died")
                break

        elif first_turn == boss:
            if boss_action == "block":
                actions.display_action(boss, boss_action)
                changing_character_stats.heal_character_with_block(boss)
            else:
                actions.display_action(boss, boss_action)
                damage = changing_character_stats.calculate_damage(boss, boss_action, character)
                changing_character_stats.calculate_hp_loss(character, damage)
                changing_character_stats.display_damage(character, damage)

            if changing_character_stats.check_death(character):
                delayed_print("You died")
                return False

            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            elif player_action in ["light_attack", "heavy_attack", "skill"]:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, boss)
                changing_character_stats.calculate_hp_loss(boss, damage)
                changing_character_stats.display_damage(boss, damage)

            if changing_character_stats.check_death(boss):
                delayed_print(f"You win!\n Congratulations! {character['name']} has passed level {character['level']} course!")
                return True
    return
