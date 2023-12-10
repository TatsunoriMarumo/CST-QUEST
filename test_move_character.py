"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from character_movement import move_character


class Test(TestCase):
    def test_move_character_North(self):
        character = {"coordinates": [1, 0]}
        user_choice = "north"
        actual = move_character(character, user_choice)
        expected = {"coordinates": [0, 0]}
        self.assertEqual(actual, expected)

    def test_move_character_East(self):
        character = {"coordinates": [0, 0]}
        user_choice = "east"
        actual = move_character(character, user_choice)
        expected = {"coordinates": [0, 1]}
        self.assertEqual(actual, expected)

    def test_move_character_South(self):
        character = {"coordinates": [0, 0]}
        user_choice = "south"
        actual = move_character(character, user_choice)
        expected = {"coordinates": [1, 0]}
        self.assertEqual(actual, expected)

    def test_move_character_West(self):
        character = {"coordinates": [0, 1]}
        user_choice = "west"
        actual = move_character(character, user_choice)
        expected = {"coordinates": [0, 0]}
        self.assertEqual(actual, expected)

