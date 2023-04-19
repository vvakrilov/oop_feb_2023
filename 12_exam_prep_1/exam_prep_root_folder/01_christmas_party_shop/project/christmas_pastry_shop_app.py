from typing import List

from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List = []
        self.delicacies: List = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if list(filter(lambda x: x.name is name, self.delicacies)):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if list(filter(lambda x: x.booth_number is booth_number, self.booths)):
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and number_of_people <= booth.capacity:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booths_by_number = list(b for b in self.booths if b.booth_number is booth_number)
        delicacies_by_name = list(d for d in self.delicacies if d.name is delicacy_name)
        if not booths_by_number:
            raise Exception(f"Could not find booth {booth_number}!")
        if not delicacies_by_name:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth, delicacy = booths_by_number[0], delicacies_by_name[0]
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = list(filter(lambda b: b.booth_number is booth_number, self.booths))[0]
        bill = booth.price_for_reservation + sum(list(d.price for d in booth.delicacy_orders))
        booth.is_reserved = False
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        self.income += bill
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
