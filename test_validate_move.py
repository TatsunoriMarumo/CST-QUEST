"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from character_movement import validate_move


class Test(TestCase):
    def test_validate_move_valid_movement_North(self):
        board = {(1, 0): 1, (0, 0): 1}
        character = {"coordinates": [1, 0]}
        direction = "north"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_valid_movement_East(self):
        board = {(0, 0): 1, (0, 1): 1}
        character = {"coordinates": [0, 0]}
        direction = "east"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_valid_movement_South(self):
        board = {(0, 0): 1, (1, 0): 1}
        character = {"coordinates": [0, 0]}
        direction = "south"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_valid_movement_West(self):
        board = {(0, 1): 1, (0, 0): 1}
        character = {"coordinates": [0, 1]}
        direction = "west"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(actual, expected)
