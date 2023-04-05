from abc import ABC, abstractmethod


class Animal(ABC):
    _default_food_value = 0
    name: str
    weight: float
    food_eaten: int
    SOUNDS = {
        "Owl": "Hoot Hoot",
        "Hen": "Cluck",
        "Mouse": "Squeak",
        "Dog": "Woof!",
        "Cat": "Meow",
        "Tiger": "ROAR!!!",
    }
    ACCEPTABLE_FOOD: list = []
    WEIGHT_PER_FOOD = 0

    def __init__(self, name: str, weight: float, food_eaten: int = _default_food_value):
        self.acceptable_foods = self.ACCEPTABLE_FOOD
        self.weight_per_food = self.WEIGHT_PER_FOOD
        self.name: str = name
        self.weight: float = weight
        self.food_eaten: int = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if type(food) not in self.acceptable_foods:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * self.weight_per_food
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    wing_size: float

    def __init__(self, name, weight, wing_size: float, ):
        super().__init__(name, weight, )
        self.wing_size: float = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    living_region: str

    def __init__(self, name, weight, living_region: str, ):
        super().__init__(name, weight, )
        self.living_region: str = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
