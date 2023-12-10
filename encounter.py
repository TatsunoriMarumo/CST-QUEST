"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import random


def check_encounter():
    """
    Determine if player will encounter something.

    Determine if the player will encounter something after moving rooms, chance for an encounter is 50%.

    :postcondition: Determine if player will encounter something
    :return: None or 1
    """
    encounter_possibility = 2
    numbers = [number for number in range(encounter_possibility)]
    # return random.choice(numbers) == 1
    return True


def check_encounter_type():
    """
    Determine what type of encounter player experiences.

    :postcondition: determine if player will encounter foe, puzzle, random event, or nothing
    :return: if encounter type is nothing, return None, else return a string
    """
    random_number = random.randint(0, 10)
    if 0 <= random_number <= 5:
        return "combat"
    elif 6 <= random_number <= 7:
        return "quiz"
    elif 8 <= random_number <= 9:
        return "random_event"
    else:
        return None


def main():
    if check_encounter():
        check_encounter()


if __name__ == '__main__':
    main()
