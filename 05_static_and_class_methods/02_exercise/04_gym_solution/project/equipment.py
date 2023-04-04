import itertools


class Equipment:
    name: str
    _id_counter = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self._id_counter += 1

    @staticmethod
    def get_next_id():
        return Equipment._id_counter + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
