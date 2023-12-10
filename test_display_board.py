"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from instance_display import display_board


class Test(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_board_starting_coordinates(self, mock_output):
        character = {"coordinates": [0, 0]}
        game_board = {(row, column): 0 for row in range(13) for column in range(13)}
        display_board(game_board, character)
        actual = mock_output.getvalue()
        expected = ("[*] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [*] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_board(self, mock_output):
        character = {"coordinates": [3, 6]}
        game_board = {(row, column): 0 for row in range(13) for column in range(13)}
        display_board(game_board, character)
        actual = mock_output.getvalue()
        expected = ("[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [*] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [*] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
                    "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n")
        self.assertEqual(actual, expected)
