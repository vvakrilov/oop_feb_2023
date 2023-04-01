class Shop:
    name: str
    s_type: str
    capacity: int
    items: dict

    def __init__(self, name: str, s_type: str, capacity: int, ):
        self.name = name
        self.type = s_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, c_type: str):
        return cls(name, c_type, 10)

    def add_item(self, item_name):
        if self.capacity <= sum(self.items.values()):
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        item_amount = self.items.get(item_name)

        if item_amount is None or item_amount - amount < 0:
            return f"Cannot remove {amount} {item_name}"

        result = self.items[item_name] - amount
        self.items[item_name] = result

        if result == 0:
            self.items.pop(item_name)

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)

# import unittest
#
#
# class ShopTests(unittest.TestCase):
#     def setUp(self):
#         self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
#
#     def test_add_item_success(self):
#         result = self.fresh_shop.add_item("Bananas")
#         self.assertEqual(self.fresh_shop.items["Bananas"], 1)
#         self.assertEqual(result, "Bananas added to the shop")
#
#     def test_remove_item_success(self):
#         self.fresh_shop.add_item("Bananas")
#         result = self.fresh_shop.remove_item("Bananas", 1)
#         self.assertEqual(result, "1 Bananas removed from the shop")
#
#     def test_remove_item_unsuccessful(self):
#         self.fresh_shop.add_item("Bananas")
#         result = self.fresh_shop.remove_item("Tomatoes", 2)
#         self.assertEqual(result, "Cannot remove 2 Tomatoes")
#
#     def test_repr(self):
#         self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")
#
#
# if __name__ == "__main__":
#     unittest.main()
