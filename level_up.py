"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

from instance_display import delayed_print


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


def increase_status(character):
    increase_amount = character["level"]
    for key, value in character["status"].items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if sub_key != "turn_count":
                    character["status"][key][sub_key] += increase_amount
        elif key in ["max_hp", "current_hp"]:
            character["status"][key] += increase_amount


def add_skill(character: dict):
    character_level = character["level"]
    character_class = character["class"]
    if character_level == 2:
        if character_class == "front_end_developer":
            character["skills"]["2"] = "console.log"
        elif character_class == "back_end_developer":
            character["skills"]["2"] = 'print("Hello World")'
        else:
            character["skills"]["2"] = 'print("Hello World")'

    elif character_level == 3:
        if character_class == "front_end_developer":
            character["skills"]["3"] = "margin: auto"
        elif character_class == "back_end_developer":
            character["skills"]["3"] = "spread like bacteria"
        else:
            character["skills"]["3"] = 'status(200)'

    elif character_level == 4:
        if character_class == "front_end_developer":
            character["skills"]["4"] = "display: flex"
        elif character_class == "back_end_developer":
            character["skills"]["4"] = "roll a die"
        else:
            character["skills"]["4"] = "try except"

    elif character_level == 5:
        if character_class == "front_end_developer":
            character["skills"]["5"] = "addEventListener"
        elif character_class == "back_end_developer":
            character["skills"]["5"] = "try except"
        else:
            character["skills"]["5"] = "git stash"

    elif character_level == 6:
        if character_class == "front_end_developer":
            character["skills"]["6"] = "github copilot"
        elif character_class == "back-end-developer":
            character["skills"]["6"] = "give a chocolate"
        else:
            character["skills"]["6"] = "implement API"


def change_level(character):
    if check_level_up(character):
        level_up(character)
        delayed_print(f"you have leveled up!\nYou became level{character['level']}!")
        increase_status(character)
        add_skill(character)
        delayed_print(f"Wow! {character['name']} has learned {character['skills'][character['level']]}!")
        change_job(character)
        delayed_print(f"Congratulations!\nNow {character['name']} became a {character['job']}!")


def main():
    pass


if __name__ == '__main__':
    main()
