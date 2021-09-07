from collections import namedtuple

from project.domain.person import Person


class Player(Person):
    """
    Create the object palyer. A player must have:
        - name
        - date of birth
        - a position in the players queue
    A player may be:
        - an associate to the Board Games Association
        - a host for a board game session
    """

    def __init__(self, name, date_of_birth, is_associate, position, is_host):
        super().__init__(name, date_of_birth, is_associate)
        self.position = position
        self.is_host = is_host

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self.date_of_birth == other.date_of_birth and \
                   self.is_associate == other.is_associate and self.position == other.position and \
                   self.is_host == other.is_host
        return False

    @staticmethod
    def from_dict(d):
        return namedtuple("Player", d.keys())(*d.values())

    def to_dict(self):
        return {'name': self.name, 'date_of_birth': self.date_of_birth, 'is_associate': self.is_associate,
                'position': self.position, 'is_host': self.is_host}
