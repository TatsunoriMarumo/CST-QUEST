"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
import io
from quiz_comp_1510 import display_result


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_result_intelligence_increased_by_one(self, mock_output):
        answer = True
        display_result(answer)
        actual = mock_output.getvalue()
        expected = "True: Your intelligence has increased by 1\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_result_intelligence_decreased_by_one(self, mock_output):
        answer = False
        display_result(answer)
        actual = mock_output.getvalue()
        expected = "False: Your intelligence has decreased by 1\n"
        self.assertEqual(actual, expected)
