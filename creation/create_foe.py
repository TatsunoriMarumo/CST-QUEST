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
            "stats": {"current_hp": 1, "intelligence": 1, "mental_fortitude": 1,
                      "typing_speed": 1, "luck": 1, "exp": 1}}


def create_foe_year_two():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "year 2 Burnaby campus student",
            "stats": {"current_hp": 3, "intelligence": 3, "mental_fortitude": 3,
                      "typing_speed": 3, "luck": 3, "exp": 3}}


def create_foe_international():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "international Burnaby campus student",
            "stats": {"current_hp": 5, "intelligence": 7, "mental_fortitude": 7,
                      "typing_speed": 3, "luck": 1, "exp": 5}}


def create_foe_elite():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "elite Burnaby campus student",
            "stats": {"current_hp": 7, "intelligence": 7, "mental_fortitude": 7,
                      "typing_speed": 7, "luck": 7, "exp": 7}}


def create_foe_set_rep():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "Burnaby campus set rep",
            "stats": {"current_hp": 10, "intelligence": 10, "mental_fortitude": 10,
                      "typing_speed": 10, "luck": 10, "exp": 10}}


def create_foe_graduate():
    """
    Create a foe, also known as Burnaby campus student

    :postcondition: create a dictionary representing a foe
    :return: a dictionary representing a foe
    """
    return {"name": "Burnaby campus graduate",
            "stats": {"current_hp": 13, "intelligence": 13, "mental_fortitude": 13,
                      "typing_speed": 13, "luck": 13, "exp": 13}}


def create_boss_julian():
    """
    Create a boss, also known as an instructor, Julian

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Julian",
            "stats": {"current_hp": 3, "intelligence": 3, "mental_fortitude": 3,
                      "typing_speed": 3, "luck": 3}}


def create_boss_sam():
    """
    Create a boss, also known as an instructor, Sam

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Sam",
            "stats": {"current_hp": 5, "intelligence": 5, "mental_fortitude": 5,
                      "typing_speed": 5, "luck": 5}}


def create_boss_hoda():
    """
    Create a boss, also known as an instructor, Hoda

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Hoda",
            "stats": {"current_hp": 7, "intelligence": 7, "mental_fortitude": 7,
                      "typing_speed": 7, "luck": 7}}


def create_boss_nabil():
    """
    Create a boss, also known as an instructor, Nabil

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Nabil",
            "stats": {"current_hp": 11, "intelligence": 11, "mental_fortitude": 11,
                      "typing_speed": 11, "luck": 11}}


def create_boss_maryam():
    """
    Create a boss, also known as an instructor, Maryam

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Maryam",
            "stats": {"current_hp": 13, "intelligence": 13, "mental_fortitude": 13,
                      "typing_speed": 13, "luck": 13}}


def create_boss_chris():
    """
    Create a boss, also known as an instructor, Chris

    :postcondition: create a dictionary representing a boss
    :return: a dictionary representing a boss
    """
    return {"name": "Chris",
            "stats": {"current_hp": 17, "intelligence": 17, "mental_fortitude": 17,
                      "typing_speed": 17, "luck": 17}}


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
    elif character["level"] == 5:
        return random.choice([foe_level_four, foe_level_five, foe_level_six])
    else:
        return random.choice([foe_level_five, foe_level_six])


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
