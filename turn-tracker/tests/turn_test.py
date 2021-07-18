import unittest

from project import turn
from project.player import Player


class Turn(unittest.TestCase):

    def test_get_next_player(self):
        players = [Player("Jhon", "1990-04-03", True, 1, True),
                   Player("Robert", "1986-08-13", True, 2, False),
                   Player("Mary", "1985-11-07", False, 3, False),
                   Player("Patricia", "1991-05-14", False, 4, False),
                   Player("Taylor", "1989-04-23", False, 5, False)]
        self.assertEqual(turn.next_player(players), Player("Jhon", "1990-04-03", True, 1, True))
