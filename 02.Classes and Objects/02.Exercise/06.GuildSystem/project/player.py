class Player:
    DEFAULT_GUILD = 'Unaffiliated'

    def __init__(self, name: str, hp: int, mp: int, ):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        on_new_row = '\n'
        player_info = f"Name: {self.name}\n"
        player_info += f"Guild: {self.guild}\n"
        player_info += f"HP: {self.hp}\n"
        player_info += f"MP: {self.mp}\n"
        player_info += on_new_row.join(f'==={sn} - {smc}' for sn, smc in self.skills.items())
        return player_info