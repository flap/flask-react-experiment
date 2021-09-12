import unittest
from unittest.mock import patch

from project.domain.player import Player
from project.use_cases.game_session import GameSession
from project.use_cases.turn import Turn


class GameSessionTest(unittest.TestCase):
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

    turn = Turn(players)

    session_name = "A comedianne walks into a bar..."

    session = GameSession(name=session_name)

    session_with_players = GameSession(name=session_name, players=players)

    session_started = GameSession(name=session_name, players=players, turn=turn, started=True)

    session_finished = GameSession(name=session_name, players=players, turn=turn, started=True, finished=True)

    @patch("project.repository.session_repository.save")
    def test_create_session(self, mock_save):
        result = GameSession.create_session(self.session_name)

        mock_save.assert_called_once()
        self.assertEqual(result.name, self.session_name)

    @patch("project.repository.session_repository.update")
    @patch("project.repository.session_repository.find_session_by_name", return_value=GameSession(name=session_name))
    def test_add_players_to_session(self, mock_find_session_by_name, mock_update):
        result = self.session.add_players(self.session_name, self.players)

        mock_find_session_by_name.assert_called_once_with(self.session_name)
        mock_update.assert_called_once()
        self.assertEqual(result.name, self.session_name)
        self.assertEqual(result.players, self.players)

    @patch("project.use_cases.turn.Turn.current_player", return_value=Player(name="John Doe",
                                                                             date_of_birth="1990-04-03",
                                                                             is_associate=True,
                                                                             position=1, is_host=True))
    @patch("project.repository.session_repository.update")
    @patch("project.repository.session_repository.find_session_by_name", return_value=GameSession(name=session_name,
                                                                                                  players=players))
    def test_start_session(self, mock_find_session_by_name, mock_update, mock_get_current_player):
        result = self.session_with_players.start(self.session_name)

        mock_find_session_by_name.assert_called_once_with(self.session_name)
        mock_update.assert_called_once()
        mock_get_current_player.assert_called_once()
        self.assertEqual(result, Player(name="John Doe",
                                        date_of_birth="1990-04-03",
                                        is_associate=True,
                                        position=1, is_host=True))

    @patch("project.repository.session_repository.find_session_by_name", return_value=GameSession(name=session_name))
    def test_raise_BusinessException_when_try_start_session_without_players(self, mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session.start(self.session_name)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.repository.session_repository.update")
    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True))
    def test_finish_session(self, mock_find_session_by_name, mock_update):
        result = self.session_started.finish(self.session_name)

        mock_find_session_by_name.assert_called_once_with(self.session_name)
        mock_update.assert_called_once()
        self.assertEqual(result.name, self.session_name)
        self.assertEqual(result.players, self.players)
        self.assertTrue(result.finished)

    @patch("project.repository.session_repository.find_session_by_name", return_value=GameSession(name=session_name))
    def test_raise_BusinessException_when_try_finish_not_started_session(self, mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session.finish(self.session_name)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.use_cases.turn.Turn.current_player", return_value=Player(name="John Doe",
                                                                             date_of_birth="1990-04-03",
                                                                             is_associate=True,
                                                                             position=1, is_host=True))
    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True))
    def test_get_current_player(self, mock_find_session_by_name, mock_get_current_player):
        result = self.session_started.current_player(self.session_name)

        mock_find_session_by_name.assert_called_once_with(self.session_name)
        mock_get_current_player.assert_called_once()
        self.assertEqual(result, Player(name="John Doe",
                                             date_of_birth="1990-04-03",
                                             is_associate=True,
                                             position=1, is_host=True))

    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players))
    def test_raise_BusinessExcpetion_when_try_get_current_player_before_started_session(self,
                                                                                        mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session_with_players.current_player(self.session_with_players)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True, finished=True))
    def test_raise_BusinessExcpetion_when_try_get_current_player_after_finished_session(self,
                                                                                        mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session_with_players.current_player(self.session_finished)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.use_cases.turn.Turn.end_turn", return_value=Player(name="Katherine Ryan",
                                                                       date_of_birth="1983-06-30",
                                                                       is_associate=True,
                                                                       position=2,
                                                                       is_host=False))
    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True))
    def test_end_turn_and_get_next_player(self, mock_find_session_by_name, mock_end_turn):
        result = self.session_started.end_turn(self.session_name)

        mock_find_session_by_name.assert_called_once_with(self.session_name)
        mock_end_turn.assert_called_once()
        self.assertEqual(result, Player(name="Katherine Ryan",
                                        date_of_birth="1983-06-30",
                                        is_associate=True,
                                        position=2,
                                        is_host=False))

    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players))
    def test_raise_BusinessExcpetion_when_try_get_next_player_before_started_session(self,
                                                                                     mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session_with_players.end_turn(self.session_with_players)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True, finished=True))
    def test_raise_BusinessExcpetion_when_try_get_next_player_after_finished_session(self,
                                                                                     mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session_with_players.end_turn(self.session_finished)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.use_cases.turn.Turn.skip", return_value=turn)
    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True))
    def test_skip_turn(self, mock_find_session_by_name, mock_skip_turn):
        self.session_started.skip_turn(self.session_name)

        mock_find_session_by_name.assert_called_once_with(self.session_name)
        mock_skip_turn.assert_called_once()

    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players))
    def test_raise_BusinessExcpetion_when_try_skip_turn_before_started_session(self,
                                                                               mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session_with_players.skip_turn(self.session_name)
            mock_find_session_by_name.assert_called_once_with(self.session_name)

    @patch("project.repository.session_repository.find_session_by_name",
           return_value=GameSession(name=session_name, players=players, turn=turn, started=True, finished=True))
    def test_raise_BusinessExcpetion_when_try_skip_turn_after_finished_session(self,
                                                                               mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session_with_players.skip_turn(self.session_name)
            mock_find_session_by_name.assert_called_once_with(self.session_name)
