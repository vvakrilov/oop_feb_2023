from project.animals.animal import Animal


class Lion(Animal):
    CARE_COST = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=self.CARE_COST)
