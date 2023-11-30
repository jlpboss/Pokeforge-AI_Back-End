from pokeforge.schema.pokemonSchema import *
from pokeforge.PokeForgeSandbox.battletest1 import calc_battle_win, Pokemon
#import calc_battle_win, Pokemon
def generate_new_pokemon(pokemonIn: PokemonIn, realPokemonInTier: dict):
    

    return PokemonOut(name= pokemonIn.name, types=pokemonIn.types, tier=pokemonIn.tier, baseStats={"hp":45,"atk":49,"def":49,"spa":65,"spd":65,"spe":45})