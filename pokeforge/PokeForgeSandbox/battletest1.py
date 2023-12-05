from pokeforge.PokeForgeSandbox.pokemon_schema import Pokemon

def calc_dmg(atk, def_):
    # assume 50bp and stab
    return round((((2100 * (atk / def_)) / 50) + 2) * 1.065 * 1.5)

def calc_battle_win(random_pokemon: Pokemon, real_pokemon: Pokemon):
    rand_hp = (random_pokemon.baseStats['hp'] * 2) + 110
    real_hp = (real_pokemon.baseStats['hp'] * 2) + 110

    rand_atk_stat = max(random_pokemon.baseStats['atk'], random_pokemon.baseStats['spa'])
    real_atk_stat = max(real_pokemon.baseStats['atk'], real_pokemon.baseStats['spa'])
    
    rand_atk = (rand_atk_stat * 2) + 5
    real_atk = (real_atk_stat * 2) + 5

    real_def_stat = real_pokemon.baseStats['def'] if real_pokemon.baseStats['atk'] >= real_pokemon.baseStats['spa'] else real_pokemon.baseStats['spd']
    rand_def_stat = random_pokemon.baseStats['def'] if random_pokemon.baseStats['atk'] >= random_pokemon.baseStats['spa'] else random_pokemon.baseStats['spd']

    real_def = (real_def_stat * 2) + 5
    rand_def = (rand_def_stat * 2) + 5

    rand_dmg_to_real = calc_dmg(rand_atk, real_def)
    real_dmg_to_rand = calc_dmg(real_atk, rand_def)

    if random_pokemon.baseStats['spe'] > real_pokemon.baseStats['spe']:
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    max_iterations = 100

    for _ in range(max_iterations):
        rand_hp -= real_dmg_to_rand
        if rand_hp <= 0:
            return 0
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    return 0
