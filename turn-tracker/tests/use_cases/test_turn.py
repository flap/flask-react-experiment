import unittest

from project.domain.player import Player
from project.use_cases.turn import Turn


class TurnTest(unittest.TestCase):
    players = [
        Player(
            name="John Doe",
            date_of_birth="1990-04-03",
            is_associate=True,
            position=1,
            is_host=True
        ),
        Player(
            name="Katherine Ryan",
            date_of_birth="1983-06-30",
            is_associate=True,
            position=2,
            is_host=False
        ),
        Player(
            name="Iliza Shlesinger",
            date_of_birth="1983-02-22",
            is_associate=False,
            position=3,
            is_host=False
        ),
        Player(
            name="Tina Fey",
            date_of_birth="1970-05-18",
            is_associate=False,
            position=4,
            is_host=False
        )]

    turn = Turn(players=players)

    def test_turn_init(self):
        turn = Turn(players=self.players)

        self.assertEqual(turn.players[0], self.players[0])
        self.assertEqual(turn.players[1], self.players[1])
        self.assertEqual(turn.players[2], self.players[2])
        self.assertEqual(turn.players[3], self.players[3])

    def test_current_player(self):
        result = self.turn.current_player()
        self.assertEqual(result, self.players[0])

    def test_end_turn(self):
        result = self.turn.end_turn()
        self.assertEqual(result, Player(name="Katherine Ryan", date_of_birth="1983-06-30",
                                        is_associate=True, position=2, is_host=False))
        self.assertEqual(self.turn.players, [Player(name="Katherine Ryan", date_of_birth="1983-06-30",
                                                    is_associate=True, position=2, is_host=False),
                                             Player(name="Iliza Shlesinger", date_of_birth="1983-02-22",
                                                    is_associate=False, position=3, is_host=False),
                                             Player(name="Tina Fey", date_of_birth="1970-05-18",
                                                    is_associate=False, position=4, is_host=False),
                                             Player(name="John Doe", date_of_birth="1990-04-03",
                                                    is_associate=True, position=1, is_host=True)])

    def test_a_player_skip_turns(self):
        players = [Player(name="Sarah Silverman", date_of_birth="1970-12-01", is_associate=False,
                          position=1, is_host=False),
                   Player(name="Gabriel Iglesias", date_of_birth="1976-07-15", is_associate=False,
                          position=2, is_host=True)]

        turn = Turn(players)

        # sarah turns
        turn.skip()
        turn.end_turn()

        # gabriel turns
        result = turn.end_turn()

        self.assertEqual(result, Player(name="Gabriel Iglesias", date_of_birth="1976-07-15", is_associate=False,
                                        position=2, is_host=True))
        self.assertEqual(turn.players, players)
        self.assertFalse(turn.skipped_players)

    def test_all_players_skip_turns(self):
        players = [Player(name="Sarah Silverman", date_of_birth="1970-12-01", is_associate=False,
                          position=1, is_host=False),
                   Player(name="Gabriel Iglesias", date_of_birth="1976-07-15", is_associate=False,
                          position=2, is_host=True)]

        turn = Turn(players)

        # sarah turns
        turn.skip()
        turn.end_turn()

        # gabriel turns
        turn.skip()
        result = turn.end_turn()

        self.assertEqual(result, Player(name="Sarah Silverman", date_of_birth="1970-12-01", is_associate=False,
                                        position=1, is_host=False))
        self.assertEqual(turn.players, players)
        self.assertFalse(turn.skipped_players)

    def test_player_skip_multiple_turns(self):
        players = [Player(name="Sarah Silverman", date_of_birth="1970-12-01", is_associate=False,
                          position=1, is_host=False),
                   Player(name="Gabriel Iglesias", date_of_birth="1976-07-15", is_associate=False,
                          position=2, is_host=True)]

        turn = Turn(players)

        # sarah turns
        turn.skip()
        turn.skip()
        turn.skip()
        turn.end_turn()

        # gabriel turn
        result = turn.end_turn()

        self.assertEqual(result, Player(name="Gabriel Iglesias", date_of_birth="1976-07-15", is_associate=False,
                                        position=2, is_host=True))
        self.assertEqual(turn.players, players)
        self.assertEqual(turn.skipped_players, [Player(name="Sarah Silverman", date_of_birth="1970-12-01",
                                                       is_associate=False, position=1, is_host=False),
                                                Player(name="Sarah Silverman", date_of_birth="1970-12-01",
                                                       is_associate=False, position=1, is_host=False)])
