import random
import copy
from init_pop import *
from load_dist import *
from two_opt import *
from util import *


def check_cases(initial_population, distances, generations):
    if None in (initial_population, distances):
        return True
    if generations is None:
        return True
    if generations <= 0:
        return True
    return False


def get_minimum(collection, distances, calculated_costs):
    min_cost = float('Inf')
    min_path = None

    for path in collection:
        if path in calculated_costs:
            path_cost = calculated_costs[path]
        else:
            path_cost = cost(path, distances)
            calculated_costs[path] = path_cost
        if path_cost is not None and path_cost < min_cost:
            min_cost = path_cost
            min_path = path

    return min_path


def parent_selection(population, distances, calculated_cost):
    k = 5
    num_parents = len(population) / 2
    if num_parents % 2 != 0:
        num_parents += 1

    parents = []
    while len(parents) < num_parents:
        contenders = random.sample(population, k)
        winner = get_minimum(contenders, distances, calculated_cost)
        parents.append(winner)

    return parents


def reproduction(parent1, parent2):
    n = len(parent1)
    start = random.randint(0, n - 3)
    end = random.randint(start + 2, n - 1)
    child1 = [-1] * n
    child2 = [-1] * n

    child1[start:end + 1] = parent1[start:end + 1]
    child2[start:end + 1] = parent2[start:end + 1]

    c1_i = (end + 1) % n
    for gene in parent2:
        if gene not in child1:
            child1[c1_i] = gene
            c1_i = (c1_i + 1) % n

    c2_i = (end + 1) % n
    for gene in parent1:
        if gene not in child2:
            child2[c2_i] = gene
            c2_i = (c2_i + 1) % n

    return tuple(child1), tuple(child2)


def get_next_gen(parents):
    next_gen = []
    reproduction_rate = len(parents)

    for i in range(0, reproduction_rate, 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        child1, child2 = reproduction(parent1, parent2)
        next_gen.extend([child1, parent1, child2, parent2])

    return next_gen


def ga_tsp(initial_population, distances, generations):
    if check_cases(initial_population, distances, generations):
        return None

    population = copy.deepcopy(initial_population)
    calculated_cost = {}

    for generation in range(0, generations):
        parents = parent_selection(population, distances, calculated_cost)
        next_gen = get_next_gen(parents)
        population = next_gen

    best_path = get_minimum(population, distances, calculated_cost)
    return best_path
