"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def describe_room(character, game_board):
    room_descriptions_pool = {0: "placeholder", 1: "placeholder", 2: "placeholder", 3: "placeholder", 4: "placeholder"}
    room_key = game_board[character["coordinates"]]
    print(room_descriptions_pool[room_key])


def main():
    pass


if __name__ == "__main__":
    main()
