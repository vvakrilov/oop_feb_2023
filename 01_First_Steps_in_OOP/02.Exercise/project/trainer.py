from typing import List

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name, ):
        self.name = name
        self.pokemons: List[Pokemon] = []

    @staticmethod
    def find_pokemon(p_name, p_list):
        for p in p_list:
            if p.name == p_name:
                return p

    def add_pokemon(self, pokemon: Pokemon):
        searched_pokemon = self.find_pokemon(pokemon.name, self.pokemons)
        if searched_pokemon:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, name):
        searched_pokemon = self.find_pokemon(name, self.pokemons)
        if not searched_pokemon:
            return f"Pokemon is not caught"
        self.pokemons.remove(searched_pokemon)
        return f"You have released {name}"

    def trainer_data(self):
        nr = '\n'
        data_message = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        data_message += f"- {(nr.join([p.pokemon_details() for p in self.pokemons]))}"
        return data_message
