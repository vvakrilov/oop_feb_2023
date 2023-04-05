from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    ACCEPTABLE_FOOD = [Meat]
    WEIGHT_PER_FOOD = 0.25

    def make_sound(self):
        return self.SOUNDS[self.__class__.__name__]


class Hen(Bird):
    WEIGHT_PER_FOOD = 0.35

    def make_sound(self):
        return self.SOUNDS[self.__class__.__name__]

    def feed(self, food):
        self.weight += food.quantity * self.weight_per_food
        self.food_eaten += food.quantity
