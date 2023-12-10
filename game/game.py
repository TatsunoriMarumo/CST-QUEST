"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

from combat import actions, changing_character_stats, inventory, level_up
from creation import character_creation, game_board, foe
from display import instance_display, introduce_story
from movement import encounter, get_user_direction, move_character, validate_move
from quiz import quiz_comp_1510
import sys


def game():
    introduce_story.story_introduction()
    character = character_creation.create_character()
    game_map = game_board.create_board()
    while True:
        instance_display.display_board(game_map, character)

        try:
            player_direction = get_user_direction.get_user_choice()
        except (ValueError, KeyError, IndexError, TypeError) as e:
            print(f"{str(e)}", file=sys.stderr)

        try:
            if validate_move.validate_move(game_map, character, player_direction):
                move_character.move_character(character, player_direction)
                instance_display.describe_room(game_map, character)
        except ValueError as e:
            print(f"{str(e)}", file=sys.stderr)

        if encounter.check_encounter():
            encounter_type = encounter.check_encounter_type()
            encounter.implement_encounter(encounter_type, quiz_comp_1510.run_quiz, quiz_comp_1510.run_quiz, quiz_comp_1510.run_quiz)


def main():
    game()


if __name__ == '__main__':
    main()
