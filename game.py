"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

from combat import fights, changing_character_stats, inventory, level_up
from creation import character_creation, game_board, create_foe
from display import instance_display, introduce_story
from movement import character_movement, encounter
from quiz import quiz_comp_1510
import sys


def game():
    introduce_story.story_introduction()
    character = character_creation.create_character()
    game_map = game_board.create_board()
    instance_display.display_board(game_map, character)
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


def main():
    game()


if __name__ == '__main__':
    main()

