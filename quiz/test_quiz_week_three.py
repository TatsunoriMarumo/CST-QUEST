"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from quiz_comp_1510 import ask_quiz_week_three


class Test(TestCase):
    @patch("builtins.input", side_effect="!")
    def test_ask_quiz_week_three_invalid_input(self, _):
        with self.assertRaises(ValueError):
            ask_quiz_week_three()

    @patch("builtins.input", side_effect="1")
    def test_ask_quiz_week_three_valid_input_one(self, _):
        actual = ask_quiz_week_three()
        expected = False
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect="2")
    def test_ask_quiz_week_three_valid_input_two(self, _):
        actual = ask_quiz_week_three()
        expected = False
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect="3")
    def test_ask_quiz_week_three_valid_input_three(self, _):
        actual = ask_quiz_week_three()
        expected = True
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect="4")
    def test_ask_quiz_week_three_valid_input_four(self, _):
        actual = ask_quiz_week_three()
        expected = False
        self.assertEqual(actual, expected)
