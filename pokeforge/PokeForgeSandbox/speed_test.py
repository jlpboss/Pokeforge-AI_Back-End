# from cbattletest1 import calc_battle_win, Pokemon
from timeit import timeit

# random_pokemon = Pokemon(name="Random", baseStats={"hp": 100, "atk": 50, "def": 30, "spe": 70, "spa": 60, "spd": 40})
# real_pokemon = Pokemon(name="Real", baseStats={"hp": 120, "atk": 60, "def": 40, "spe": 60, "spa": 70, "spd": 50})

t1 = timeit(
    'calc_battle_win(Pokemon(name="Random", baseStats={"hp": 100, "atk": 50, "def": 30, "spe": 70, "spa": 60, "spd": 40}), Pokemon(name="Real", baseStats={"hp": 120, "atk": 60, "def": 40, "spe": 60, "spa": 70, "spd": 50}))',
    setup="from cbattletest1 import calc_battle_win, Pokemon",
    number=100_000
)
t2 = timeit(
    'calc_battle_win(Pokemon(name="Random", baseStats={"hp": 100, "atk": 50, "def": 30, "spe": 70, "spa": 60, "spd": 40}), Pokemon(name="Real", baseStats={"hp": 120, "atk": 60, "def": 40, "spe": 60, "spa": 70, "spd": 50}))',
    setup="from battletest1 import calc_battle_win, Pokemon",
    number=100_000
)

print(f"Python: {t2:.3f}")
print(f"Cython: {t1:.3f}")
print(f"Cython is {t2 / t1:.3f}x faster")

# result = calc_battle_win(random_pokemon, real_pokemon)
# print("Battle result:", result)