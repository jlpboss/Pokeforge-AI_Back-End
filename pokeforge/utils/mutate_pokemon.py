from pokeforge.schema.pokemonSchema import Pokemon
import random


def mutate_pokemon(pokemon: Pokemon):
    # baseStatsCopy = pokemon.baseStats
    for stat in pokemon.baseStats:
        if random.random() > 0.95:
            rand_num = random.randint(-10,10)
            if rand_num + pokemon.baseStats[stat] > 0:
                pokemon.baseStats[stat] = int(round(float(pokemon.baseStats[stat]) + rand_num))
            
    # pokemon.baseStats = baseStatsCopy
    return pokemon
