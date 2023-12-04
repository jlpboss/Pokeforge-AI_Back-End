from pokeforge.schema.pokemonSchema import *

def crossover_pokemon(pokemon_1: Pokemon, pokemon_2: Pokemon):
    
    for stat in pokemon_1.baseStats:
        pokemon_1.baseStats[stat] = (pokemon_1.baseStats[stat] + pokemon_2.baseStats[stat]) / 2
    pokemon_1.name = pokemon_1.name + pokemon_2.name
    return pokemon_1