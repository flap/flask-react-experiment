import unittest

from project.domain.player import Player


class PlayerTest(unittest.TestCase):

    def test_player_init(self):
        player = Player(
            name="John Doe",
            date_of_birth="1990-04-03",
            is_associate=True,
            position=1,
            is_host=True
        )

        self.assertEqual(player.name, 'John Doe')
        self.assertEqual(player.date_of_birth, '1990-04-03')
        self.assertEqual(player.is_associate, True)
        self.assertEqual(player.position, 1)
        self.assertEqual(player.is_host, True)

    def test_create_player_from_dict(self):
        player_dict = {
            "name": "John Doe",
            "date_of_birth": "1990-04-03",
            "is_associate": True,
            "position": 1,
            "is_host": True
        }

        player = Player.from_dict(player_dict)
        self.assertEqual(player.name, 'John Doe')
        self.assertEqual(player.date_of_birth, '1990-04-03')
        self.assertEqual(player.is_associate, True)
        self.assertEqual(player.position, 1)
        self.assertEqual(player.is_host, True)

    def test_convert_player_to_dict(self):
        player_dict = {
            "name": "John Doe",
            "date_of_birth": "1990-04-03",
            "is_associate": True,
            "position": 1,
            "is_host": True
        }

        player = Player(
            name="John Doe",
            date_of_birth="1990-04-03",
            is_associate=True,
            position=1,
            is_host=True
        )

        response = Player.to_dict(player)
        self.assertEqual(response, player_dict)

    def test_create_player_from_dict_and_convert_player_to_dict(self):
        player_dict = {
            "name": "John Doe",
            "date_of_birth": "1990-04-03",
            "is_associate": True,
            "position": 1,
            "is_host": True
        }

        player = Player.from_dict(player_dict)
        response = Player.to_dict(player)
        self.assertEqual(response, player_dict)
