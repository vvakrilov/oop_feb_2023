from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    TEAM_MINIMUM_BUDGET: int = 1000 * 1000
    TEAM_SPONSORSHIP_PER_PLACE: dict
    TEAM_EXPENSES_PER_RACE: int

    def __init__(self, budget: int):
        self.budget: int = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.TEAM_MINIMUM_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        ...
