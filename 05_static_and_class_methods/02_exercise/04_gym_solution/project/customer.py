class Customer:
    name: str
    address: str
    email: str
    _id_counter = 0

    def __init__(self, name: str, address: str, email: str, ):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self._id_counter += 1

    @staticmethod
    def get_next_id():
        return Customer._id_counter + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
