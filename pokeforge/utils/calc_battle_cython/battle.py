from pokeforge.schema.pokemonSchema import Pokemon

def calculate_hp(base_hp: int) -> int:
    return (base_hp * 2) + 110

def calculate_stat(stat: int) -> int:
    return (stat * 2) + 5

def calc_dmg(atk: int, def_: int, bp: int = 50, stab: float = 1.5, modifier: float = 1.065) -> int:
    return round((((2100 * (atk / def_)) / bp) + 2) * modifier * stab)

def calc_battle_win(random_pokemon: Pokemon, real_pokemon: Pokemon) -> int:
    rand_hp = calculate_hp(random_pokemon.baseStats['hp'])
    real_hp = calculate_hp(real_pokemon.baseStats['hp'])

    rand_atk_stat = max(random_pokemon.baseStats['atk'], random_pokemon.baseStats['spa'])
    real_atk_stat = max(real_pokemon.baseStats['atk'], real_pokemon.baseStats['spa'])
    
    rand_atk = calculate_stat(rand_atk_stat)
    real_atk = calculate_stat(real_atk_stat)

    real_def_stat = real_pokemon.baseStats['def'] if real_pokemon.baseStats['atk'] >= real_pokemon.baseStats['spa'] else real_pokemon.baseStats['spd']
    rand_def_stat = random_pokemon.baseStats['def'] if random_pokemon.baseStats['atk'] >= random_pokemon.baseStats['spa'] else random_pokemon.baseStats['spd']

    real_def = calculate_stat(real_def_stat)
    rand_def = calculate_stat(rand_def_stat)

    rand_dmg_to_real = calc_dmg(rand_atk, real_def)
    real_dmg_to_rand = calc_dmg(real_atk, rand_def)

    if random_pokemon.baseStats['spe'] > real_pokemon.baseStats['spe']:
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    MAX_ITERATIONS = 100

    for _ in range(MAX_ITERATIONS):
        rand_hp -= real_dmg_to_rand
        if rand_hp <= 0:
            return 0
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    return 0