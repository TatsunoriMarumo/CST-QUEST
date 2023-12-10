"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import actions
import changing_character_stats
import create_foe


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
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            else:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, foe)
                changing_character_stats.calculate_hp_loss(foe, damage)
                changing_character_stats.display_damage(foe, damage)

            if changing_character_stats.check_death(foe):
                print(f"You win!\nYou got {foe['exp']}")
                character["exp"] += foe["exp"]
                break

            if foe_action == "block":
                actions.display_action(foe, foe_action)
                changing_character_stats.heal_character_with_block(foe)
            else:
                actions.display_action(foe, foe_action)
                damage = changing_character_stats.calculate_damage(foe, foe_action, character)
                changing_character_stats.calculate_hp_loss(damage, foe)
                changing_character_stats.display_damage(damage, foe)

            if changing_character_stats.check_death(character):
                print("You died")
                break

        elif first_turn == foe:
            if foe_action == "block":
                actions.display_action(foe, foe_action)
                changing_character_stats.heal_character_with_block(foe)
            else:
                actions.display_action(foe, foe_action)
                damage = changing_character_stats.calculate_damage(foe, foe_action, character)
                changing_character_stats.calculate_hp_loss(character, damage)

            if changing_character_stats.check_death(character):
                print("You died")
                break

            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            else:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, foe)
                changing_character_stats.calculate_hp_loss(foe, damage)

            if changing_character_stats.check_death(foe):
                print(f"You win!\nYou got {foe['exp']}")
                character["exp"] += foe["exp"]
                break
    return


def combat_with_boss(character):
    boss = create_foe.assign_boss(character)
    print("⚠️⚠️⚠️⚠️You have reached the required level to fight the BOSS!⚠️⚠️⚠️⚠️")
    print(f"⚠️⚠️⚠️⚠️Battle with {boss['name']}!!⚠️⚠️⚠️⚠️")
    while True:
        player_action = actions.determine_player_attack_type()
        boss_action = actions.determine_foe_action(boss)
        if player_action == "skill":
            actions.display_skills(character)
            player_choice_skill = actions.get_user_skill_choice(character)
            if player_choice_skill == str(len(character["skills"]) + 1):
                player_action = actions.determine_player_attack_type()
        first_turn = actions.determine_turn_order(character, boss)
        if first_turn == character:
            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            else:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, boss)
                changing_character_stats.calculate_hp_loss(boss, damage)
                changing_character_stats.display_damage(boss, damage)

            if changing_character_stats.check_death(boss):
                print(f"You win!\nYou got {boss['exp']}")
                character["exp"] += boss["exp"]
                break

            if boss_action == "block":
                actions.display_action(boss, boss_action)
                changing_character_stats.heal_character_with_block(boss)
            else:
                actions.display_action(boss, boss_action)
                damage = changing_character_stats.calculate_damage(boss, boss_action, character)
                changing_character_stats.calculate_hp_loss(damage, boss)
                changing_character_stats.display_damage(damage, boss)

            if changing_character_stats.check_death(character):
                print("You died")
                break

        elif first_turn == boss:
            if boss_action == "block":
                actions.display_action(boss, boss_action)
                changing_character_stats.heal_character_with_block(boss)
            else:
                actions.display_action(boss, boss_action)
                damage = changing_character_stats.calculate_damage(boss, boss_action, character)
                changing_character_stats.calculate_hp_loss(character, damage)

            if changing_character_stats.check_death(character):
                print("You died")
                break

            if player_action == "block":
                actions.display_action(character, player_action)
                changing_character_stats.heal_character_with_block(character)
            else:
                actions.display_action(character, player_action)
                damage = changing_character_stats.calculate_damage(character, player_action, boss)
                changing_character_stats.calculate_hp_loss(boss, damage)

            if changing_character_stats.check_death(boss):
                print(f"You win!\nYou got {boss['exp']}")
                character["exp"] += boss["exp"]
                break
    return


