from pokeforge.schema.pokemonSchema import *
import random

def crossover_pokemon(pokemon_1: Pokemon, pokemon_2: Pokemon, generation: int, batch_num: int):
    
    child_pokemon = Pokemon(f"Gen: {generation}, num: {batch_num}", {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0})

    for stat in child_pokemon.baseStats:
        coin_flip = random.randint(0,1)
        if coin_flip:
            child_pokemon.baseStats[stat] = pokemon_2.baseStats[stat]
        else:
            child_pokemon.baseStats[stat] = pokemon_1.baseStats[stat]
        
    return child_pokemon