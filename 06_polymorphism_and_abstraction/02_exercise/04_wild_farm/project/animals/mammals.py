from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    ACCEPTABLE_FOOD = [Vegetable, Fruit]
    WEIGHT_PER_FOOD = 0.1

    def make_sound(self):
        return self.SOUNDS[self.__class__.__name__]


class Dog(Mammal):
    ACCEPTABLE_FOOD = [Meat]
    WEIGHT_PER_FOOD = 0.4

    def make_sound(self):
        return self.SOUNDS[self.__class__.__name__]


class Cat(Mammal):
    ACCEPTABLE_FOOD = [Vegetable, Meat]
    WEIGHT_PER_FOOD = 0.3

    def make_sound(self):
        return self.SOUNDS[self.__class__.__name__]


class Tiger(Mammal):
    ACCEPTABLE_FOOD = [Meat]
    WEIGHT_PER_FOOD = 1

    def make_sound(self):
        return self.SOUNDS[self.__class__.__name__]
