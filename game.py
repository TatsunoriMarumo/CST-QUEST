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


def game():
    introduce_story.story_introduction()
    character = character_creation.create_character()
    game_map = game_board.create_board()
    instance_display.display_board(game_map, character)
    instance_display.display_character_details(character)
    instance_display.display_character_stats(character)
    while True:
        try:
            player_direction = character_movement.get_user_choice()
        except (ValueError, KeyError, IndexError, TypeError) as e:
            print(f"{str(e)}", file=sys.stderr)
        try:
            if character_movement.validate_move(game_map, character, player_direction):
                character_movement.move_character(character, player_direction)
                instance_display.describe_room(game_map, character)
        except ValueError as e:
            print(f"{str(e)}", file=sys.stderr)

        if encounter.check_encounter():
            encounter_type = encounter.check_encounter_type()
            if encounter_type == "combat":
                fights.run_combat(character)

            elif encounter_type == "quiz":
                quiz_comp_1510.run_quiz(character)
            elif encounter_type == "random_event":
                pass
            else:
                print("This room seems to be empty...")
        if level_up.check_level_up(character):
            boss_battle = fights.combat_with_boss(character)
            if boss_battle:
                level_up.change_level(character)

        if changing_character_stats.check_death(character):
            print(f"Game over\n{character['name']} failed the course...")
            break

        if character["level"] == 6:
            print(f"Congratuations!!\n {character['name']} has cleared the game!!\n"
                  f"Thank you for playing!")
        instance_display.display_board(game_map, character)
        instance_display.display_character_details(character)
        instance_display.display_character_stats(character)


def main():
    game()


if __name__ == '__main__':
    main()

