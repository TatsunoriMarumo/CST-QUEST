"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def check_level_up(character: dict):
    if character["level"] >= 6:
        return False
    else:
        return character["exp"] > character["level"] * 10


def level_up(character):
    character["level"] += 1
    return


def main():
    pass


if __name__ == '__main__':
    main()
