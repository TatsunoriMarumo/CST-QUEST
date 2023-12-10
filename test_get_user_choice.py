"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from character_movement import get_user_choice


class Test(TestCase):
    @patch("builtins.input", side_effect=["**@#&$"])
    def test_get_user_choice_invalid_input(self, _):
        with self.assertRaises(ValueError):
            get_user_choice()

    @patch("builtins.input", side_effect=["1"])
    def test_get_user_choice_valid_input_North(self, _):
        actual = get_user_choice()
        expected = "north"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["e"])
    def test_get_user_choice_valid_input_East(self, _):
        actual = get_user_choice()
        expected = "east"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["south"])
    def test_get_user_choice_valid_input_South(self, _):
        actual = get_user_choice()
        expected = "south"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["   WeSt   "])
    def test_get_user_choice_valid_input_with_white_space_and_uppercase(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)
