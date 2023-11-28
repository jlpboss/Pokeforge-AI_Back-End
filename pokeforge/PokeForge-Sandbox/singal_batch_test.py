from cbattletest1 import calc_battle_win, Pokemon
from random import randint


batch = []
for num in range(1000):
    random_mon = Pokemon(name=f"Random{num}", baseStats={"hp": randint(40, 200), "atk": randint(40, 200), "def": randint(40, 200), "spe": randint(40, 200), "spa": randint(40, 200), "spd": randint(40, 200)})
    batch.append(random_mon)

batch2 = []
for num in range(1000):
    random_mon = Pokemon(name=f"Random{num}", baseStats={"hp": randint(40, 200), "atk": randint(40, 200), "def": randint(40, 200), "spe": randint(40, 200), "spa": randint(40, 200), "spd": randint(40, 200)})
    batch2.append(random_mon)

print(batch)
print(batch2)

fullsum = []
for pokemon in batch:
    sumA = []
    print(dir(pokemon))
    for pokemon2 in batch2:
        sumA.append(calc_battle_win(pokemon, pokemon2))
    fullsum.append(sum(sumA) / len(sumA))

print(fullsum)