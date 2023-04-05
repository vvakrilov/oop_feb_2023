from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    TEAM_SPONSORSHIP_PER_PLACE = {
        1: 1000 * 1000,
        3: 500 * 1000,
        5: 100 * 1000,
        7: 50 * 1000,
    }
    TEAM_EXPENSES_PER_RACE = 200 * 1000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        for position in self.TEAM_SPONSORSHIP_PER_PLACE.keys():
            if position == race_pos:
                revenue = self.TEAM_SPONSORSHIP_PER_PLACE[position] - self.TEAM_EXPENSES_PER_RACE
                self.budget += revenue
                return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
