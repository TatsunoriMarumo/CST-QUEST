"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from character_creation import get_class


class Test(TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_get_class_user_input_is_1(self, _):
        actual = get_class()
        expected = "front_end_developer"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["2"])
    def test_get_class_user_input_is_2(self, _):
        actual = get_class()
        expected = "back_end_developer"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["3"])
    def test_get_class_user_input_is_3(self, _):
        actual = get_class()
        expected = "full_stack_developer"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["4"])
    def test_get_class_user_input_is_invalid(self, _):
        with self.assertRaises(ValueError):
            get_class()
