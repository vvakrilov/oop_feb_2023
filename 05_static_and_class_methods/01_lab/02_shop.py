class Shop:
    def __init__(self, name: str, type: str, capacity: int, ):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity <= len(self.items):
            return "Not enough capacity in the shop"
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        pass
