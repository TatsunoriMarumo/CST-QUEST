"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from quiz_comp_1510 import ask_bonus_quiz


class Test(TestCase):
    @patch("builtins.input", side_effect="!")
    def test_ask_bonus_quiz_invalid_input(self, _):
        with self.assertRaises(ValueError):
            ask_bonus_quiz()

    @patch("builtins.input", side_effect="1")
    def test_ask_bonus_quiz_valid_input_one(self, _):
        actual = ask_bonus_quiz()
        expected = True
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect="2")
    def test_ask_bonus_quiz_valid_input_two(self, _):
        actual = ask_bonus_quiz()
        expected = None
        self.assertEqual(actual, expected)
