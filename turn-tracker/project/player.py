class Player:
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
        self.name = name
        self.date_of_birth = date_of_birth,
        self.is_associate = is_associate,
        self.position = position,
        self.is_host = is_host

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and self.date_of_birth == other.date_of_birth and \
                   self.is_associate == other.is_associate and self.position == other.position and \
                   self.is_host == other.is_host
        return False
