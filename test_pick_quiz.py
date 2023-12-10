"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from quiz_comp_1510 import pick_quiz
from quiz_comp_1510 import ask_quiz_week_one
from quiz_comp_1510 import ask_quiz_week_two
from quiz_comp_1510 import ask_quiz_week_three
from quiz_comp_1510 import ask_quiz_week_four
from quiz_comp_1510 import ask_quiz_week_five
from quiz_comp_1510 import ask_quiz_week_six
from quiz_comp_1510 import ask_quiz_week_seven
from quiz_comp_1510 import ask_quiz_week_eight
from quiz_comp_1510 import ask_quiz_week_nine
from quiz_comp_1510 import ask_quiz_week_ten


class Test(TestCase):
    @patch("random.randint", return_value=0)
    def test_pick_quiz_random_integer_is_zero(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_one
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=1)
    def test_pick_quiz_random_integer_is_one(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_two
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=2)
    def test_pick_quiz_random_integer_is_two(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_three
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=3)
    def test_pick_quiz_random_integer_is_three(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_four
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=4)
    def test_pick_quiz_random_integer_is_four(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_five
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=5)
    def test_pick_quiz_random_integer_is_five(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_six
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=6)
    def test_pick_quiz_random_integer_is_six(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_seven
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=7)
    def test_pick_quiz_random_integer_is_seven(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_eight
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=8)
    def test_pick_quiz_random_integer_is_eight(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_nine
        self.assertEqual(actual, expected)

    @patch("random.randint", return_value=9)
    def test_pick_quiz_random_integer_is_nine(self, _):
        actual = pick_quiz()
        expected = ask_quiz_week_ten
        self.assertEqual(actual, expected)


