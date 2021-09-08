import unittest

from project.domain.person import Person


class PersonTest(unittest.TestCase):

    def test_person_init(self):
        person = Person(
            name="John Doe",
            date_of_birth="1990-04-03",
            is_associate=True
        )

        self.assertEqual(person.name, 'John Doe')
        self.assertEqual(person.date_of_birth, '1990-04-03')
        self.assertEqual(person.is_associate, True)

    def test_create_person_from_dict(self):
        person_dict = {
            "name": "John Doe",
            "date_of_birth": "1990-04-03",
            "is_associate": True
        }

        person = Person.from_dict(person_dict)
        self.assertEqual(person.name, 'John Doe')
        self.assertEqual(person.date_of_birth, '1990-04-03')
        self.assertEqual(person.is_associate, True)

    def test_convert_person_to_dict(self):
        person_dict = {
            "name": "John Doe",
            "date_of_birth": "1990-04-03",
            "is_associate": True
        }

        person = Person(
            name="John Doe",
            date_of_birth="1990-04-03",
            is_associate=True
        )

        response = Person.to_dict(person)
        self.assertEqual(response, person_dict)

    def test_create_person_from_dict_and_convert_person_to_dict(self):
        person_dict = {
            "name": "John Doe",
            "date_of_birth": "1990-04-03",
            "is_associate": True
        }

        person = Person.from_dict(person_dict)
        response = Person.to_dict(person)
        self.assertEqual(response, person_dict)
