from abc import ABC

from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam, ABC):
    TEAM_SPONSORSHIP_PER_PLACE = {
        1: 1500 * 1000,
        2: 800 * 1000,
        8: 20 * 1000,
        10: 10 * 1000,
    }
    TEAM_EXPENSES_PER_RACE = 250 * 1000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        for position in self.TEAM_SPONSORSHIP_PER_PLACE:
            if position == race_pos:
                revenue = self.TEAM_SPONSORSHIP_PER_PLACE[position] - self.TEAM_EXPENSES_PER_RACE
                self.budget += revenue
                return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
