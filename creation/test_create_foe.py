"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""
from unittest import TestCase
from foe import create_foe


class Test(TestCase):
    def test_create_foe(self):
        actual = create_foe()
        expected = {"name": "year 1 Burnaby campus student",
                    "stats": {"current_hp": 1, "intelligence": 1, "mental_fortitude": 1,
                              "typing_speed": 1, "luck": 1}}
