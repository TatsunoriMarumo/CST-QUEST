"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from encounter import check_encounter


class Test(TestCase):
    @patch("random.choice", return_value=1)
    def test_check_encounter_returns_integer_one(self, _):
        actual = check_encounter()
        expected = 1
        self.assertEqual(actual, expected)

    @patch("random.choice", return_value=0)
    def test_check_encounter_returns_integer_two(self, _):
        actual = check_encounter()
        expected = 0
        self.assertEqual(actual, expected)
