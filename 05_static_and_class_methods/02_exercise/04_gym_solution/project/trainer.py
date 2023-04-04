class Trainer:
    name: str
    _id_counter = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self._id_counter += 1

    @staticmethod
    def get_next_id():
        return Trainer._id_counter + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
