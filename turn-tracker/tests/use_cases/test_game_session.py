import unittest
from unittest.mock import patch

from project.domain.player import Player
from project.use_cases.game_session import GameSession


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

    session = GameSession(name="A comedianne walks into a bar...")

    session_with_players = GameSession(name="A comedianne walks into a bar...",
                                       players=players)

    session_started = GameSession(name="A comedianne walks into a bar...",
                                  players=players,
                                  started=True)

    @patch("project.repository.session_repository.save")
    def test_create_session(self, mock_save):
        result = self.session.create_session(self.session.name)

        mock_save.assert_called_once()
        self.assertEqual(result.name, self.session.name)

    @patch("project.repository.session_repository.update")
    @patch("project.repository.session_repository.find_session_by_name", return_value=session)
    def test_add_players_to_session(self, mock_find_session_by_name, mock_update):
        result = self.session.add_players(self.session.name, self.players)

        mock_find_session_by_name.assert_called_once_with(self.session.name)
        mock_update.assert_called_once()
        self.assertEqual(result.name, self.session.name)
        self.assertEqual(result.players, self.players)

    @patch("project.repository.session_repository.update")
    @patch("project.repository.session_repository.find_session_by_name", return_value=session_with_players)
    def test_start_session(self, mock_find_session_by_name, mock_update):
        result = self.session_with_players.start(self.session_with_players.name)

        mock_find_session_by_name.assert_called_once_with(self.session_with_players.name)
        mock_update.assert_called_once()
        self.assertEqual(result.name, self.session_with_players.name)
        self.assertEqual(result.players, self.players)
        self.assertTrue(result.started)

    @patch("project.repository.session_repository.find_session_by_name", return_value=session)
    def test_raise_BusinessException_when_try_start_session_without_players(self, mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session.start(self.session.name)
            mock_find_session_by_name.assert_called_once_with(self.session.name)

    @patch("project.repository.session_repository.update")
    @patch("project.repository.session_repository.find_session_by_name", return_value=session_started)
    def test_finish_session(self, mock_find_session_by_name, mock_update):
        result = self.session_started.finish(self.session_started.name)

        mock_find_session_by_name.assert_called_once_with(self.session_started.name)
        mock_update.assert_called_once()
        self.assertEqual(result.name, self.session_started.name)
        self.assertEqual(result.players, self.players)
        self.assertTrue(result.finished)

    @patch("project.repository.session_repository.find_session_by_name", return_value=session)
    def test_raise_BusinessException_when_try_finish_not_started_session(self, mock_find_session_by_name):
        with self.assertRaises(Exception):
            self.session.finish(self.session.name)
            mock_find_session_by_name.assert_called_once_with(self.session.name)
