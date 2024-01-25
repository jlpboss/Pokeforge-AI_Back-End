from pokeforge.schema.pokemonSchema import *
from pokeforge.utils.calc_battle_cython.batch_fitness import calculate_batch_fitness
import random
from pokeforge.utils.mutate_pokemon import mutate_pokemon
from pokeforge.utils.crossover_pokemon import crossover_pokemon


def generate_new_pokemon(pokemonIn: PokemonIn, realPokemonInTier: dict):
    
    num_pokemon = 1000
    num_generations = 100
    num_top_perfomers = 200
    batch = []

    for num in range(num_pokemon):
        random_mon = Pokemon(name=f"Random {num}", baseStats={"hp": random.randint(40, 200), "atk": random.randint(40, 200), "def": random.randint(40, 200), "spa": random.randint(40, 200), "spd": random.randint(40, 200), "spe": random.randint(40, 200)})
        batch.append(random_mon)
    
    

    for generation in range(num_generations):
        
        top_perfomers = find_top_x(batch, realPokemonInTier, num_top_perfomers)
        new_batch = []
        for batch_num in range(num_pokemon):
            
            parent1, parent2 = random.choice(top_perfomers), random.choice(top_perfomers)
            child = crossover_pokemon(parent1, parent2, generation, batch_num)
            mutated_child = mutate_pokemon(child)
            new_batch.append(mutated_child)

        batch = new_batch
    
    top_5 = find_top_x(batch, realPokemonInTier, 5)
    lowest_bst = 10000000000
    lowest_bst_pokemon = None

    for pokemon in top_5:
        sum = 0
        print(pokemon.baseStats)
        for stat in pokemon.baseStats:
            sum += pokemon.baseStats[stat]
        if sum < lowest_bst:
            lowest_bst_pokemon = pokemon
            lowest_bst = sum
    return PokemonOut(name = pokemonIn.name, types = pokemonIn.types, baseStats = lowest_bst_pokemon.baseStats, tier = pokemonIn.tier)  #out[1]

def find_top_x(batch, realPokemonInTier, num: int):
    fitness_values = calculate_batch_fitness(batch, realPokemonInTier)
    print(sum(fitness_values) / len(fitness_values))
    creatures_with_fitness = list(zip(batch, fitness_values))

    creatures_with_fitness = sorted(creatures_with_fitness, key=lambda x: abs(x[1] - 0.5))
    
    top_x = [creature for creature, _ in creatures_with_fitness[:num]]
    
    return top_x
