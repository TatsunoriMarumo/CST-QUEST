"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from character_creation import get_username


class Test(TestCase):
    @patch("builtins.input", side_effect=["ephraim"])
    def test_get_username_input_is_ephraim(self, _):
        actual = get_username()
        expected = "ephraim"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["tatsunori"])
    def test_get_username_input_is_tatsunori(self, _):
        actual = get_username()
        expected = "tatsunori"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["1234"])
    def test_get_username_input_is_numerals(self, _):
        actual = get_username()
        expected = "1234"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["1a2b3c4d"])
    def test_get_username_input_is_numerals_and_roman_alphabet(self, _):
        actual = get_username()
        expected = "1a2b3c4d"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["&)!@$&"])
    def test_get_username_input_is_special_characters(self, _):
        actual = get_username()
        expected = "&)!@$&"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["         "])
    def test_get_username_input_is_all_white_space(self, _):
        with self.assertRaises(ValueError):
            get_username()

