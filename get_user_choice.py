"""
Tatsunori Marumo
A01327744
"""


def get_user_choice():
    """
    Receive the direction user wants to go

    This function let user choose the direction they want to go and return the direction

    :postcondition: only valid user input is accepted
    :return: the direction user chose to go stored as string
    :raises ValueError: if user input is not suggested direction
    """

    while True:
        movements = ["north", "east", "south", "west", "1", "2", "3", "4"]
        user_choice = input("Where do you wish to go?\n1: North\n2: East\n3: South\n4: West\n").strip().lower()
        try:
            if user_choice not in movements:
                raise ValueError("Invalid input\nTry again")
            elif user_choice.isdigit():
                return movements[int(user_choice) - 1]
            else:
                return user_choice
        except ValueError as error:
            print(error)


def main():
    get_user_choice()


if __name__ == '__main__':
    main()
