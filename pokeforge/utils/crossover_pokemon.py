from pokeforge.schema.pokemonSchema import *

def crossover_pokemon(pokemon_1: Pokemon, pokemon_2: Pokemon):
    # print('6.1.1')
    for stat in pokemon_1.baseStats:
        pokemon_1.baseStats[stat] = int((pokemon_1.baseStats[stat] + pokemon_2.baseStats[stat]) / 2)
        # print('6.1.2')
    # pokemon_1.name = pokemon_1.name + pokemon_2.name
    # print('6.1.3')
    return pokemon_1