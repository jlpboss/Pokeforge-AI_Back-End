# import sys
# sys.path.append('/workspace/pokeforge/pokeforge/utils/calc_battle_cython/')
#
# import cython_battle
from pokeforge.utils.calc_battle_cython.battle import calc_battle_win
from random import randint

def calculate_batch_fitness(batch, realmons):
    fullsum = []
    for pokemon in batch:
        sumA = []
        for pokemon2 in realmons:
            # cython_pokemon_1 = cython_battle.Pokemon(batch[pokemon].name, batch[pokemon].baseStats)
            # cython_pokemon_2 = cython_battle.Pokemon(realmons[pokemon2].name, realmons[pokemon2].baseStats)
            # sumA.append(cython_battle.calc_battle_win(cython_pokemon_1, cython_pokemon_2))
            sumA.append(calc_battle_win(pokemon, realmons[pokemon2]))
        fullsum.append(sum(sumA) / len(sumA))
    return fullsum


if __name__ == '__main__':
    batch = []
    for num in range(1000):
        random_mon = cython_battle.Pokemon(name=f"Random {num}", baseStats={"hp": randint(40, 200), "atk": randint(40, 200), "def": randint(40, 200), "spe": randint(40, 200), "spa": randint(40, 200), "spd": randint(40, 200)})
        batch.append(random_mon)

    batch2 = []
    for num in range(1000):
        random_mon = cython_battle.Pokemon(name=f"Random {num}", baseStats={"hp": randint(40, 200), "atk": randint(40, 200), "def": randint(40, 200), "spe": randint(40, 200), "spa": randint(40, 200), "spd": randint(40, 200)})
        batch2.append(random_mon)

    print(calculate_batch_fitness(batch, batch2))
