from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }

    VALID_RAM_SIZE = (2, 2, 64)  # min, step, max

    def __init__(self, manufacturer, model, processor=None, ram=None, price=0):
        super().__init__(manufacturer, model, processor, ram, price)
        self.ram_max_size = list(r for r in self.ram_size(*self.VALID_RAM_SIZE))
        self.ram_price = list(p * 100 for p in range(1, len(self.ram_max_size) + 1))

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in self.ram_max_size:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = self.AVAILABLE_PROCESSORS[processor] + self.ram_price[self.ram_max_size.index(ram)]
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {ram}GB RAM for {self.price}$."
