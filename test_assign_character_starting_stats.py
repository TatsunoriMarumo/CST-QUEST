"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from character_creation import assign_character_starting_stats


class Test(TestCase):
    def test_assign_character_starting_stats_class_is_front_end_developer(self):
        user_class = "front_end_developer"
        a_front_end_character = {}
        actual = assign_character_starting_stats(a_front_end_character, user_class)
        expected = {"status": {"max_hp": 10, "current_hp": 10,
                               "intelligence": {"value": 5, "turn_count": 0},
                               "mental_fortitude": {"value": 5, "turn_count": 0},
                               "typing_speed": {"value": 10, "turn_count": 0},
                               "luck": {"value": 5, "turn_count": 0}}}
        self.assertEqual(actual, expected)

    def test_assign_character_starting_stats_class_is_back_end_developer(self):
        user_class = "back_end_developer"
        a_back_end_developer = {}
        actual = assign_character_starting_stats(a_back_end_developer, user_class)
        expected = {"status": {"max_hp": 10, "current_hp": 10,
                               "intelligence": {"value": 10, "turn_count": 0},
                               "mental_fortitude": {"value": 5, "turn_count": 0},
                               "typing_speed": {"value": 5, "turn_count": 0},
                               "luck": {"value": 5, "turn_count": 0}}}
        self.assertEqual(actual, expected)

    def test_assign_character_starting_stats_class_is_full_stack_developer(self):
        user_class = "full_stack_developer"
        a_full_stack_developer = {}
        actual = assign_character_starting_stats(a_full_stack_developer, user_class)
        expected = {"status": {"max_hp": 10, "current_hp": 10,
                               "intelligence": {"value": 7, "turn_count": 0},
                               "mental_fortitude": {"value": 7, "turn_count": 0},
                               "typing_speed": {"value": 7, "turn_count": 0},
                               "luck": {"value": 7, "turn_count": 0}}}
        self.assertEqual(actual, expected)

