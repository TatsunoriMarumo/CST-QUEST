"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from CST_Quest.creation import make_character, make_floor


def display_board(game_board, character):
    visual_board = {}
    character_coordinates = (character['coordinates'][0], character['coordinates'][1])
    boss_room_coordinates = (6, 6)
    for item in game_board:
        visual_board[item] = False
    visual_board[character_coordinates] = True
    visual_board[boss_room_coordinates] = True
    for row in range(13):
        for column in range(13):
            if not visual_board[row, column]:
                print("[ ]", end=" ")
            else:
                print("[*]", end=" ")
        print()


def main():
    character = make_character.create_character()
    game_board = make_floor.make_board()
    display_board(game_board, character)


if __name__ == "__main__":
    main()
