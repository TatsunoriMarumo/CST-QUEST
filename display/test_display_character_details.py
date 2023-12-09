"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from unittest.mock import patch
import io
from instance_display import display_character_details


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_character_details_tommy(self, mock_output):
        character = {"name": "Tommy", "class": "front_end_developer", "job": "struggling student",
                     "level": 1, "exp": 0,
                     "inventory": [], "skills": ["control C and V"]}
        display_character_details(character)
        actual = mock_output.getvalue()
        print(actual)
        expected = ("\nCharacter Class: front end developer"
                    "\nCharacter Job: struggling student"
                    "\nCharacter Level: 1"
                    "\nCharacter Experience: 0"
                    "\nInventory: []"
                    "\nSkills: ['control C and V']\n")
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_character_details_matthew(self, mock_output):
        character = {"name": "Matthew", "class": "full_stack_developer", "job": "struggling student",
                     "level": 3, "exp": 21,
                     "inventory": [], "skills": ["control C and V"]}
        display_character_details(character)
        actual = mock_output.getvalue()
        expected = ("\nCharacter Class: full stack developer"
                    "\nCharacter Job: struggling student"
                    "\nCharacter Level: 3"
                    "\nCharacter Experience: 21"
                    "\nInventory: []"
                    "\nSkills: ['control C and V']\n")
        self.assertEqual(actual, expected)
