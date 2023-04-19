class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


from unittest import TestCase, main


class TestPerson(TestCase):
    def setUp(self):
        self.person = Person('first_name', 'last_name', 100)

    def test_init_(self):
        self.assertEqual('first_name', self.person.first_name)
        self.assertEqual('last_name', self.person.last_name)
        self.assertEqual(100, self.person.age)

    def test_get_full_name_correct_string(self):
        self.assertEqual('first_name last_name', self.person.get_full_name())

    def test_get_info_correct_string(self):
        self.assertEqual('first_name last_name is 100 years old', self.person.get_info())


if __name__ == '__main__':
    main()
