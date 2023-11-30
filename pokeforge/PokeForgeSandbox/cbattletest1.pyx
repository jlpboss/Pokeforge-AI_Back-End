# cython: language_level=3

from typing import Optional, Dict
from cython import boundscheck, wraparound

cdef class Pokemon:
    cdef str name
    cdef Dict[str, int] baseStats

    def __init__(self, name: str, baseStats: Dict[str, int]):
        self.name = name
        self.baseStats = baseStats

cdef calc_dmg(double atk, double def_):
    return (((2100 * (atk / def_)) / 50) + 2) * 1.065 * 1.5

@boundscheck(False)
@wraparound(False)
cpdef calc_battle_win(Pokemon random_pokemon, Pokemon real_pokemon):
    cdef double rand_hp = (random_pokemon.baseStats['hp'] * 2) + 110
    cdef double real_hp = (real_pokemon.baseStats['hp'] * 2) + 110

    cdef double rand_atk_stat = max(random_pokemon.baseStats['atk'], random_pokemon.baseStats['spa'])
    cdef double real_atk_stat = max(real_pokemon.baseStats['atk'], real_pokemon.baseStats['spa'])
    
    cdef double rand_atk = (rand_atk_stat * 2) + 5
    cdef double real_atk = (real_atk_stat * 2) + 5

    cdef double real_def_stat = real_pokemon.baseStats['def'] if real_pokemon.baseStats['atk'] >= real_pokemon.baseStats['spa'] else real_pokemon.baseStats['spd']
    cdef double rand_def_stat = random_pokemon.baseStats['def'] if random_pokemon.baseStats['atk'] >= random_pokemon.baseStats['spa'] else random_pokemon.baseStats['spd']

    cdef double real_def = (real_def_stat * 2) + 5
    cdef double rand_def = (rand_def_stat * 2) + 5

    cdef double rand_dmg_to_real = calc_dmg(rand_atk, real_def)
    cdef double real_dmg_to_rand = calc_dmg(real_atk, rand_def)

    if random_pokemon.baseStats['spe'] > real_pokemon.baseStats['spe']:
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    cdef int max_iterations = 1000

    for _ in range(max_iterations):
        rand_hp -= real_dmg_to_rand
        if rand_hp <= 0:
            return 0
        real_hp -= rand_dmg_to_real
        if real_hp <= 0:
            return 1

    return -1