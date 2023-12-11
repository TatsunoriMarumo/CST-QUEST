"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import random


def create_foe_year_one():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "year 1 Burnaby campus student",
            "status": {"current_hp": 5, "max_hp": 5, "intelligence": {"value": 3}, "mental_fortitude": {"value": 1},
                       "typing_speed": {"value": 3}, "luck": {"value": 1}, "exp": 1}}


def create_foe_year_two():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "year 2 Burnaby campus student",
            "status": {"current_hp": 7, "max_hp": 7, "intelligence": {"value": 5}, "mental_fortitude": {"value": 3},
                       "typing_speed": {"value": 5}, "luck": {"value": 3}, "exp": 3}}


def create_foe_international():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "international Burnaby campus student",
            "status": {"current_hp": 11, "max_hp": 11, "intelligence": {"value": 7}, "mental_fortitude": {"value": 5},
                       "typing_speed": {"value": 7}, "luck": {"value": 5}, "exp": 5}}


def create_foe_elite():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "elite Burnaby campus student",
            "status": {"current_hp": 13, "max_hp": 13, "intelligence": {"value": 11}, "mental_fortitude": {"value": 7},
                       "typing_speed": {"value": 11}, "luck": {"value": 7}, "exp": 7}}


def create_foe_set_rep():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "Burnaby campus set rep",
            "status": {"current_hp": 17, "max_hp": 17, "intelligence": {"value": 13}, "mental_fortitude": {"value": 11},
                       "typing_speed": {"value": 13}, "luck": {"value": 11}, "exp": 11}}


def create_foe_graduate():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "Burnaby campus graduate",
            "status": {"current_hp": 19, "max_hp": 19, "intelligence": {"value": 17}, "mental_fortitude": {"value": 13},
                       "typing_speed": {"value": 17}, "luck": {"value": 13}, "exp": 13}}


def create_boss_julian():
    """
    Create a boss, also known as an instructor, Julian

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Julian",
            "status": {"current_hp": 7, "max_hp": 7, "intelligence": {"value": 5}, "mental_fortitude": {"value": 5},
                       "typing_speed": {"value": 5}, "luck": {"value": 5}}}


def create_boss_sam():
    """
    Create a boss, also known as an instructor, Sam

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Sam",
            "status": {"current_hp": 11, "max_hp": 11, "intelligence": {"value": 7}, "mental_fortitude": {"value": 5},
                       "typing_speed": {"value": 7}, "luck": {"value": 5}}}


def create_boss_hoda():
    """
    Create a boss, also known as an instructor, Hoda

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Hoda",
            "status": {"current_hp": 13, "max_hp": 13, "intelligence": {"value": 13}, "mental_fortitude": {"value": 11},
                       "typing_speed": {"value": 11}, "luck": {"value": 5}}}


def create_boss_nabil():
    """
    Create a boss, also known as an instructor, Nabil

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Nabil",
            "status": {"current_hp": 17, "max_hp": 17, "intelligence": {"value": 17}, "mental_fortitude": {"value": 13},
                       "typing_speed": {"value": 13}, "luck": {"value": 7}}}


def create_boss_maryam():
    """
    Create a boss, also known as an instructor, Maryam

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Maryam",
            "status": {"current_hp": 19, "max_hp": 19, "intelligence": {"value": 19}, "mental_fortitude": {"value": 17},
                       "typing_speed": {"value": 17}, "luck": {"value": 11}}}


def create_boss_chris():
    """
    Create a boss, also known as an instructor, Chris

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Chris",
            "status": {"current_hp": 23, "max_hp": 23, "intelligence": {"value": 23}, "mental_fortitude": {"value": 23},
                       "typing_speed": {"value": 23}, "luck": {"value": 13}}}


def assign_foe(character):
    foe_level_one = create_foe_year_one()
    foe_level_two = create_foe_year_two()
    foe_level_three = create_foe_international()
    foe_level_four = create_foe_elite()
    foe_level_five = create_foe_set_rep()
    foe_level_six = create_foe_graduate()

    if character["level"] == 1:
        return foe_level_one
    elif character["level"] == 2:
        return random.choice([foe_level_one, foe_level_two, foe_level_three])
    elif character["level"] == 3:
        return random.choice([foe_level_two, foe_level_three, foe_level_four])
    elif character["level"] == 4:
        return random.choice([foe_level_three, foe_level_four, foe_level_five])
    else:
        return random.choice([foe_level_four, foe_level_five, foe_level_six])


def assign_boss(character):
    boss_level_one = create_boss_julian()
    boss_level_two = create_boss_sam()
    boss_level_three = create_boss_hoda()
    boss_level_four = create_boss_nabil()
    boss_level_five = create_boss_maryam()
    boss_level_six = create_boss_chris()

    boss = {1: boss_level_one, 2: boss_level_two, 3: boss_level_three, 4: boss_level_four, 5: boss_level_five,
            6: boss_level_six}

    return boss[character["level"]]
