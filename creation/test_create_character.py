"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from character_creation import create_character


class Test(TestCase):
    @patch("builtins.input", side_effect=[" "])
    def test_create_character_username_invalid(self, _):
        with self.assertRaises(ValueError):
            create_character()

    @patch("builtins.input", side_effect=["Ephraim", "4"])
    def test_create_character_user_class_invalid(self, _):
        with self.assertRaises(ValueError):
            create_character()

    @patch("builtins.input", side_effect=["Tats", "1"])
    def test_create_character_user_is_front_end_developer(self, _):
        actual = create_character()
        expected = {'name': 'Tats', 'class': 'front_end_developer', 'job': 'struggling student', 'level': 1,
                    'exp': 0, 'status': {'max_hp': 10, 'current_hp': 10,
                                         'intelligence': {'value': 5, 'turn_count': 0},
                                         'mental_fortitude': {'value': 5, 'turn_count': 0},
                                         'typing_speed': {'value': 10, 'turn_count': 0},
                                         'luck': {'value': 5, 'turn_count': 0}},
                    'coordinates': [0, 0], 'inventory': []}
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["Anthony", "2"])
    def test_create_character_user_is_back_end_developer(self, _):
        actual = create_character()
        expected = {'name': 'Anthony', 'class': 'back_end_developer', 'job': 'struggling student', 'level': 1,
                    'exp': 0, 'status': {'max_hp': 10, 'current_hp': 10,
                                         'intelligence': {'value': 10, 'turn_count': 0},
                                         'mental_fortitude': {'value': 5, 'turn_count': 0},
                                         'typing_speed': {'value': 5, 'turn_count': 0},
                                         'luck': {'value': 5, 'turn_count': 0}},
                    'coordinates': [0, 0], 'inventory': []}
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["Momo", "3"])
    def test_create_character_user_is_full_stack_developer(self, _):
        actual = create_character()
        expected = {'name': 'Momo', 'class': 'full_stack_developer', 'job': 'struggling student', 'level': 1,
                    'exp': 0, 'status': {'max_hp': 10, 'current_hp': 10,
                                         'intelligence': {'value': 7, 'turn_count': 0},
                                         'mental_fortitude': {'value': 7, 'turn_count': 0},
                                         'typing_speed': {'value': 7, 'turn_count': 0},
                                         'luck': {'value': 7, 'turn_count': 0}},
                    'coordinates': [0, 0], 'inventory': []}
        self.assertEqual(actual, expected)
