from project.repository import session_repository
from project.use_cases.turn import Turn


class GameSession:
    """
    Create the object game session. A game session must have:
        - name
        - turns
        - players
    A game session may be:
        - started
        - finished
    """

    def __init__(self, name, players: list = [], turn: Turn = None, started=False, finished=False):
        self.name = name
        self.players = players
        self.turn = turn
        self.started = started
        self.finished = finished

    def __eq__(self, other):
        if isinstance(other, GameSession):
            return self.name == other.name and self.players == other.players and self.turn == other.turn \
                   and self.started == other.started and self.finished == other.finished
        return False

    @staticmethod
    def create_session(name):
        session = GameSession(name)
        session_repository.save(session)
        return session

    def add_players(self, name, players: list):
        session = self._find_session(name)
        session.players = players
        session_repository.update(session)
        return session

    def start(self, name):
        """
        Start the board game session.
        It assumes that all players added previously will not be changed during the game.
        It defines who is first player in the turn.
        :return the first player (current player)
        """

        session = self._find_session(name)
        if not session.players:
            raise Exception
        # start first turn
        session.turn = Turn(session.players)
        session.started = True
        session_repository.update(session)
        return session.turn.current_player()

    def finish(self, name):
        """
        Finish the board game session.
        It saves the session current status.
        :return the session current status
        """

        session = self._find_session(name)
        if not session.started:
            raise Exception
        session.finished = True
        session_repository.update(session)
        return session

    def current_player(self, name):
        session = self._find_session(name)
        if not session.started or session.finished:
            raise Exception
        return session.turn.current_player()

    def end_turn(self, name):
        session = self._find_session(name)
        if not session.started or session.finished:
            raise Exception
        return session.turn.end_turn()

    def skip_turn(self, name):
        session = self._find_session(name)
        if not session.started or session.finished:
            raise Exception
        session.turn.skip()

    @staticmethod
    def _find_session(name):
        return session_repository.find_session_by_name(name)
