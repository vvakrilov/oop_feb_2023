from typing import List

from project.dvd import DVD


class Customer:
    name: str
    age: int
    id: int

    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        _id, name, age, count = self.id, self.name, self.age, len(self.rented_dvds)
        dvds = ', '.join(d.name for d in self.rented_dvds)

        return f"{_id}: {name} of age {age} has {count} rented DVD's ({dvds})"
