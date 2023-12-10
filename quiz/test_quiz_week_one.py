"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from quiz_comp_1510 import ask_quiz_week_one


class Test(TestCase):
    @patch("builtins.input", side_effect="_")
    def test_ask_quiz_week_one_invalid_input(self, _):
        with self.assertRaises(ValueError):
            ask_quiz_week_one()

    @patch("builtins.input", side_effect="1")
    def test_ask_quiz_week_one_valid_input_one(self, _):
        actual = ask_quiz_week_one()
        expected = None
        self.assertEqual(actual, expected)