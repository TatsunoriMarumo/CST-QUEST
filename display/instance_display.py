"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from creation.game_board import create_board
from creation.character_creation import create_character


def display_character_details(character):
    """
    Print a brief summary of character details.

    Print the class, current hp, and stats.

    :param character: is a dictionary with key-value pairs that represent character details
    :precondition character: must be a dictionary with key-value pairs that represent character details
    :postcondition: print a brief summary of a characters class, current hp, and stats
    :return: None
    """
    character_class = character["class"].replace("_", " ")
    character_job = character["job"]
    character_level = character["level"]
    character_experience = character["exp"]
    inventory = character["inventory"]
    skills = character["skills"]
    print(f"\nCharacter Class: {character_class}\nCharacter Job: {character_job}\n"
          f"Character Level: {character_level}\nCharacter Experience: {character_experience}\n"
          f"Inventory: {inventory}\nSkills: {skills}")


def display_character_stats(character):
    """
    Print a summary of character stats.

    Print a character's individual stat values.

    :param character: is a dictionary with key-value pairs of 'status' and character stats
    :precondition character: must be a dictionary with key-value pairs of 'status' and character stats
    :postcondition: print a brief summary of a characters current stats
    :return: None
    """
    current_hp = character["status"]["current_hp"]
    max_hp = character["status"]["max_hp"]
    intelligence = character["status"]["intelligence"]["value"]
    mental_fortitude = character["status"]["mental_fortitude"]["value"]
    typing_speed = character["status"]["typing_speed"]["value"]
    luck = character["status"]["luck"]["value"]
    print(f"\nH(ope for coo)P: {current_hp}/{max_hp}\n"
          f"Intelligence(attack): {typing_speed}\nMental Fortitude(defense): {mental_fortitude}\n"
          f"Typing Speed(speed): {intelligence}\nLuck: {luck}\n")


def display_board(game_board, character):
    visual_board = {}
    character_coordinates = (character['coordinates'][0], character['coordinates'][1])
    boss_room_coordinates = (6, 6)
    for item in game_board:
        visual_board[item] = False
    visual_board[character_coordinates] = True
    visual_board[boss_room_coordinates] = True
    for row in range(13):
        for column in range(13):
            if not visual_board[row, column]:
                print("[ ]", end=" ")
            else:
                print("[*]", end=" ")
        print()


def describe_room(character, game_board):
    room_descriptions_pool = {0: "placeholder", 1: "placeholder", 2: "placeholder", 3: "placeholder", 4: "placeholder"}
    room_key = game_board[character["coordinates"]]
    print(room_descriptions_pool[room_key])


def main():
    display_character_stats(create_character())


if __name__ == "__main__":
    main()
