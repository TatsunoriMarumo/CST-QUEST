"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def determine_player_action():
    possible_player_actions = {"1": "light_attack", "2": "heavy_attack", "3": "block", "4": "unique_skill"}
    player_action = input(f"What action would you like to perform? "
                          f"Please use please use integers 1 to 4, inclusive, to perform an action.\n\n"
                          f"1: Light Attack\n"
                          f"2: Heavy Attack\n"
                          f"3: Block\n"
                          f"4: Unique Skill\n\n"
                          f"Your choice: ").strip()
    try:
        return possible_player_actions[player_action]
    except KeyError:
        raise KeyError("\nNot a valid action, please use integers 1 to 4, inclusive, to perform an action.")
