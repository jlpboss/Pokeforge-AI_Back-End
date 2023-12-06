# cython: language_level=3

cdef class Pokemon:
    cdef str name
    cdef dict[str, int] baseStats

    def __init__(self, name: str, baseStats: dict[str, int]):
        self.name = name
        self.baseStats = baseStats

cpdef int calculate_hp(int base_hp):
    return (base_hp * 2) + 110

cpdef int calculate_stat(int stat):
    return (stat * 2) + 5

cpdef int calc_dmg(int atk, int def_, int bp=50, float stab=1.5, float modifier=1.065):
    return round((((2100 * (atk / def_)) / bp) + 2) * modifier * stab)

cpdef int calc_battle_win(Pokemon random_pokemon, Pokemon real_pokemon):
    cdef int rand_hp = calculate_hp(<int>random_pokemon.baseStats['hp'])
    cdef int real_hp = calculate_hp(<int>real_pokemon.baseStats['hp'])

    cdef int rand_atk_stat = max(<int>random_pokemon.baseStats['atk'], <int>random_pokemon.baseStats['spa'])
    cdef int real_atk_stat = max(<int>real_pokemon.baseStats['atk'], <int>real_pokemon.baseStats['spa'])
    
    cdef int rand_atk = calculate_stat(rand_atk_stat)
    cdef int real_atk = calculate_stat(real_atk_stat)

    cdef int real_def_stat = real_pokemon.baseStats['def'] if real_pokemon.baseStats['atk'] >= real_pokemon.baseStats['spa'] else real_pokemon.baseStats['spd']
    cdef int rand_def_stat = random_pokemon.baseStats['def'] if random_pokemon.baseStats['atk'] >= random_pokemon.baseStats['spa'] else random_pokemon.baseStats['spd']

    cdef int real_def = calculate_stat(real_def_stat)
    cdef int rand_def = calculate_stat(rand_def_stat)

    cdef int rand_dmg_to_real = calc_dmg(rand_atk, real_def)
    cdef int real_dmg_to_rand = calc_dmg(real_atk, rand_def)

    if random_pokemon.baseStats['spe'] > real_pokemon.baseStats['spe']:
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    cdef int MAX_ITERATIONS = 100

    for _ in range(MAX_ITERATIONS):
        rand_hp -= real_dmg_to_rand
        if rand_hp <= 0:
            return 0
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    return 0
