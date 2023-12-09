"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import random


def check_encounter():
    encounter_possibility = 4
    numbers = [number for number in range(encounter_possibility)]
    return random.choice(numbers) == 1


def check_encounter_type():
    return random.choice(["combat", "quiz", "random_event"])


def main():
    if check_encounter():
        check_encounter()


if __name__ == '__main__':
    main()
