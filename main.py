"""
First sentence.

Second optional sentence.

:param:
:precondition:
:post condition:
:return:
:raises ValueError:
"""
from combat import actions, changing_character_stats, inventory, level_up
from creation import character_creation, foe, game_board
from display import instance_display, introduce_story
from event import encounter
from quiz import quiz_comp_1510
import sys


def main():
    introduce_story.story_introduction()
    character = character_creation.create_character()
    game_map = game_board.create_board()
    while True:
        instance_display.display_board(game_map, character)
        instance_display.describe_room(game_map, character)
        return


if __name__ == '__main__':
    main()
