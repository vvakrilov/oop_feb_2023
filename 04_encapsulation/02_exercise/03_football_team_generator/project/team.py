from typing import List
from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        if not [p for p in self.__players if p.name == player.name]:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player: str):
        for p in self.__players:
            if p.name == player:
                self.__players.remove(p)
                return p
        return f"Player {player} not found"
