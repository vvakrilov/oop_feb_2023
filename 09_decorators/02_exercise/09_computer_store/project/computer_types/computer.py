from abc import ABC, abstractmethod
from typing import List


class Computer(ABC):
    manufacturer: str
    model: str
    processor: str
    ram: int
    price: int

    def __init__(self, manufacturer: str, model: str,
                 processor: str = None, ram: int = None, price: int = 0):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = processor
        self.ram: int = ram
        self.price: int = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int, ):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @staticmethod
    def ram_size(min_size: int, step: int, max_size: int):
        """yields list of integers from min powered by step to max"""
        size = min_size
        while size <= max_size:
            yield size
            size *= step
