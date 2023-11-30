"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
import random


def determine_encounter():
    encounter_type = {0: "no encounter", 1: "enemy", 2: "puzzle", 3: "buff/debuff"}
    if random.choice(range(1, 5)) == 1:
        return encounter_type[1]
    elif random.choice(range(1, 5)) == 2:
        return encounter_type[2]
    elif random.choice(range(1, 5)) == 3:
        return encounter_type[3]
    else:
        return encounter_type[0]


def main():
    print(determine_encounter())


if __name__ == "__main__":
    main()
