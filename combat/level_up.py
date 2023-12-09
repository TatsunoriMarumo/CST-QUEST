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


def change_job(character):
    character_level = character["level"]
    if character_level == 2:
        character["job"] = "average student"
    elif character_level == 3:
        character["job"] = "honor student"
    elif character_level == 4:
        character["job"] = "junior developer"
    elif character_level == 5:
        character["job"] = "middle developer"
    elif character_level == 6:
        character["job"] = "senior developer"
    return


def main():
    pass


if __name__ == '__main__':
    main()
