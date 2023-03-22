from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str, ):
        self.name = name
        self.players: List = []

    def assign_player(self, player: Player):
        if player.guild == Player.DEFAULT_GUILD:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        player = [self.players.pop(self.players.index(p)) for p in self.players if p.name == player_name]
        if player:
            player[0].guild = Player.DEFAULT_GUILD
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        nr = '\n'
        guild_info = f"Guild: {self.name}\n"
        guild_info += nr.join([f'{p.player_info()}' for p in self.players])
        return guild_info
