"""
First sentence.

Second optional sentence.

:param:
:precondition:
:post condition:
:return:
:raises ValueError:
"""
from creation import character_creation, game_board
from display import instance_display, introduce_story


def main():
    introduce_story.story_introduction()
    character = character_creation.create_character()
    game_map = game_board.create_board()
    while True:
        instance_display.display_board(game_map, character)
        instance_display.describe_room(game_map, character)


if __name__ == '__main__':
    main()
