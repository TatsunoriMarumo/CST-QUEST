"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
import io
from instance_display import display_character_stats


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_character_stats_back_end_developer(self, mock_output):
        character = {'status': {'max_hp': 20, 'current_hp': 5,
                                'intelligence': {'value': 10, 'turn_count': 0},
                                'mental_fortitude': {'value': 5, 'turn_count': 0},
                                'typing_speed': {'value': 5, 'turn_count': 0},
                                'luck': {'value': 5, 'turn_count': 0}}}
        display_character_stats(character)
        actual = mock_output.getvalue()
        expected = ("\nH(ope for coo)P: 5/20\n"
                    "Intelligence(attack): 10\n"
                    "Mental Fortitude(defense): 5\n"
                    "Typing Speed(speed): 5\n"
                    "Luck: 5\n\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_character_stats_front_end_developer(self, mock_output):
        character = {'status': {'max_hp': 10, 'current_hp': 8,
                                'intelligence': {'value': 5, 'turn_count': 0},
                                'mental_fortitude': {'value': 5, 'turn_count': 0},
                                'typing_speed': {'value': 10, 'turn_count': 0},
                                'luck': {'value': 5, 'turn_count': 0}}}
        display_character_stats(character)
        actual = mock_output.getvalue()
        expected = ("\nH(ope for coo)P: 8/10\n"
                    "Intelligence(attack): 5\n"
                    "Mental Fortitude(defense): 5\n"
                    "Typing Speed(speed): 10\n"
                    "Luck: 5\n\n")
        self.assertEqual(actual, expected)
