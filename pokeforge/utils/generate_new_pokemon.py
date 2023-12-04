from pokeforge.schema.pokemonSchema import *
from pokeforge.utils.calc_battle_cython.batch_fitness import calculate_batch_fitness, cython_battle
import random
from pokeforge.utils.mutate_pokemon import mutate_pokemon
from pokeforge.utils.crossover_pokemon import crossover_pokemon

#import calc_battle_win, Pokemon
def generate_new_pokemon(pokemonIn: PokemonIn, realPokemonInTier: dict):

    batch = []
    for num in range(100):
        random_mon = Pokemon(name=f"Random {num}", baseStats={"hp": random.randint(40, 200), "atk": random.randint(40, 200), "def": random.randint(40, 200), "spe": random.randint(40, 200), "spa": random.randint(40, 200), "spd": random.randint(40, 200)})
        batch.append(random_mon)

    num_generations = 10

    for generation in range(num_generations):

        top_100 = find_top_x(batch, realPokemonInTier, 10)

        new_batch = []
        for _ in range(100):
            parent1, parent2 = random.choice(top_100), random.choice(top_100)
            child = crossover_pokemon(parent1, parent2)
            mutated_child = mutate_pokemon(child)
            new_batch.append(mutated_child)

        batch = new_batch

    out = find_top_x(batch, realPokemonInTier, 1)

    return PokemonOut(name = pokemonIn.name, types = pokemonIn.ty, baseStats = out[1].BaseStats, tier = pokemonIn.tier)  #out[1]

def find_top_x(batch, realPokemonInTier, num: int):
        fitness_values = calculate_batch_fitness(batch, realPokemonInTier)

        creatures_with_fitness = list(zip(batch, fitness_values))

        creatures_with_fitness = sorted(creatures_with_fitness, key=lambda x: x[1])

        top_x = [creature for creature, _ in creatures_with_fitness[:num]]

        return top_x


if __name__ == '__main__':
    testmon = PokemonIn(name = 'test', types = [], tier = "test")
    generate_new_pokemon(testmon, {})