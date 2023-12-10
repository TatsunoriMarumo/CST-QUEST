"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from instance_display import describe_room


class Test(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_room_board_dictionary_int_value_of_zero(self, mock_output):
        game_board = {(0, 0): 0}
        character = {"coordinates": [0, 0]}
        describe_room(game_board, character)
        actual = mock_output.getvalue()
        expected = ("You enter into a room that is brightly lit and sterile. Large monitors "
                    "periodically decorate the wall along with pods of desks and chair.\nVery strange, "
                    "why would there be a classroom modeled after your BCIT downtown campus room 645 "
                    "in a foreign realm, within a dungeon no less.\nYou're so curious you decide to "
                    "press on and explore.\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_room_board_dictionary_int_value_of_one(self, mock_output):
        game_board = {(0, 0): 1}
        character = {"coordinates": [0, 0]}
        describe_room(game_board, character)
        actual = mock_output.getvalue()
        expected = ("You cautiously enter a old and musty lecture hall. Wait a second, this looks just "
                    "like the archaic lecture hall where your BCIT orientation was held.\nYou think back "
                    "to a time long long ago when you were once a CST Term 1 fledgling, and how glad you "
                    "were that you managed to get into the downtown campus.\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_room_board_dictionary_int_value_of_two(self, mock_output):
        game_board = {(0, 0): 2}
        character = {"coordinates": [0, 0]}
        describe_room(game_board, character)
        actual = mock_output.getvalue()
        expected = ("All of a sudden you are magically thrust into a room lined with brick walls, a "
                    "handful of dimly lit torches, and moss.\nNow this is what a dungeon should look like,"
                    " just kidding, before you can get too excited about being in a real dungeon the\n"
                    "holograms and reflective screens turn off and you find yourself in the BCIT "
                    "downtown campus Tech Hub.\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_room_board_dictionary_int_value_of_three(self, mock_output):
        game_board = {(0, 0): 3}
        character = {"coordinates": [0, 0]}
        describe_room(game_board, character)
        actual = mock_output.getvalue()
        expected = "You enter into what looks like a normal dungeon room.\n"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_room_board_dictionary_int_value_of_four(self, mock_output):
        game_board = {(0, 0): 4}
        character = {"coordinates": [0, 0]}
        describe_room(game_board, character)
        actual = mock_output.getvalue()
        expected = "You cautiously enter a room that is pitch black.\n"
        self.assertEqual(actual, expected)
