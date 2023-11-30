"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def create_burnaby_student(character):
    row = character["coordinates"][0]
    column = character["coordinates"][1]
    board_lower_bound = 4
    board_higher_bound = 6
    if board_lower_bound < row < board_higher_bound and board_lower_bound < column < 10:
        return {"name": "year 1 Burnaby campus student",
                "stats": {"max_hp": 1, "current_hp": 1, "intelligence": 1, "luck": 1,
                          "typing_speed": 1, "mentality": 1}}
    else:
        return {"name": "year 1 Burnaby campus student",
                "stats": {"max_hp": 1, "current_hp": 1, "intelligence": 1, "luck": 1,
                          "typing_speed": 1, "mentality": 1}}
