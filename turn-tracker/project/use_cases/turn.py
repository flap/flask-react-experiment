import collections


class Turn:
    """
    Create the object turn. A turn must indicate:
        - the current player
        - the next player to play when a player ends its turn
        - the skipped players
    """
    skipped_players = []

    def __init__(self, players):
        self.players = players

    def __eq__(self, other):
        if isinstance(other, Turn):
            return self._compare(self.players, other.players)
        return False

    @staticmethod
    def _compare(x, y):
        return collections.Counter(x) == collections.Counter(y)

    def current_player(self):
        """
        :return the current player
        """
        return self.players[0]

    def end_turn(self):
        """
        End the turn of the current player.
        Validates if the following players can play (have not skipped his/hers turn).
        :return the following player
        """
        player_to_skip = next((i for i, p in enumerate(self.skipped_players) if p == self.players[1]), False)
        if player_to_skip is not False:
            self.skipped_players.pop(player_to_skip)
            self._get_next_player()
            return self.end_turn()
        return self._get_next_player()

    def _get_next_player(self):
        player = self.players.pop(0)
        self.players.append(player)
        return self.players[0]

    def skip(self):
        """
        Set that the player will not play in the upcoming turn.
        So it will pass the turn ti the next player.
        """
        self.skipped_players.append(self.players[0])
