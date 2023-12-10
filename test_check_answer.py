"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from quiz_comp_1510 import check_answer


class Test(TestCase):
    def test_check_answer_quiz_answer_correct(self):
        character = {"status": {"intelligence": {"value": 1, "count": 0}}}
        answer = True
        actual = check_answer(character, answer)
        # expected = {"status": {"intelligence": {"value": 2, "count": 0}}}
        expected = None
        self.assertEqual(actual, expected)

    def test_check_answer_quiz_answer_incorrect(self):
        character = {"status": {"intelligence": {"value": 1, "count": 0}}}
        answer = False
        actual = check_answer(character, answer)
        # expected = {"status": {"intelligence": {"value": 0, "count": 0}}}
        expected = None
        self.assertEqual(actual, expected)
