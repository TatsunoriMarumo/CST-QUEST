"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def get_username():
    user_name = input("enter your name: ")
    if not user_name:
        raise ValueError("username cannot be blank")
    else:
        return user_name


def main():
    get_username()


if __name__ == "__main__":
    main()
