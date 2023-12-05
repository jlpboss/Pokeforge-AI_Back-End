from pokeforge.schema.pokemonSchema import Pokemon
import random


def mutate_pokemon(pokemon: Pokemon):
    baseStatsCopy = pokemon.baseStats
    for stat in baseStatsCopy:
        baseStatsCopy[stat] = round(float(baseStatsCopy[stat]) * (0.5 + random.random()))
    pokemon.baseStats = baseStatsCopy
    return pokemon

if __name__ == '__main__':
    testmon = Pokemon(name = 'test', baseStats={"hp":45,"atk":49,"def":49,"spa":65,"spd":65,"spe":45})
    mutate_pokemon(testmon)