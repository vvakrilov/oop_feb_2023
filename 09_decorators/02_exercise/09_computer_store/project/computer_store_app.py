from typing import List
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    warehouse: List
    profits: int
    initial_profit_value: int = 0
    VALID_TYPES = {"Laptop": Laptop, "Desktop Computer": DesktopComputer}

    def __init__(self, ):
        self.warehouse: List = []
        self.profits: int = self.initial_profit_value

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        comp = self.VALID_TYPES[type_computer](manufacturer, model, processor, ram)
        result = comp.configure_computer(processor, ram)
        if result:
            self.warehouse.append(comp)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
                self.warehouse.remove(comp)
                self.profits += comp.price - client_budget
                return f"{str(comp)} sold for {client_budget}$."
        else:
            raise Exception("Sorry, we don't have a computer for you.")
