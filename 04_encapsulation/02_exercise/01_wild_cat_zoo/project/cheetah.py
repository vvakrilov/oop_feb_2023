from project.animal import Animal


class Cheetah(Animal):
    CARE_COST = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=self.CARE_COST)
