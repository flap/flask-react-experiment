from collections import namedtuple


class Person:
    """
    Create the object person. A person must have:
        - name
        - date of birth
    A person may be:
        - an associate to the Board Games Association
    """

    def __init__(self, name, date_of_birth, is_associate):
        self.name = name
        self.date_of_birth = date_of_birth
        self.is_associate = is_associate

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.date_of_birth == other.date_of_birth and \
                   self.is_associate == other.is_associate
        return False

    @staticmethod
    def from_dict(d):
        return namedtuple("Person", d.keys())(*d.values())

    def to_dict(self):
        return {'name': self.name, 'date_of_birth': self.date_of_birth, 'is_associate': self.is_associate}
