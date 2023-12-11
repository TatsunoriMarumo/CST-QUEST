"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import fights
import game_board
import level_up
import character_creation
import changing_character_stats
import introduce_story
import instance_display
import encounter
import character_movement
import quiz_comp_1510
import sys
from instance_display import delayed_print


def game():
    introduce_story.story_introduction()
    character = character_creation.create_character()
    game_map = game_board.create_board()
    instance_display.display_board(game_map, character)
    instance_display.display_character_details(character)
    instance_display.display_character_stats(character)
    while True:
        character_movement.run_movement(character, game_map)
        if encounter.check_encounter():
            encounter_type = encounter.check_encounter_type()
            if encounter_type == "combat":
                fights.run_combat(character)

            elif encounter_type == "quiz":
                quiz_comp_1510.run_quiz(character)
            elif encounter_type == "random_event":
                pass
            else:
                delayed_print("This room seems to be empty...")
        if level_up.check_level_up(character):
            boss_battle = fights.combat_with_boss(character)
            if boss_battle:
                level_up.change_level(character)

        if changing_character_stats.check_death(character):
            delayed_print(f"Game over\n{character['name']} failed the course...")
            break

        if character["level"] > 6:
            final_grade = level_up.calculate_grade(character)
            delayed_print(f"Congratuations!!\n {character['name']} has cleared the game!!\n"
                          f"{character['name']}'s final grade was '{final_grade}'"
                          f"Thank you for playing!")
            break
        instance_display.display_board(game_map, character)
        instance_display.display_character_details(character)
        instance_display.display_character_stats(character)


def main():
    game()


if __name__ == '__main__':
    main()

