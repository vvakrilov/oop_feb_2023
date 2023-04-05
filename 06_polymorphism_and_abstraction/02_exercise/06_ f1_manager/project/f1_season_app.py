from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    red_bull_team: RedBullTeam
    mercedes_team: MercedesTeam

    def __init__(self, red_bull_team=None, mercedes_team=None):
        self.red_bull_team = red_bull_team
        self.mercedes_team = mercedes_team

    def register_team_for_season(self, team_name: str, budget: int):
        valid_teams = {"Red Bull": RedBullTeam, "Mercedes": MercedesTeam}
        if team_name not in valid_teams:
            raise ValueError("Invalid team name!")
        obj = valid_teams[team_name](budget)
        if team_name == "Red Bull":
            self.red_bull_team = obj
        if team_name == "Mercedes":
            self.mercedes_team = obj
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):

        if self.red_bull_team is None and self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        rb_review = RedBullTeam.calculate_revenue_after_race(self.red_bull_team, red_bull_pos)
        mb_review = MercedesTeam.calculate_revenue_after_race(self.mercedes_team, mercedes_pos)

        better_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return f"Red Bull: {rb_review}. Mercedes: {mb_review}. " \
               f"{better_team} is ahead at the {race_name} race."
