"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def get_user_choice():
    """
    Receive the direction user wants to go

    This function let user choose the direction they want to go and return the direction

    :postcondition: only valid user input is accepted
    :return: the direction user chose to go stored as string
    :raises ValueError: if user input is not suggested direction
    """

    movements = {"1": "north", "2": "east", "3": "south", "4": "west",
                 "n": "north", "e": "east", "s": "south", "w": "west",
                 "north": "north", "east": "east", "south": "south", "west": "west"}

    while True:
        user_choice = input("Where do you wish to go?\n1: North\n2: East\n3: South\n4: West\n").strip().lower()
        try:
            return movements[user_choice]
        except KeyError:
            raise ValueError("Invalid input\nTry again")


def main():
    print(get_user_choice())


if __name__ == '__main__':
    main()
