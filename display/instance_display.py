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
          f"Intelligence(attack): {intelligence}\nMental Fortitude(defense): {mental_fortitude}\n"
          f"Typing Speed(speed): {typing_speed}\nLuck: {luck}\n")


def display_board(game_board, character):
    """
    Print a visual representation of the game board.

    Print a visual representation of the game board including boss room location and player's current location.

    :param game_board: is a dictionary with key-value pairs of coordinates and an int
    :param character: is a dictionary with key-value pairs that represent character details
    :precondition game_board: must be a dictionary with key-value pairs of coordinates and an int
    :precondition character: must be a dictionary with key-value pairs that represent character details
    :postcondition: print the game board with boss room location and player's current location
    :return: None
    """
    visual_board = {item: False for item in game_board}
    character_coordinates = (character['coordinates'][0], character['coordinates'][1])
    boss_room_coordinates = (6, 6)
    visual_board[character_coordinates] = True
    visual_board[boss_room_coordinates] = True
    for row in range(13):
        for column in range(13):
            if not visual_board[row, column]:
                print("[ ]", end=" ")
            else:
                print("[*]", end=" ")
        print()


def describe_room(game_board, character):
    """
    Print a description of a room.

    Print a description of a room that the player has just entered.

    :param game_board: is a dictionary with key-value pairs of coordinates and an int
    :param character: is a dictionary with key-value pairs that represent character details
    :precondition game_board: must be a dictionary with key-value pairs of coordinates and an int
    :precondition character: must be a dictionary with key-value pairs that represent character details
    :postcondition: print a brief description of the room player has entered
    :return: None
    """
    room_descriptions_pool = {0: "You enter into a room that is brightly lit and sterile. Large monitors "
                                 "periodically decorate the wall along with pods of desks and chair.\nVery strange, "
                                 "why would there be a classroom modeled after your BCIT downtown campus room 645 "
                                 "in a foreign realm, within a dungeon no less.\nYou're so curious you decide to "
                                 "press on and explore.",
                              1: "You cautiously enter a old and musty lecture hall. Wait a second, this looks just "
                                 "like the archaic lecture hall where your BCIT orientation was held.\nYou think back "
                                 "to a time long long ago when you were once a CST Term 1 fledgling, and how glad you "
                                 "were that you managed to get into the downtown campus.",
                              2: "All of a sudden you are magically thrust into a room lined with brick walls, a "
                                 "handful of dimly lit torches, and moss.\nNow this is what a dungeon should look like,"
                                 " just kidding, before you can get too excited about being in a real dungeon the\n"
                                 "holograms and reflective screens turn off and you find yourself in the BCIT "
                                 "downtown campus Tech Hub.",
                              3: "You enter into what looks like a normal dungeon room.",
                              4: "You cautiously enter a room that is pitch black."}
    room_key = game_board[character["coordinates"][0], character["coordinates"][1]]
    print(room_descriptions_pool[room_key])


def main():
    pass


if __name__ == "__main__":
    main()
