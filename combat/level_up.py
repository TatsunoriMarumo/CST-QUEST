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


def add_skill(character: dict):
    character_level = character["level"]
    character_class = character["class"]
    if character_level == 2:
        if character_class == "front_end_developer":
            character["skills"].append("console.log")
        elif character_class == "back_end_developer":
            character["skills"].append('print("Hello World")')
        else:
            character["skills"].append('print("Hello World")')

    elif character_level == 3:
        if character_class == "front_end_developer":
            character["skills"].append("margin: auto")
        elif character_class == "back_end_developer":
            character["skills"].append("spread like bacteria")
        else:
            character["skills"].append('status(200)')

    elif character_level == 4:
        if character_class == "front_end_developer":
            character["skills"].append("display: flex")
        elif character_class == "back_end_developer":
            character["skills"].append("roll a die")
        else:
            character["skills"].append("try except")

    elif character_level == 5:
        if character_class == "front_end_developer":
            character["skills"].append("addEventListener")
        elif character_class == "back_end_developer":
            character["skills"].append("try except")
        else:
            character["skills"].append("git stash")

    elif character_level == 6:
        if character_class == "front_end_developer":
            character["skills"].append("github copilot")
        elif character_class == "back-end-developer":
            character["skills"].append("give a chocolate")
        else:
            character["skills"].append("implement API")


def main():
    pass


if __name__ == '__main__':
    main()
