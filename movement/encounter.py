"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import random


def check_encounter():
    encounter_possibility = 2
    numbers = [number for number in range(encounter_possibility)]
    return random.choice(numbers) == 1


def check_encounter_type():
    random_number = random.randint(1, 6)
    if 1 <= random_number <= 3:
        return "combat"
    elif 4 <= random_number <= 5:
        return "quiz"
    else:
        return "random_event"


def main():
    if check_encounter():
        check_encounter()


if __name__ == '__main__':
    main()
