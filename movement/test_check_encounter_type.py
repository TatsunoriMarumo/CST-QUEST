"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from encounter import check_encounter_type


class Test(TestCase):
    @patch("random.randint", return_value=1)
    def test_check_encounter_type_is_combat(self, _):
        actual = check_encounter_type()
        expected = "combat"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=3)
    def test_check_encounter_type_is_puzzle(self, _):
        actual = check_encounter_type()
        expected = "quiz"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=5)
    def test_check_encounter_type_is_random_event(self, _):
        actual = check_encounter_type()
        expected = "random_event"
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=7)
    def test_check_encounter_type_is_None(self, _):
        actual = check_encounter_type()
        expected = None
        self.assertEqual(actual, expected)
