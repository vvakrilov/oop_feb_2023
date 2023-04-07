from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }

    VALID_RAM_SIZE = (2, 2, 128)  # min, step, max

    def __init__(self, manufacturer, model, processor=None, ram=None, price=0):
        super().__init__(manufacturer, model, processor, ram, price)
        self.ram_max_size = list(r for r in self.ram_size(*self.VALID_RAM_SIZE))
        self.ram_price = list(p * 100 for p in range(1, len(self.ram_max_size) + 1))

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in self.ram_max_size:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = self.AVAILABLE_PROCESSORS[processor] + self.ram_price[self.ram_max_size.index(ram)]
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {ram}GB RAM for {self.price}$."
